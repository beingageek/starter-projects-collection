# Docker Guide for setting up MySQL Database

Create a new container using the MySQL image in Docker.
```
docker run -d --name mysql_demo -e MYSQL_ROOT_PASSWORD=mySqlAdmin1 -p 3307:3306 mysql
```

Log into bash shell in the same container
```
docker exec -it mysql_demo bash
```

Log in using root user to the MySQL instance.
```
mysql -u root -p
```

Create a DB and 2 tables
```
CREATE DATABASE `user_info` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

DROP TABLE IF EXISTS user_info.user_account;
CREATE TABLE user_info.user_account (
	user_id INT auto_increment NOT NULL,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	middle_initial varchar(1) NULL,
	age INT NOT NULL,
	CONSTRAINT user_account_PK PRIMARY KEY (user_id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS user_info.user_address;
CREATE TABLE user_info.user_address (
	user_id INT NOT NULL,
	address_type VARCHAR(10) NOT NULL,
	address_line1 varchar(200) NOT NULL,
	address_line2 varchar(100) NULL,
	city varchar(50) NOT NULL,
	state varchar(50) NOT NULL,
	zip_code varchar(10) NOT NULL,
	CONSTRAINT user_address_user_account_FK FOREIGN KEY (user_id) REFERENCES user_info.user_account(user_id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;
```

Create a new user and grant permissions
```
CREATE USER 'mysql_user'@'172.17.0.1' IDENTIFIED BY 'passWord1';

GRANT SELECT, INSERT, UPDATE ON user_info.user_account TO 'mysql_user'@'172.17.0.1'; 

GRANT SELECT, INSERT, UPDATE ON user_info.user_address TO 'mysql_user'@'172.17.0.1'; 

FLUSH PRIVILEGES;
```

Insert test records into the tables
```
insert into user_info.user_account (first_name, last_name, age) values ('Jery', 'Ryan', 29);

insert into user_info.user_address (user_id, address_type , address_line1, city, state, zip_code)
values (1, 'Home', '100 STEWART ST APT B', 'Remlin', 'Salem', 10001);
```

Verify that the records are showing correctly
```
select * from user_info.user_account ua inner join user_info.user_address a where ua.user_id = a.user_id;
```
