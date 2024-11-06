package com.lgcns.mission.book;

import java.text.NumberFormat;
import java.util.Locale;

public class MissionUtil {
    public static String moneyFormat(double amount) {
        NumberFormat formatter = NumberFormat.getCurrencyInstance(Locale.getDefault());
        return formatter.format(amount);
    }
}
