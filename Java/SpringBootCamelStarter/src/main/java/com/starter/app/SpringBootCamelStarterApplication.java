package com.starter.app;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@ComponentScan("com.starter")
@RestController
public class SpringBootCamelStarterApplication {

	public static void main(String[] args) {
		SpringApplication.run(SpringBootCamelStarterApplication.class, args);
	}

	@GetMapping("/")
	public String home() {
		return "Spring is here!";
	}

}
