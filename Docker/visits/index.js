const express = require('express');
const redis = require('redis');

// Testing by adding a way to crash when visiting the root route '/'
const process = require('process')


const app = express();
const client = redis.createClient({
    host: 'redice-server',
    port: 6379
});
client.set('visits', 0);

app.get('/', (req, res) => {

    // Forcing to exit for testing on the docker-compose.yml file
    //https://docs.docker.com/compose/compose-file/compose-file-v3/#restart
    //         restart: "no"
    //         restart: always
    //         restart: on-failure
    //         restart: unless-stopped
    process.exit(0);

    client.get('visits', (err, visits) => {
        res.send('Number of visits is: ' + visits);
        client.set('visits', parseInt(visits) + 1);
    });
});

app.listen(8081, () => {
    console.log('Listening on port 8081');
});