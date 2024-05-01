package com.starter.web.service;

import org.apache.cxf.Bus;
import org.apache.cxf.bus.spring.SpringBus;
import org.apache.cxf.ext.logging.LoggingFeature;
import org.apache.cxf.jaxws.EndpointImpl;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class AddNumbersWsConfig {

    @Bean(name = Bus.DEFAULT_BUS_ID)
    public SpringBus springBus(LoggingFeature loggingFeature) {
        SpringBus springBus = new SpringBus();
        springBus.getFeatures().add(loggingFeature);
        return springBus;
    }

    @Bean
    public LoggingFeature loggingFeature() {
        LoggingFeature loggingFeature = new LoggingFeature();
        loggingFeature.setPrettyLogging(true);
        return loggingFeature;
    }

    // Define service endpoint for CXF service
    @Bean
    public EndpointImpl endpoint(Bus bus, AddNumbersImpl addNumbers) {
        EndpointImpl endpoint = new EndpointImpl(bus, addNumbers);
        endpoint.publish("/addNumbers");
        return endpoint;
    }
}
