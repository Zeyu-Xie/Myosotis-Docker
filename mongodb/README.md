# Mongodb

Containers built from this image will run a MongoDB server.

## Basic Commands

1. Pull Official MongoDB Image from Docker Hub

```
docker pull mongo:latest
```

2. Run MongoDB Server & Define Root User

```
docker run -v .:/app -d -p 27017:27017 --name [container_name] -e MONGO_INITDB_ROOT_USERNAME=[root_username] -e MONGO_INITDB_ROOT_PASSWORD=[root_password] mongo
```

3. Rerun MongoDB Container

```
docker restart [container_name]
```

4. Execute Commands in the Container

```
docker exec -it [container_name] /bin/bash
mongosh -u [root_username] -p [root_password]
```

or you can directly enter mongosh instead of bash

```
docker exec -it [container_name] mongosh -u [root_username] -p [root_password]
```

## Mongodb Shell Commands

1. Enter Mongodb Shell

```
mongosh -u [username] -p [password]
```

2. Show Databases

```
show dbs
```

3. Use a Database

```
use [database_name]
```

4. Show Collections

```
show collections
```

5. Show Documents in a Collection

```
db.[collection_name].find()
```

6. Insert a Document

```
db.[collection_name].insertOne({key: value})
```

7. Update a Document

```
db.[collection_name].updateOne({key: value}, {$set: {key: value}})
```

8. Delete a Document

```
db.[collection_name].deleteOne({key: value})
```

9. Drop a Collection

```
db.[collection_name].drop()
```

10. Drop a Database

```
db.dropDatabase()
```

11. Exit Mongodb Shell

```
exit
```

## Reference

[Docker MongoDB](./Docker_MongoDB.md)