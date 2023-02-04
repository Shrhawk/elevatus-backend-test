# Elevatus Test

## Features

+ Python FastAPI backend.
+ MongoDB Database.
+ Pydantic Schemas Validation


## Local Development with Docker

Start the dev server for local development:

```shell
cp .env.docker .env
docker-compose up
```


## Local Development without Docker

To use the application, follow the outlined steps:

Clone/Copy the code and create a virtual environment in it:
```shell
python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
```
Install the modules listed in the `requirements.txt` file
```shell
pip install -r requirements.txt
pre-commit install
```
Create a `.env` file in the root directory of the project
```shell
cp .env.dist .env
```
add the following variables to `.env` file according to your environment needs:
```shell
MONGO_DB=elavatus_assignment_db
DATABASE_URL=<database_url>
ACCESS_TOKEN_EXPIRE_MINUTES=<seconds>
JWT_SECRET=<secret_string>
ALGORITHM=<jwt_algorithn=m>
```
Start the application:
```shell
python main.py
```

The server will start listens on port 8080 on address [http://0.0.0.0:8080/docs](http://0.0.0.0:8080/docs).
