package com.starter.repository.model.finance;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name = "user_finance")
public class UserFinance {

    @Id
    @Column(name = "user_id")
    private Integer userId;
    @Column(name = "year")
    private Integer year;
    @Column(name = "month")
    private Integer month;
    @Column(name = "starting_balance")
    private Long startingBalance;
    @Column(name = "ending_balance")
    private Long endingBalance;

    public Integer getUserId() {
        return userId;
    }

    public void setUserId(Integer userId) {
        this.userId = userId;
    }

    public Integer getYear() {
        return year;
    }

    public void setYear(Integer year) {
        this.year = year;
    }

    public Integer getMonth() {
        return month;
    }

    public void setMonth(Integer month) {
        this.month = month;
    }

    public Long getStartingBalance() {
        return startingBalance;
    }

    public void setStartingBalance(Long startingBalance) {
        this.startingBalance = startingBalance;
    }

    public Long getEndingBalance() {
        return endingBalance;
    }

    public void setEndingBalance(Long endingBalance) {
        this.endingBalance = endingBalance;
    }

    @Override
    public String toString() {
        return "UserFinance{" +
                "userId=" + userId +
                ", year=" + year +
                ", month=" + month +
                ", startingBalance=" + startingBalance +
                ", endingBalance=" + endingBalance +
                '}';
    }
}
