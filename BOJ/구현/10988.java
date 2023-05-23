/**
팰린드롬인지 확인하기(백준 10988번)

 입력
 level

 출력
 1
**/

import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder(br.readLine());

        int result = ((sb.toString().equals(sb.reverse().toString())) ? 1:0);
        System.out.println(result);
    }
}
