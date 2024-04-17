# UserStats

This is an event-driven microservices app with Python, Kafka, Flask and Redis.
The app has a store service where users land and an analyzer service that can see data on the users that visited.
These two services communicate via a Kafka topic. 
After a user visits the store, a Kafka producer sends their browser information to a topic log.
The analyzer service has a Kafka consumer which reads from the topic log and stores the counts of
different browsers seen in a Redis database.
The analyzer service also has an API enpoint that will display a count of all
the browers seen by reading from the database.

## Requirements
Docker Engine and Docker Compose are needed to run this app.
The install docs can be found here https://docs.docker.com/engine/install/ 
and here https://docs.docker.com/compose/install/ .

## Running the app
To start the app, run `docker-compose up` from the root directory of the app.

```bash
user@hostname:~/UserStats$ docker-compose up
```

The services will start up after a short amount of time.
Some services depend on others being in a healthy state which adds to start up time. 

Once everything is up and running, visit the store service at `http://localhost:5000/` from various 
browsers to accumulate user data. For example, FireFox and Chrome can be used.
Also a curl command can be used to make an HTTP request. 

```bash
user@hostname:~$ curl localhost:5000
<p>Welcome to the Store</p>
```

Visit the analyzer service at `http://localhost:5001/` to see the counts of browsers
that have visited the store endpoint. This can be accessed via a browser where JSON 
would be displayed or one can use a curl command.

```bash
user@hostname:~$ curl localhost:5001
{"Firefox/123.0":4,"Safari/537.36":3,"curl/7.81.0":2}
```

To stop the app, press `CTRL+C` in the termnial where docker-compose was run, and
then run `docker-compose down`.

```bash
user@hostname:~/UserStats$ docker-compose down
```