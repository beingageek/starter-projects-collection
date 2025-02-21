package com.starter.view;

import com.starter.repository.model.user.UserAccount;
import com.starter.repository.model.user.UserAddress;
import com.starter.repository.model.finance.UserFinance;

import java.util.List;

public class ApiResponse {

    private UserAccount userAccount;
    private List<UserAddress> userAddresses;
    private List<UserFinance> userFinances;

    public UserAccount getUserAccount() {
        return userAccount;
    }

    public void setUserAccount(UserAccount userAccount) {
        this.userAccount = userAccount;
    }

    public List<UserAddress> getUserAddresses() {
        return userAddresses;
    }

    public void setUserAddresses(List<UserAddress> userAddresses) {
        this.userAddresses = userAddresses;
    }

    public List<UserFinance> getUserFinances() {
        return userFinances;
    }

    public void setUserFinances(List<UserFinance> userFinances) {
        this.userFinances = userFinances;
    }

    @Override
    public String toString() {
        StringBuilder builder = new StringBuilder();
        builder.append("ApiResponse{" + "userAccount=").append(userAccount.toString());
        if (null != userAddresses && !userAddresses.isEmpty()) {
            builder.append(", userAddresses=").append(userAddresses);
        }
        if (null != userFinances && !userFinances.isEmpty()) {
            builder.append(", userFinances=").append(userFinances);
        }
        builder.append("}");
        return builder.toString();
    }
}
