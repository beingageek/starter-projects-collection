package com.starter.repository.dao.user;

import com.starter.repository.model.user.UserAccount;
import com.starter.repository.model.user.UserAddress;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface UserAccountRepository extends JpaRepository<UserAccount, Integer> {

    @Query("select a from UserAccount a where a.userId = :userId")
    UserAccount findUserAccount(Integer userId);

    @Query("select a from UserAddress a where a.userId = :userId")
    List<UserAddress> findUserAddresses(Integer userId);
}
