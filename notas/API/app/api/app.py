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


def execute_query(query, conn=conn):
    cur = conn.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)
    try:
        cur.execute(query)
        results = cur.fetchall()
    except Exception as e:
        print(f"Error on the query: {e}")
        results = []
    cur.close()
    return json.dumps([x._asdict() for x in results], default=str)


def send_data(query, conn=conn):
    cur = conn.cursor()
    try:
        cur.execute(query)
        conn.commit()
    except Exception as e:
        print(f"Error at the insert: {e}")
        user_id = ""
    cur.close()


@app.route("/")
def home():
    query = "select * from users"
    return execute_query(query)


@app.route("/users", methods=["GET", "POST", "DELETE", "PATCH"])
def users():
    if request.method == "GET":
        user_id = request.args.get("id")
        if user_id:
            query = f"select * from users where id={user_id}"
            return execute_query(query)
        else:
            query = "select * from users"
            return execute_query(query)
    if request.method == "POST":
        users = json.loads(request.data)
        for user in users:
            query = f"insert into users (name, lastname, age) values ('{user['name']}', '{user['lastname']}', '{user['age']}')"
            send_data(query)
            user_id = execute_query("SELECT LASTVAL()")[0]
        return json.dumps({"user_id": user_id})
    if request.method == "DELETE":
        user_id = request.args.get("id")
        if user_id:
            send_data(f"delete from users where id={user_id}")
        return json.dumps({"user_id": user_id})
    if request.method == "PATCH":
        user_id = request.args.get("id")
        users = json.loads(request.data)
        for user in users:
            query = f"update users set (name, lastname, age) =  ('{user['name']}', '{user['lastname']}', '{user['age']}') where id={user_id}"
            send_data(query)
        return json.dumps({"user_id": user_id})


@app.route("/flights", methods=["GET"])
def flights():
    query = "select * from flights limit 100"
    return execute_query(query)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8080)
