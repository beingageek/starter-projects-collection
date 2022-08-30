package com.starter.camel;

import org.apache.camel.builder.RouteBuilder;
import org.springframework.stereotype.Component;

@Component
public class CamelRoutes extends RouteBuilder {

    @Override
    public void configure() {

        from("timer:foo?period={{myPeriod}}").routeId("timer")
                .log("Hello Timer!");

        from("timer:foo2?period={{myPeriod}}").routeId("timer2")
                .log("Hello Timer2");
    }
}
