package com.starter;

import com.starter.service.StarterUtility;
import io.vavr.control.Try;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.util.function.Supplier;

public class StarterUtilityTest {

    @Test
    public void testUtility() {
        StarterUtility su = new StarterUtility();
        Assertions.assertEquals(10, su.getSum(1, 9));

        Assertions.assertEquals(11, su.getConcatenatedNumber(1, 1));
    }
    
    @Test
    public void testTryMonad() {
        String defaultResponse = "default";
        Supplier<Integer> clientAction = () -> 100;

        Try<Integer> response = Try.ofSupplier(clientAction);
        String result = response.map(Object::toString).getOrElse(defaultResponse);

        Assertions.assertTrue(response.isSuccess());
        response.onSuccess(r -> Assertions.assertEquals(100, (int) r));
        Assertions.assertEquals("100", result);
    }
}
