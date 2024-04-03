# Mongodb

Containers built from this image will run a MongoDB server.

## Basic Commands

1. Pull Official MongoDB Image

```
docker pull mongo:latest
```

2. Run MongoDB Container in the Background

```
docker run -v .:/app -d -p 27017:27017 --name localhost_mongodb mongo --config /app/mongodb.conf
```

3. Rerun MongoDB Container

```
docker restart localhost_mongodb
```

3. Execute Commands in the MongoDB Container

```
docker exec -it localhost_mongodb mongo
```

## Mongodb Shell Commands

1. Enter Mongodb Shell

```
mongosh
```

2. Show Databases

```
show dbs
```

3. Use a Database

```
use <database_name>
```

## Reference

[Docker MongoDB](./Docker_MongoDB.md)

