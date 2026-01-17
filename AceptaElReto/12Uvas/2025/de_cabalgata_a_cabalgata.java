import java.util.Scanner;

public class de_cabalgata_a_cabalgata {

    public static void main(String args[]) {

        Scanner scan = new Scanner(System.in);

        while(scan.hasNext()) {

            int nLights = scan.nextInt();
            int range = scan.nextInt();
            long money = scan.nextLong();

            long[] summOfLights = new long[nLights];
            long[] prefixSum = new long[nLights];
            long highestSummOfLights = 0;

            for (int i = 0; i < nLights; i++) {
                long value = scan.nextLong();
                prefixSum[i] = value + prefixSum[Math.max(0,i-1)];
            }

            for (int i = 0; i < nLights; i++) {
                int leftIndex = i - range - 1;
                long sumLeft = (leftIndex < 0) ? 0 : prefixSum[leftIndex];
                long sumRight = prefixSum[Math.min(nLights-1, i+range)];

                summOfLights[i] = sumRight - sumLeft;
                highestSummOfLights = Math.max(highestSummOfLights, sumRight - sumLeft);
            }
            
            long right = highestSummOfLights + money;
            long left = 0;
            long ans = 0;

            while (left <= right) {

                long middle = left + (right - left) / 2;
                long accumulatedMoney = 0;                
                long accumulatedLight = 0;
                boolean notEnoughMoney = false;
                long[] maxRange = new long[nLights];

                for (int i = 0; i < nLights; i++) {
                    accumulatedLight-= maxRange[i];                    

                    if (summOfLights[i] + accumulatedLight < middle) {
                        int rightMostLight = i + 2*range + 1;
                        long diffLight = Math.abs(middle - (summOfLights[i] + accumulatedLight));
                        accumulatedMoney += diffLight;
                        accumulatedLight += diffLight;
                         if (accumulatedMoney > money) {
                            notEnoughMoney = true;
                            break;
                        }
                        if (rightMostLight < nLights) {
                            maxRange[rightMostLight]+= diffLight;
                        }   
                    }
                   
                }
                if (notEnoughMoney) {
                    right = middle-1;
                } else {
                    ans = middle;
                    left = middle+1;
                }
            }

            System.out.println(ans);
        }
        
    }
}
