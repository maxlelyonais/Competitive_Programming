import java.util.Scanner;

public class hijos_a_tope {

    public static int maxHeight = 0;

    public static void main(String args[]) {

        Scanner scan = new Scanner(System.in);

        int nTests = scan.nextInt();

        for (int i = 0; i < nTests; i ++){

            maxHeight = 0;
            dfs(scan);

            System.out.println(maxHeight);

        }
    }
    
    public static int dfs(Scanner scan) {

        int nChildren = scan.nextInt();

        if (nChildren == 2) {
            // recursion over left child
            // recursion over right child
            int leftHeight = dfs(scan);
            int rightHeight = dfs(scan);
            int highest = 1 + Math.min(leftHeight, rightHeight);
            maxHeight = Math.max(maxHeight, highest);
            return highest;
        } else {
            if (nChildren == 1) {
                dfs(scan);
            }
            return 0;
        }
    }
}
