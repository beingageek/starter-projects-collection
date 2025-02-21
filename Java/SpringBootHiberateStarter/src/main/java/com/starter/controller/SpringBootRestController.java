package com.starter.controller;

import com.starter.repository.dao.finance.UserFinanceRepository;
import com.starter.repository.dao.user.UserAccountRepository;
import com.starter.repository.model.finance.UserFinance;
import com.starter.repository.model.user.UserAccount;
import com.starter.view.ApiResponse;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class SpringBootRestController {

    private static final Logger logger = LoggerFactory.getLogger(SpringBootRestController.class);

    @Autowired
    UserAccountRepository userAccountRepository;

    @Autowired
    UserFinanceRepository userFinanceRepository;

    @GetMapping("/api/get_users")
    public List<UserAccount> getUsers() {
        return userAccountRepository.findAll();
    }

    @GetMapping("/api/get_finances")
    public List<UserFinance> getFinances() {
        return userFinanceRepository.findAll();
    }

    @GetMapping("/api/get_user")
    public UserAccount getUser(@RequestParam Integer userId) {
        logger.info("Finding user information for userId = {}", userId);
        return userAccountRepository.findUserAccount(userId);
    }

    @GetMapping("api/get_user_and_address")
    public ApiResponse getUserAndAddress(@RequestParam Integer userId) {
        logger.info("Finding user information with addresses for userId = {}", userId);
        UserAccount userAccount = userAccountRepository.findUserAccount(userId);
        if (null != userAccount) {
            ApiResponse response = new ApiResponse();
            response.setUserAccount(userAccount);
            response.setUserAddresses(userAccountRepository.findUserAddresses(userId));
            logger.info("Retrieved UserAndAddress:{}", response);
            return response;
        }
        return null;
    }

    @GetMapping("api/get_user_and_finance")
    public ApiResponse getUserAndFinanceInformation(@RequestParam Integer userId) {
        ApiResponse response = getUserAndAddress(userId);
        if (null != response && null != response.getUserAccount()) {
            response.setUserFinances(userFinanceRepository.findUserFinancesByUserId(userId));
        }
        logger.info("Retrieved UserAndFinanceInformation:{}", response);
        return response;
    }
}
