curl -X POST -H "Content-Type: application/json"\
     -d '{"name":"Pedro", "lastname":"Pérez", "age":33}'\
     0.0.0.0:8080/user

curl -X DELETE '0.0.0.0:8080/user?id=2'

curl -X PATCH -H "Content-Type: application/json"\
     -d '{"name":"Pedru", "lastname":"Péres", "age":44}'\
     '0.0.0.0:8080/user?id=3'

curl -X POST -H "Content-Type: application/json"\
     -d '[{"name":"Pedro", "lastname":"Pérez", "age":33},
     	  {"name":"Lucía", "lastname":"Juarez", "age":23}]'\
     0.0.0.0:8080/users


curl '0.0.0.0:8080/mesdia?mes=12&dia=12' > la_guadalupana.json
