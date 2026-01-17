import java.util.Scanner;

public class en_ascensor_o_andando {

    public static void main(String args[]) {

        Scanner scan = new Scanner(System.in);

        while(true) {

            int iniFloor = scan.nextInt();
            int endFloor = scan.nextInt();
            int elevatorFloor = scan.nextInt();
            int walkTime = scan.nextInt();
            int elevateTime = scan.nextInt();
            int minimumTime = Integer.MAX_VALUE;

            if (iniFloor == 0 && endFloor == 0 && elevatorFloor == 0 && walkTime == 0 && elevateTime == 0){
                break;
            }
            
            minimumTime = Math.abs(endFloor - iniFloor) * walkTime;

            minimumTime = Math.min(minimumTime, Math.abs(iniFloor - elevatorFloor) * elevateTime + Math.abs(endFloor - iniFloor) * elevateTime);
            minimumTime = Math.min(minimumTime, Math.abs(elevatorFloor - iniFloor) * walkTime + Math.abs(endFloor - elevatorFloor) * elevateTime);

            System.out.println(minimumTime);

        }

    }

}
