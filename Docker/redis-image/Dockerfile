# Use an existing docker images as a base
FROM alpine

# Download and install a dependency
RUN apk add --update redis

# Tell the image what to do when it starts
# as a container
CMD [ "redis-server" ]


# jdelat04@ITS-JDELAT04-1 ~/src/MyNotes/Docker/redis-image [2021-06-16 17:28:24]
# $ docker build . 
# [+] Building 2.2s (6/6) FINISHED                                         
#  => [internal] load build definition from Dockerfile                0.0s
#  => => transferring dockerfile: 246B                                0.0s
#  => [internal] load .dockerignore                                   0.0s
#  => => transferring context: 2B                                     0.0s
#  => [internal] load metadata for docker.io/library/alpine:latest    0.0s
#  => [1/2] FROM docker.io/library/alpine                             0.0s
#  => [2/2] RUN apk add --update redis                                1.9s
#  => exporting to image                                              0.1s 
#  => => exporting layers                                             0.1s 
#  => => writing image sha256:4b16375d21806d6b0e9cdbe3235e3bcefcfc3c  0.0s 

