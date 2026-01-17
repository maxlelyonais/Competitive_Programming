import java.util.HashMap;
import java.util.Scanner;

public class triple_y_quintuple_repeticion {
    public static void main(String args[]) {

        Scanner scan = new Scanner(System.in);

        while(true) {
            HashMap<String, Integer> counter = new HashMap<>();
            int ntests = scan.nextInt();

            boolean turnA = true;
            boolean repetition = false;

            if (ntests == 0) break;

            for (int i = 0; i < ntests; i++) {

                String newEntry = scan.next() + (turnA ? "turnA" : "turnB");
                if (counter.containsKey(newEntry)) {
                    counter.put(newEntry, counter.get(newEntry) + 1);
                } else {
                    counter.put(newEntry, 1);
                }

                if (counter.get(newEntry) == 5) {
                    repetition = true;
                }
                turnA = !turnA;
            }

            if (repetition) {
                System.out.println("SI");
            } else {
                System.out.println("NO");
            }


        }



    }
}
