package com.starter.repository.dao.finance;

import com.starter.repository.model.finance.UserFinance;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface UserFinanceRepository extends JpaRepository<UserFinance, Integer> {

    @Query("select f from UserFinance f where f.userId = :userId")
    List<UserFinance> findUserFinancesByUserId(Integer userId);
}
