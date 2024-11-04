# Spring Boot Security Starter

### Description

This project is a starter project for Spring Boot based Security Authorization. 
It uses Jasypt to encrypt passwords, and it uses Spring Security for authentication and authorization.

### Requirements

- Java 17
- Maven

### Usage

1. Clone the repository.
2. Build the project using `mvn clean package`.
3. Run the Java class [JasyptEncryptor.java](src/main/java/com/starter/standalone/JasyptEncryptor.java). You can modify the password and the key for encryption in this file as per your choosing.
   - This is a standalone Java class, but this has to be in sync with the file used in the main Spring Boot application [SpringBootSecurityStarter.java](src/main/java/com/starter/app/SpringBootSecurityStarter.java).
   - Any updates to the encryptor key, algorithm, etc. will need to be updated in both files.
   - You can run JasyptEncryptor.java using `mvn exec:java -D"exec.mainClass"="com.starter.standalone.JasyptEncryptor"`, or you can run inside your IDE.
4. The above class will generate an encrypted password in the console.
5. Update the file [application.properties](src/main/resources/application.properties) with the encrypted password in the `api_user_password` property.
6. Start the application using `mvn spring-boot:run`. Or you can run the main Spring Boot application [SpringBootSecurityStarter.java](src/main/java/com/starter/app/SpringBootSecurityStarter.java) from the IDE.
7. Once the application is started, you can access it using `http://localhost:8080`.
8. There are mainly two sets of API endpoints for testing.
   - Unsecured APIs: `http://localhost:8080/unsecured/hello` and `http://localhost:8080/unsecured/count`.
   - Secured APIs: `http://localhost:8080/secured/hello` and `http://localhost:8080/secured/count`.
9. You can also test the API endpoints using Postman. See [spring-boot-security-poc.postman_collection.json](spring-boot-security-poc.postman_collection.json).

### Dependencies

- Spring Boot
- Jasypt
- Spring Security