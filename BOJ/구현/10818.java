//최소, 최대(백준 10818번)

import java.io.*;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int first = Integer.parseInt(st.nextToken());

        int min = first;
        int max = first;

        for(int i=0; i<n-1; i++) {
            int num = Integer.parseInt(st.nextToken());
            if(num>max) {
                max = num;
            }
            if(num<min) {
                min = num;
            }
        }
        bw.write(min + " " + max);
        bw.close();

    }
}
