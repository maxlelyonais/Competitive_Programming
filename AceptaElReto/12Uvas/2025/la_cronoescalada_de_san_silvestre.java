import java.util.Scanner;

public class la_cronoescalada_de_san_silvestre {


    public static long merge(int left, int right, int middle, int[] array) {
        long totalInversions = 0;

        int n1 = middle - left + 1;
        int n2 = right - middle;

        int[] auxiliarArray = new int[n1 + n2];

        int i = 0, j = 0;

        while (i < n1 && j < n2) {
            int element = 0;
            if (array[middle+j+1] < array[left+i]){
                totalInversions += (n1 - i);
                element = array[middle+j+1];
                auxiliarArray[i+j] = element;
                j+=1;
            } else {
                element = array[left+i];
                auxiliarArray[i+j] = element;
                i+=1;
            }
        }

        while (i < n1) {
            int element = array[left+i];
            auxiliarArray[i+j] = element;
            i+=1;
        }

        while (j < n2) {
            int element = array[middle+j+1];
            auxiliarArray[i+j] = element;
            j+=1;
        }

        int k = 0;
        for (int p = left; p <= right; p++) {
            array[p] = auxiliarArray[k];
            k+=1;
        }

        return totalInversions;
    }


    public static long mergeSort(int left, int right, int[] array) {

        long totalInversions = 0;

        if (left < right) {
            int middle = (left + right) / 2;

            totalInversions+=mergeSort(left, middle, array);
            totalInversions+=mergeSort(middle+1, right, array);
            totalInversions+= merge(left, right, middle, array);           
        }

        return totalInversions;
    }


    public static void main(String args[]) {

        Scanner scan = new Scanner(System.in);

        while (true){

            int nTrams = scan.nextInt();
            if (nTrams == 0) break;

            int[] CansinoCumulativeTime = new int[nTrams+1];
            int ConstantinTime = scan.nextInt();
            CansinoCumulativeTime[0] = 0;

            for (int i = 1; i <= nTrams; i++) {
                int time = scan.nextInt();
                CansinoCumulativeTime[i] = CansinoCumulativeTime[i - 1] + (time - ConstantinTime);
            }

            long result = mergeSort(0, nTrams++, CansinoCumulativeTime);
            System.out.println(result);
        }

    }
}
