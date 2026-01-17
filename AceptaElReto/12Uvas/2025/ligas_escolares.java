import java.math.BigInteger;
import java.util.Scanner;



public class ligas_escolares {

    public static BigInteger combinatorioBig(int n, int k) {    
    BigInteger resultado = BigInteger.ONE;
    if (k > n / 2) k = n - k;
    
    for (int i = 0; i < k; i++) {
        BigInteger numerador = BigInteger.valueOf(n - i);
        BigInteger denominador = BigInteger.valueOf(i + 1);
        
        resultado = resultado.multiply(numerador).divide(denominador);
    }
    
    return resultado;
}


    public static void main(String args[]) {

        Scanner scan = new Scanner(System.in);
        int nTests = scan.nextInt();

        for (int i = 0; i < nTests; i++) {
            int n = scan.nextInt();
            int k = scan.nextInt();
            BigInteger total = combinatorioBig(n, k);
            System.out.println(total);
        }

    }

}
