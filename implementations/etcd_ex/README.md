## ETCD server implementation with FASTAPI

###### create docker volume
``
docker volume create --name=etcd_data
``
You can choose the location for docker volume manually. Else delete the volumes section from docker-compose.

###### POST
``
$ curl -X POST -H "Content-Type: application/json" 'http://localhost:5000/set_key?key=my_key&value=my_value'
``
###### GET
``
$ curl 'http://localhost:5000/get_key/my_key'
``
###### PUT/PATCH
``
$ curl -X PUT -H "Content-Type: application/json" 'http://localhost:5000/update_key/my_key?value=updated_value'
``
###### DELETE
``
$ curl -X DELETE 'http://localhost:5000/delete_key/my_key'
``