package com.starter;

import org.apache.cxf.Bus;
import org.apache.cxf.bus.spring.SpringBus;
import org.apache.cxf.ext.logging.LoggingFeature;
import org.apache.cxf.jaxws.EndpointImpl;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import javax.xml.ws.Endpoint;

@Configuration
public class EclipseMetroJaxwsWsConfig {

    @Bean(name = Bus.DEFAULT_BUS_ID)
    public SpringBus springBus(LoggingFeature loggingFeature) {
        SpringBus cxfBus = new SpringBus();
        cxfBus.getFeatures().add(loggingFeature);
        return cxfBus;
    }

    @Bean
    public LoggingFeature loggingFeature() {
        LoggingFeature loggingFeature = new LoggingFeature();
        loggingFeature.setPrettyLogging(true);
        return loggingFeature;
    }

    @Bean
    public Endpoint endpoint(Bus bus, AddNumbersImpl addNumbersImpl) {
        EndpointImpl endpoint = new EndpointImpl(bus, addNumbersImpl);
        endpoint.publish("/AddNumbersService");
        return endpoint;
    }

}
