package com.starter.client;

import com.starter.AddNumbersPortType;
import org.apache.cxf.jaxws.JaxWsProxyFactoryBean;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class SpringBootCxtClient {

    private static final Logger logger = LoggerFactory.getLogger(SpringBootCxtClient.class);

    private static volatile AddNumbersPortType addNumbersService;

    public static void main(String[] args) {
        logger.info("Running SpringBootCxtClient...");
        initService();
        try {
            logger.info("addNumbers(1, 2) = {}", addNumbersService.addNumbers(1, 2));
            logger.info("addNumbers(10, 2) = {}", addNumbersService.addNumbers(10, 2));
        }
        catch (Exception e) {
            logger.error("Error", e);
        }
    }

    private static void initService() {
        if (addNumbersService == null) {
            synchronized (SpringBootCxtClient.class) {
                if (addNumbersService == null) {
                    JaxWsProxyFactoryBean factoryBean = new JaxWsProxyFactoryBean();
                    factoryBean.setServiceClass(AddNumbersPortType.class);
                    factoryBean.setAddress("http://localhost:8080/cxf/addNumbers");

                    // Setting WSDL URL may not be necessary, but can be set like this if necessary
                    // factoryBean.setWsdlURL("http://localhost:8080/cxf/addNumbers?wsdl");

                    // Create the service
                    addNumbersService = (AddNumbersPortType) factoryBean.create();
                    logger.info("Service created");
                }
            }
        }
    }
}
