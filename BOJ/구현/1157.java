/**
 * 단어공부(백준 1157번)
 *
 * 입력
 * Mississipi
 * 출력
 * ?  // 가장 많이 사용된 알파벳이 여러 개 존재할 경우 ? 출력
 * 입력
 * zZa
 * 출력
 * Z // 대문자
 */

import java.io.*;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringBuilder sb = new StringBuilder(br.readLine());
        HashMap<Character, Integer> hash = new HashMap<>();
        for (int i=0; i<sb.length(); i++) {
            char ch = sb.charAt(i);
            char upperCh = Character.toUpperCase(ch);
            if (hash.containsKey(upperCh)) {
                hash.put(upperCh, hash.get(upperCh) + 1);
            } else {
                hash.put(upperCh, 1);
            }
        }
        char maxChar = ' ';
        int maxCount = 0;
        for (Map.Entry<Character, Integer> entry: hash.entrySet()) {
            char key = entry.getKey();
            int value = entry.getValue();
            
            if (value == maxCount) {
                maxChar = '?';
            }
            else if (value > maxCount) {
                maxCount = value;
                maxChar = key;
            } 
        }
        System.out.println(maxChar);
    }
}
