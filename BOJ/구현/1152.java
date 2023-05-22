//단어의 개수(백준 1152번)
//
//입력
//The Curious Case of Benjamin Button
//
//출력
//6

import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        System.out.println(st.countTokens());
        br.close();
    }

}
