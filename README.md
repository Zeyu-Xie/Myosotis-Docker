# docker

## Commands

![Commands](https://github.com/Zeyu-Xie/docker/blob/6faa92f042b7a1edb5a567f02d949271bcc1cee1/commands.png?raw=true)

## Parameters

### Docker Build

| Parameter      | Usage                       | Description | Example                                  |
| -------------- | --------------------------- | ----------- | ---------------------------------------- |
| `-t`           | `-t [image name]`           | Tag         | `docker build -t myimage .`              |
| `-f`           | `-f [dockerfile path]`      | Dockerfile  | `docker build -f Dockerfile .`           |
| `--build-arg`  | `--build-arg [key]=[value]` | Build Arg   | `docker build --build-arg VERSION=1.0 .` |
| `--cache-from` | `--cache-from [image]`      | Cache From  | `docker build --cache-from myimage .`    |
| `--no-cache`   | `--no-cache`                | No Cache    | `docker build --no-cache .`              |
| `--pull`       | `--pull`                    | Pull        | `docker build --pull .`                  |
| `--quiet`      | `--quiet`                   | Quiet       | `docker build --quiet .`                 |
| `--progress`   | `--progress [type]`         | Progress    | `docker build --progress plain .`        |
| `--network`    | `--network [network]`       | Network     | `docker build --network mynetwork .`     |
| `--target`     | `--target [stage]`          | Target      | `docker build --target mytarget .`       |

### Docker Run

| Parameter      | Usage                             | Description    | Example                                             |
| -------------- | --------------------------------- | -------------- | --------------------------------------------------- |
| `-d`           | `-d`                              | Detached Mode  | `docker run -d [image]`                             |
| `-p`           | `-p [host port]:[container port]` | Port Mapping   | `docker run -p 8080:80 [image]`                     |
| `-i`           | `-i`                              | Interactive    | `docker run -i [image]`                             |
| `-v`           | `-v [host path]:[container path]` | Volume Mapping | `docker run -v /opt/datadir:/var/lib/mysql [image]` |
| `--name`       | `--name [container name]`         | Container Name | `docker run --name mycontainer [image]`             |
| `-e`           | `-e [key]=[value]`                | Environment    | `docker run -e MYSQL_ROOT_PASSWORD=123456 [image]`  |
| `--restart`    | `--restart [policy]`              | Restart Policy | `docker run --restart always [image]`               |
| `--network`    | `--network [network]`             | Network        | `docker run --network mynetwork [image]`            |
| `-m`           | `-m [memory]`                     | Memory         | `docker run -m 512m [image]`                        |
| `--cpu-shares` | `--cpu-shares [shares]`           | CPU Shares     | `docker run --cpu-shares 1024 [image]`              |
| `--link`       | `--link [container]:[alias]`      | Link           | `docker run --link mysql:mysql [image]`             |

### Docker Exec

### Docker Ps
