import java.util.Scanner;

public class dibujando_triangulares {
    public static void main(String args[]) {


        Scanner scan = new Scanner(System.in);

        int ntests = scan.nextInt();

        for (int i = 0; i < ntests; i++) {

            int initial = 1;
            int totalCounter = 0;
            int desiredLayer = scan.nextInt();

            for (int start = 1; start < desiredLayer; start++) {
                initial+=start;
            }

            int end = initial + (desiredLayer-1);

            for (int start = initial; start <= end; start++) {
                totalCounter += String.valueOf(start).length();
            }
            totalCounter+=(desiredLayer-1);
            System.out.println(totalCounter);
        }


    }

}
