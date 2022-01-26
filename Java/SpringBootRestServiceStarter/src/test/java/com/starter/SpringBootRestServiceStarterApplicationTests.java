package com.starter;

import com.starter.app.SpringBootRestServiceStarterApplication;
import com.starter.service.StarterServiceController;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest(classes = SpringBootRestServiceStarterApplication.class)
class SpringBootRestServiceStarterApplicationTests {
	
	private static Logger logger = LoggerFactory.getLogger(SpringBootRestServiceStarterApplicationTests.class);

	@Autowired
	StarterServiceController controller;

	@Test
	public void contextLoads() {
		Assertions.assertNotNull(controller);
	}

}
