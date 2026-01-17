import java.util.Scanner;

public class los_antiguos_grados_celsius {
    

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int nTests = scan.nextInt();

        for (int i = 0; i < nTests; i++) {

            int valueRaw = scan.nextInt();
            int transformedValue = 0;

            if (0 <= valueRaw && valueRaw <= 100) {
                transformedValue = Math.abs(valueRaw - 100);
            } else if (valueRaw > 100) {

                transformedValue = -(valueRaw-100);
            } else if( valueRaw < 0) {

                transformedValue = (-valueRaw) + 100;

            }

            System.out.println(transformedValue);
        }
    }
}
