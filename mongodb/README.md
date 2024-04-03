# Mongodb

Containers built from this image will run a MongoDB server.

## Basic Commands

1. Pull Official MongoDB Image

```
docker pull mongo:latest
```

2. Run MongoDB Container in the Background

```
docker run -d -p 27017:27017 --name localhost_mongodb mongo:latest
```

3. Execute Commands in the MongoDB Container

```
docker exec -it localhost_mongodb /bin/bash
```