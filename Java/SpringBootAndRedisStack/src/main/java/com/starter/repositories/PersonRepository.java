package com.starter.repositories;

import com.redis.om.spring.repository.RedisDocumentRepository;
import com.starter.domain.Person;

import java.util.List;

public interface PersonRepository extends RedisDocumentRepository<Person, String> {

    List<Person> findByFirstName(String firstName);
    List<Person> findByAgeBetween(int age, int age2);
}
