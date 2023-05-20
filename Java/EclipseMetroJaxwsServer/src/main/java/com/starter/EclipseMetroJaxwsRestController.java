package com.starter;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class EclipseMetroJaxwsRestController {

    @GetMapping("/")
    public static String home() {
        return "Spring Boot is here";
    }
}
