# Docker Guide for setting up PostGres Database

Create a new container using the PostGres image in Docker.
```
docker run -d -p 5432:5432 --name postgres_demo -e POSTGRES_PASSWORD=postgreSqlAdmin1 postgres
```

Log into bash shell in the same container
```
docker exec -it postgres_demo bash
```

Log in using root user to the MySQL instance.
```
psql -U postgres
```

Create a user and a DB
```
CREATE USER postgres_user PASSWORD 'passWord1' SUPERUSER;

CREATE DATABASE finance_db OWNER postgres_user;
```

Connect to the user account
```
\c finance_db postgres_user
```

Create a new table
```
CREATE TABLE user_finance (user_id serial PRIMARY KEY, year int, month int, starting_balance float, ending_balance float);
```

Insert test records into the tables
```
INSERT INTO public.user_finance
(user_id, "year", "month", starting_balance, ending_balance)
VALUES(nextval('user_finance_user_id_seq'::regclass), 2025, 1, 500, 1000);
```

Verify that the records are showing correctly
```
select * from public.user_finance uf 
```
