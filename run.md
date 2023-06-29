# Steps to run the application via docker

## Build the image of our scrapper application by using the below command

docker build -t my-app-image .

## Create and run the PostgreSQL container using the official PostgreSQL image from Docker Hub

docker run --name my-postgres-container -e POSTGRES_PASSWORD=admin -p 5432:5432 -d postgres

## Check if the database 'dependencies' exists in the PostgreSQL container

docker exec -it my-postgres-container psql -U postgres -c '\l'

## If the database is not present, create it using the following steps

docker exec -it my-postgres-container bash
psql -h 172.17.0.2 -p 5432 -U postgres
CREATE DATABASE dependencies;

# to connect to the database

\c dependencies

## Verify if the database has been created using the '\l' command in the PostgreSQL shell

## Run the scrapper application container and link it to the PostgreSQL container

docker run --name my-app-container --link my-postgres-container -d python-scrapper

## Check the logs of the application container for the results

docker logs my-app-container

## If you encounter a connection error with 'localhost', change the host in your application to the address of the PostgreSQL container

docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' my-postgres-container

## If you encounter a port error, kill all the applications working on port 5432

sudo lsof -i :5432

# Get the PID and kill the process

kill pid
