package com.starter.service;

import java.time.LocalDate;

public class DateServiceUtility {

	public static String getToday() {
		return LocalDate.now().toString();
	}

}
