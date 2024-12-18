package com.starter.app;

import org.jasypt.encryption.StringEncryptor;
import org.jasypt.encryption.pbe.PooledPBEStringEncryptor;
import org.jasypt.encryption.pbe.config.SimpleStringPBEConfig;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication
@ComponentScan("com.starter")
public class SpringBootSecurityStarter {

    public static void main(String[] args) {
        SpringApplication.run(SpringBootSecurityStarter.class, args);
    }

    @Bean("customEncryptor")
    public StringEncryptor stringEncryptor() {
        SimpleStringPBEConfig config = new SimpleStringPBEConfig();
        config.setPassword("coolEncryptorPassword");
        config.setAlgorithm("PBEWithMD5AndDES");
        config.setProviderName("SunJCE");
        config.setKeyObtentionIterations(128);
        config.setPoolSize(1);
        config.setSaltGeneratorClassName("org.jasypt.salt.RandomSaltGenerator");
        PooledPBEStringEncryptor encryptor = new PooledPBEStringEncryptor();
        encryptor.setConfig(config);
        return encryptor;
    }

}
