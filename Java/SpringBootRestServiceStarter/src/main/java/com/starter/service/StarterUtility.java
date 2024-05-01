package com.starter.service;

import com.google.common.annotations.VisibleForTesting;

public class StarterUtility {

    public int getSum(int a, int b) {
        return a + b;
    }

    @VisibleForTesting
    public int getConcatenatedNumber(int a, int b) {
        return Integer.parseInt(a + "" + b);
    }
}
