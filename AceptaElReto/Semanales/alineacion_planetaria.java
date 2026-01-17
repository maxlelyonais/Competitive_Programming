package Semanales;
import java.util.Scanner;

public class alineacion_planetaria {



    public static int gcd(int a, int b) {

        
        while(b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }

        return a;
    }

    public static void main(String args[]) {

        Scanner scan = new Scanner(System.in);

        while(true) {

            int nTests = scan.nextInt();

            if (nTests == 0) 
                break;

            int recentNumber = scan.nextInt();
            for (int i = 1; i < nTests; i++) {
                int newNumber = scan.nextInt();
                int gcd_result = gcd(recentNumber, newNumber);
                recentNumber = Math.abs(recentNumber*newNumber/ gcd_result);
            }

            System.out.println(recentNumber);

        }


    }
}
