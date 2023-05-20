package com.starter;

import jakarta.xml.ws.BindingProvider;

public class EclipseMetroJaxwsClientApp {

    public static void main(String[] args) {
        System.out.println("Hello World!");
        try {
            AddNumbersService testService = new AddNumbersService();
            AddNumbersPortType testPort = testService.getAddNumbersPort();
            BindingProvider binding = (BindingProvider) testPort;
            binding.getRequestContext().put(BindingProvider.ENDPOINT_ADDRESS_PROPERTY, "http://localhost:8080/cxf/AddNumbersService");
            int sum = testPort.addNumbers(1, 2);
            System.out.println("Sum of two numbers = " + sum);
        } catch (Exception e) {
            System.out.println("Web service call failed.");
            e.printStackTrace();
        }
    }
}
