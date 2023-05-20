/*
 * Copyright (c) 1997, 2020 Oracle and/or its affiliates. All rights reserved.
 *
 * This program and the accompanying materials are made available under the
 * terms of the Eclipse Distribution License v. 1.0, which is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 *
 * SPDX-License-Identifier: BSD-3-Clause
 */

package com.starter;

import org.springframework.stereotype.Service;

import javax.jws.WebService;

/*
 * Normally the web service implementation class would implement the endpointInterface class.
 * However, it is not necessary as this sample demonstrates.  It is to implement the
 * endpointInterface as the compiler will catch errors in the methods signatures of the
 * implementation class.
 */
@Service
@WebService(endpointInterface="com.starter.AddNumbersPortType", portName = "AddNumbersPortType", serviceName = "AddNumbersService")
public class AddNumbersImpl implements AddNumbersPortType {

    /**
     * @param number1 First number
     * @param number2 Second number
     * @return The sum
     * @throws AddNumbersFault_Exception
     *             if any of the numbers to be added is negative.
     */
    @Override
    public int addNumbers (int number1, int number2)
            throws AddNumbersFault_Exception {
        if (number1 < 0 || number2 < 0) {
            String message = "Negative number cant be added!";
            String detail = "Numbers: " + number1 + ", " + number2;
            AddNumbersFault fault = new AddNumbersFault ();
            fault.setMessage (message);
            fault.setFaultInfo (detail);
            throw new AddNumbersFault_Exception (message, fault);
        }
        return number1 + number2;
    }

    /*
     * Simple one-way method that takes an integer.
     */
    @Override
    public void oneWayInt(int number) {
        System.out.println("Service received: " + number);
    }

}