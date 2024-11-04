package com.starter.standalone;

import org.jasypt.encryption.pbe.PooledPBEStringEncryptor;
import org.jasypt.encryption.pbe.config.SimpleStringPBEConfig;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * Simple setup for Jasypt PBE encryption.
 * <p/>
 * This class demonstrates how to use the Jasypt library to encrypt
 * a password using a pooled PBE string encryptor. The password is
 * "coolPassword1", and the encryption key is "coolEncryptorPassword".
 */
public class JasyptEncryptor {

    private static final Logger logger = LoggerFactory.getLogger(JasyptEncryptor.class);

    public static void main(String[] args) {
        logger.info("Running Jasypt Encryptor!");
        SimpleStringPBEConfig config = new SimpleStringPBEConfig();
        config.setPassword("coolEncryptorPassword");
        config.setAlgorithm("PBEWithMD5AndDES");
        config.setProviderName("SunJCE");
        config.setKeyObtentionIterations(128);
        config.setPoolSize(1);
        config.setSaltGeneratorClassName("org.jasypt.salt.RandomSaltGenerator");
        PooledPBEStringEncryptor encryptor = new PooledPBEStringEncryptor();
        encryptor.setConfig(config);
        logger.info("Encrypted password: {}", encryptor.encrypt("coolPassword1"));
    }
}
