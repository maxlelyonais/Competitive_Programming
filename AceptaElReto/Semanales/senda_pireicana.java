package Semanales;
import java.util.Scanner;

public class senda_pireicana {
   
    
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);

        while (true) {
            int nTest = scan.nextInt();
            StringBuilder result = new StringBuilder();
            if (nTest == 0) break;

            int[] runDistances = new int[nTest];
            int total = 0;

            for (int i = 0; i < nTest; i++) {
                int distance = scan.nextInt();
                runDistances[i] = distance;
                total+=distance;
            }

            for (int i = 0; i < nTest; i++) {
                result.append(String.valueOf(total) + " ");
                total-= runDistances[i];
            }

            System.out.println(result.toString().trim());
        }
        
    }
}
