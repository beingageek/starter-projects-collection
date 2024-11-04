package com.starter.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class RestServiceController {

    private static final Logger logger = LoggerFactory.getLogger(RestServiceController.class);
    private static Integer count = 0;

    @GetMapping("/")
    public String home() {
        return "Spring is here!";
    }

    @GetMapping("/unsecured/sayHello")
    public String unsecuredHello(@RequestParam String name) {
        logger.info("Request received for unsecured sayHello: {}", name);
        return "Hello " + name + "!";
    }

    @GetMapping("/secured/sayHello")
    public String secureSayHello(@RequestParam String name) {
        logger.info("Request received for secured Hello sayHello: {}", name);
        return "Hello " + name + "*!";
    }

    @PostMapping("/secured/addCount")
    public int addCount(@RequestParam Integer increment) {
        logger.info("POST Request received for adding count {}", increment);
        count += increment;
        return increment;
    }

    @GetMapping("/unsecured/getCount")
    public Integer getCount() {
        return count;
    }

}
