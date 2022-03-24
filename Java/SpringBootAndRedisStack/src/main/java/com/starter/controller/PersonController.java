package com.starter.controller;

import com.starter.domain.Person;
import com.starter.repositories.PersonRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/api/persons")
public class PersonController {

    @Autowired
    PersonRepository personRepository;

    @GetMapping("/all")
    Page<Person> all(Pageable pageable) {
        return personRepository.findAll(pageable);
    }

    @GetMapping("/name/{first}")
    List<Person> byFirstName(@PathVariable("first") String firstName) {
        return personRepository.findByFirstName(firstName);
    }

    @GetMapping("/ageBetween/{age1}/{age2}")
    List<Person> byAgeBetween(@PathVariable("age1") int age1, @PathVariable("age2") int age2) {
        return personRepository.findByAgeBetween(age1, age2);
    }
}
