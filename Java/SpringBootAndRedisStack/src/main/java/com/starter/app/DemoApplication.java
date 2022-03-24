package com.starter.app;

import com.redis.om.spring.annotations.EnableRedisDocumentRepositories;
import com.starter.domain.Person;
import com.starter.repositories.PersonRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication
@ComponentScan("com.starter")
@EnableRedisDocumentRepositories(basePackages = "com.starter")
public class DemoApplication {

	@Autowired
	PersonRepository personRepository;

	@Bean
	CommandLineRunner loadTestData() {
		return args -> {
			// Clean all existing records
			personRepository.deleteAll();
			// Add new records
			personRepository.save(Person.of("Brian", "O'Conner", 44));
			personRepository.save(Person.of("Dominic", "Toretto", 45));

			// Verify data was added
			personRepository.findAll().forEach(p -> System.out.println(p.getFirstName() + "-" + p.getAge()));
			personRepository.findByFirstName("Brian").forEach(System.out::println);
			personRepository.findByAgeBetween(30, 50).forEach(System.out::println);
		};
	}

	public static void main(String[] args) {
		SpringApplication.run(DemoApplication.class, args);
	}

}
