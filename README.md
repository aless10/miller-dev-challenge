## Miller Developer Challenge

### How to run

Run 

````shell
docker compose up -d --build
````

This command should get the application up and running.

Then you can visit ```http://localhost``` and you should see the login page.

### Useful routes

- http://localhost is the frontend application
- http://localhost/login 
- http://localhost/signup to create a new user 
- http://localhost/docs you can see the api UI
- http://localhost/redoc you can see the api UI (but nicer)


### Data

The database should be prepopulated, so you can log into the application with these users:

- alessio
- federico
- william

The password is ```password```.


### Architecture

The application runs in 3 docker container:

- `server`: this is a fastapi backend where we handle the api and the database interaction. This is also where the auth logic is implemented
- `db`: we use a postgres db to store the data. The credentials are username=`admin`,password=`P455w0rd`
- `web_server`: this is a react app served behind nginx

There is also another container ```pg-admin``` that runs at ``localhost:5556`` that helps you if you need to connect to the database. The credentials are user=`admin@miller.com` and password=`password`


### TODO

Here is a list of todos:

- remove hardcoded things: there are some things that could be moved to env variables (the backend request url for example)
- add more tests on the backend
- add routes on the frontend to handle add cars and requests

