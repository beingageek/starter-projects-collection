package com.starter;

import com.starter.service.DateServiceUtility;
import io.micronaut.runtime.EmbeddedApplication;
import io.micronaut.test.extensions.junit5.annotation.MicronautTest;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import javax.inject.Inject;
import java.time.LocalDate;

@MicronautTest
public class MicronautStarterTest {

    @Inject
    EmbeddedApplication<?> application;

    @Test
    void testItWorks() {
        Assertions.assertTrue(application.isRunning());
        Assertions.assertEquals(LocalDate.now().toString(), DateServiceUtility.getToday());
    }

}
