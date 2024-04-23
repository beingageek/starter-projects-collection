package com.starter.app;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication
@ComponentScan("com.starter")
public class SpringBootSecurityStarter {

    public static void main(String[] args) {
        SpringApplication.run(SpringBootSecurityStarter.class, args);
    }

}
