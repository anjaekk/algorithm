/**
 * 피보나치 수(백준 2747번)
 *
 * 입력
 * 10
 * 출력
 * 55
 */

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        List<Integer> fibo = new ArrayList<>();
        for (int i=0; i<n+1; i++) {
            if (i < 2) {
                fibo.add(i);
            } else {
                int num = fibo.get(i-2) + fibo.get(i-1);
                fibo.add(num);
            }
        }
        System.out.println(fibo.get(fibo.size() - 1));
    }
}
