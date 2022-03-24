package com.starter.model;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class UserData {
	
	private String username;
	private String userFirstName;
	private String userLastName;
	private int age;
	
	public String toString() {
		return String.format("%s, %s %s, %d", this.getUsername(), this.getUserFirstName(), this.getUserLastName(), this.getAge());
	}

	public UserData() {

	}

	public UserData(String username, String userFirstName, String userLastName, int age) {
		this.username = username;
		this.userFirstName = userFirstName;
		this.userLastName = userLastName;
		this.age = age;
	}

}
