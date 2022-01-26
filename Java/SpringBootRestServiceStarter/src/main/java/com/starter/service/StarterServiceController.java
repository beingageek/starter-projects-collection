package com.starter.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.starter.model.UserData;

import java.util.Arrays;
import java.util.List;

@RestController
public class StarterServiceController {
	
	private static Logger logger = LoggerFactory.getLogger(StarterServiceController.class);
	
	@GetMapping("/")
	public String home() {
		return "Spring is here!";
	}
	
	@GetMapping("/sayHello")
	public String sayHello(@RequestParam String name) {
		return "Hello " + name + "!";
	}
	
	@PostMapping("/addUser")
	public String addUser(@RequestBody UserData user) {
		logger.info("Requester User Data: " + user.toString());
		return "User " + user.getUsername() + " Added!";
	}

	@GetMapping("/getUsers")
	public List<UserData> getUsers() {
		logger.info("Getting users");
		UserData adam = new UserData("adam01", "ADAM", "", 30);
		UserData eve = new UserData("eve01", "EVE", "", 30);
		UserData[] userArr = {adam, eve};
		return Arrays.asList(userArr);
	}

}
