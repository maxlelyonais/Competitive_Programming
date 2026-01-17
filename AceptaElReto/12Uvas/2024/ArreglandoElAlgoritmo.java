import java.util.Scanner;

public class ArreglandoElAlgoritmo {

    public static void main(String args[]) {

        Scanner scan = new Scanner(System.in);

        while(scan.hasNextLine()) {

            int index = 0;
            long highestValue = Long.MIN_VALUE;

            int nElements = scan.nextInt();
            if (nElements == 0) break;

            for (int i = 0; i < nElements; i++) {
                long element = scan.nextLong();

                if (element < highestValue) {
                    index = i+1;
                } else {
                    highestValue = element;
                }
            }
            System.out.println(nElements - index);
        }
    }
}
