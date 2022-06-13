package com.starter.controller;

import com.starter.service.DateServiceUtility;
import io.micronaut.http.MediaType;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Get;
import io.micronaut.http.annotation.Produces;

@Controller("/services")
public class DateServiceController {

    @Get("/getDate/today")
    @Produces(MediaType.TEXT_PLAIN)
    public String getToday() {
        return DateServiceUtility.getToday();
    }
}
