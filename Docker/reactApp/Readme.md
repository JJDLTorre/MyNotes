## To build the node frontend project
```
$ npx create-react-app frontend
```

## To build docker 
```
cd frontend
docker build -f Dockerfile.dev .
```
Note: The node_module directory was deleted to speed up the process. 

## Start the docker app
```
docker run -it -p 3000:3000 <IMAGE_ID>
```

## Run app with volume mapping to the host
```
docker run -p 3000:3000 -v /app/node_modules -v $(pwd):/app <IMAGE_ID>
```
The "-v /app/node_modules " ignores that dir and use the one in the container. 

## Start using docker-compose
```
docker-compose up
```