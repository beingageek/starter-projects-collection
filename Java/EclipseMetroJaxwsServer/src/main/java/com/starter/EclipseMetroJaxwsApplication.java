package com.starter;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication
@EnableAutoConfiguration
@ComponentScan("com.starter")
public class EclipseMetroJaxwsApplication {

    public static void main(String[] args) {
        SpringApplication.run(EclipseMetroJaxwsApplication.class, args);
    }

}
