from flask import Flask, request
import json
import psycopg2
import psycopg2.extras
import os
# Estructura del uri:
# "motor://user:password@host:port/database"
database_uri = f'postgresql://{os.environ["PGUSR"]}:{os.environ["PGPASS"]}@{os.environ["PGHOST"]}:5432/{os.environ["PGDB"]}'

app = Flask(__name__)
conn = psycopg2.connect(database_uri)

@app.route('/')
def home():
    cur = conn.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)
    cur.execute("select * from users")
    results = cur.fetchall()
    cur.close()
    return json.dumps([x._asdict() for x in results], default=str)


@app.route('/users', methods=["POST", "GET", "DELETE", "PATCH"])
def user():
    if request.method == 'GET':
        cur = conn.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)
        user_id = request.args.get("id")
        cur.execute(f"select * from users where id={user_id}")
        results = cur.fetchone()
        cur.close()
        return json.dumps(results._asdict(), default=str)
    if request.method == "POST":
        user = json.loads(request.data)
        cur = conn.cursor()
        cur.execute(
            "insert into users (name, lastname, age) values (%s, %s, %s)",
            (user[0]["name"], user[0]["lastname"], user[0]["age"]),
        )
        conn.commit()
        cur.execute("SELECT LASTVAL()")
        user_id = cur.fetchone()[0]
        cur.close()
        return json.dumps({"user_id": user_id})
    if request.method == "DELETE":
        cur = conn.cursor()
        user_id = request.args.get("id")
        cur.execute(f"delete from users where id={user_id}")
        conn.commit()
        cur.close()
        return json.dumps({"user_id": user_id})
    if request.method == "PATCH":
        user = json.loads(request.data)
        cur = conn.cursor()
        user_id = request.args.get("id")
        cur.execute(
            "update users set (name, lastname, age) = (%s,%s,%s) where id=%s ",
            (user[0]["name"], user[0]["lastname"], user[0]["age"], user_id),
        )
        conn.commit()
        cur.close()
        return json.dumps({"user_id": user_id})


@app.route('/flights', methods=['GET'])
def flights():
    cur = conn.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)
    user_id = request.args.get("id")
    cur.execute(f"select * from flights limit 100")
    results = cur.fetchall()
    cur.close()
    return json.dumps([x._asdict() for x in results], default=str)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8080)
