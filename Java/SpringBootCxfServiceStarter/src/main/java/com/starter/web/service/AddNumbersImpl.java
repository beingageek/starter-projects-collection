package com.starter.web.service;

import com.starter.AddNumbersFault;
import com.starter.AddNumbersFault_Exception;
import com.starter.AddNumbersPortType;
import jakarta.jws.WebService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;

@Service
@WebService(
        serviceName = "AddNumbersService",
        portName = "AddNumbersPort",
        targetNamespace = "http://starter.com",
        endpointInterface = "com.starter.AddNumbersPortType"
)
public class AddNumbersImpl implements AddNumbersPortType {

    private static final Logger logger = LoggerFactory.getLogger(AddNumbersImpl.class);

    @Override
    public int addNumbers(int number1, int number2) throws AddNumbersFault_Exception {
        if (number1 < 0 || number2 < 0) {
            String message = "Negative number can't be added!";
            String detail = "Numbers: " + number1 + ", " + number2;
            AddNumbersFault fault = new AddNumbersFault ();
            fault.setMessage (message);
            fault.setFaultInfo (detail);
            throw new AddNumbersFault_Exception (message, fault);
        }
        logger.info("Adding numbers {} and {}", number1, number2);
        return number1 + number2;
    }
}
