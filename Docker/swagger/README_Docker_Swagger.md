# Installing Swagger from course 

## Get Editor and UI code
```
https://github.com/swagger-api

https://github.com/swagger-api/swagger-ui/releases
https://github.com/swagger-api/swagger-editor/releases

```

## Install NodeJS
```
https://nodejs.org/en/download/
```

```
This package has installed:
	•	Node.js v12.18.4 to /usr/local/bin/node
	•	npm v6.14.6 to /usr/local/bin/npm
Make sure that /usr/local/bin is in your $PATH.
```

### Install the Webserver 
```
$ sudo npm install -g http-server

```

### Stand up the Web Servers

```
http-server swagger-editor -a 127.0.0.1 -p 8080 
```
http://localhost:8080/

```
jdelat04@ITS-JDELAT04-1 ~/src/MyNotes/Docker/swagger/downloads [2020-09-17 10:04:34]
$ http-server swagger-ui -a 127.0.0.1 -p 8081
```
http://localhost:8081/dist/


## Get OpenAPI-Specification 

```
https://github.com/OAI/OpenAPI-Specification
https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.3.md
```

## Copying the API-docs to the working directory

```
jdelat04@ITS-JDELAT04-1 ~/src/MyNotes/Docker/swagger [2020-09-17 13:56:49]
$ cp -r downloads/swagger-ui/dist .

jdelat04@ITS-JDELAT04-1 ~/src/MyNotes/Docker/swagger [2020-09-17 13:56:33]
$ mv dist api-docs
```

## Change where the API points to

```
jdelat04@ITS-JDELAT04-1 ~/src/MyNotes/Docker/swagger [2020-09-17 14:01:14]
$ code api-docs/index.html 
```

Change to point to our api
```
      const ui = SwaggerUIBundle({
        url: "https://petstore.swagger.io/v2/swagger.json",
```
to
```
      const ui = SwaggerUIBundle({
        url: "hsports-api.yaml",
```
### Start the server
```
jdelat04@ITS-JDELAT04-1 ~/src/MyNotes/Docker/swagger [2020-09-17 14:04:37]
$ http-server api-docs -a 127.0.0.1 -p 8081 
```
http://localhost:8081/



# Using Docker
## Get docker
```
docker pull swaggerapi/swagger-ui
docker run -p 8081:8080 swaggerapi/swagger-ui

```

Go to swagger using the browser
```
```

