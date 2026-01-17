import java.util.Scanner;

public class No_me_da_la_vida {
   
    public static void main(String[] args) { 

        Scanner scan = new Scanner(System.in);

        while(true) {
            if (!scan.hasNext()) break; 

            int nTests = scan.nextInt();
            
            if (nTests == 0) break;

            long duration = 0;

            for(int i = 0; i < nTests; i++) {
                duration += scan.nextLong();
            }

            long hours = duration / 3600;
            duration = duration % 3600;
            long minutes = duration / 60;
            long seconds = duration % 60;

            System.out.printf("%02d:%02d:%02d%n", hours, minutes, seconds);
        }
        
        scan.close();
    }
}