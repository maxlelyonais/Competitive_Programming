import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class laberinto_diafano {


    public static void main(String args[]) {

        Scanner scan = new Scanner(System.in);

        while(true) {

            int tx = scan.nextInt();
            int ty = scan.nextInt();
            if (tx == 0 && ty == 0) {
                break;
            }
            boolean separation = (tx % 2 == 0 && ty % 2 == 0) ? true : false;
            int total = 0;

            if (separation) {
                List<Integer> toTest = new ArrayList<>();

                for(int i = 0; i < ty; i++) {
                    for (int j = 0; j < tx; j++) {
                        int number = scan.nextInt();

                       if ((i+j) % 2 != 0) {
                        toTest.add(number);
                       }
                       total+=number;
                    }
                }

                int auxiliarTotal = total - toTest.get(0);
                for (int smallestSubstraction: toTest) {
                    auxiliarTotal = Math.max(auxiliarTotal, total - smallestSubstraction);
                }
                total = auxiliarTotal;
            } else {
                for(int i = 0; i < ty; i++) {
                    for (int j = 0; j < tx; j++) {
                        total+= scan.nextInt();
                    }
                }
            }

            System.out.println(total);
        }

    }

}
