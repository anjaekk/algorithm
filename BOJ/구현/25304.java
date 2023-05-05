import java.util.Scanner;

public class Main {
    public static void main(String[] ars) {
        Scanner sc = new Scanner(System.in);

        int total = sc.nextInt();
        int n = sc.nextInt();
        int sum = 0;

        for(int i=0; i < n; i++){
            int p = sc.nextInt();
            int q = sc.nextInt();
            sum += p * q;
        }
        if(total == sum){
            System.out.println("Yes");
        }
        else{
            System.out.println("No");
        }
    }
}
