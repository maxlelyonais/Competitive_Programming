import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Irving {

    static class Point {
        double x;
        double y;

        public Point(double x, double y) {
            this.x = x;
            this.y = y;
        }
    }

    public static long calcularArea(List<Point> points) {
        int n = points.size();
        long suma1 = 0, suma2 = 0;

        for (int i = 0; i < n; i++) {
            int siguiente = (i + 1) % n;
            suma1 += points.get(i).x * points.get(siguiente).y;
            suma2 += points.get(i).y * points.get(siguiente).x;
        }

        return Math.abs(suma1 - suma2) / 2;
    }

    public static void main(String args[]) {

        Scanner scan = new Scanner(System.in);

        
        while(scan.hasNextLine()) {

            String[] elements = scan.nextLine().split(" ");
            List<Point> vertex = new ArrayList<>();

            int x = 0;
            int y = 0;
            vertex.add(new Point(x,y));
            String prevMov = "";
            for(int i = 0; i < elements.length; i++) {

                switch (elements[i]) {
                    case "e":
                        
                        if (prevMov.equals("n") || prevMov.equals("s")) {
                            vertex.add(new Point(x,y));
                        }
                        y+=1;
                        break;
                    case "n":

                        if (prevMov.equals("e") || prevMov.equals("o")) {
                            vertex.add(new Point(x,y));
                        }
                        x+=1;
                        break;
                    case "o":

                        if (prevMov.equals("n") || prevMov.equals("s")) {
                            vertex.add(new Point(x,y));
                        }
                        y-=1;
                        break;
                    case "s":

                        if (prevMov.equals("e") || prevMov.equals("o")) {
                            vertex.add(new Point(x,y));
                        }
                        x-=1;
                        break;
                    case "E":

                        if (prevMov.equals("n") || prevMov.equals("s")) {
                            vertex.add(new Point(x,y));
                        }
                        y+=Integer.parseInt(elements[i+1]);
                        break;
                    case "N":

                        if (prevMov.equals("e") || prevMov.equals("o")) {
                            vertex.add(new Point(x,y));
                        }
                        x+=Integer.parseInt(elements[i+1]);
                        break;
                    case "O":

                        if (prevMov.equals("n") || prevMov.equals("s")) {
                            vertex.add(new Point(x,y));
                        }
                        y-=Integer.parseInt(elements[i+1]);
                        break;
                    case "S":

                        if (prevMov.equals("e") || prevMov.equals("o")) {
                            vertex.add(new Point(x,y));
                        }
                        x-=Integer.parseInt(elements[i+1]);
                        break;
                    default:
                        break;
                }
                prevMov = elements[i].toLowerCase();

                if (elements[i].equals("N") || elements[i].equals("S") || elements[i].equals("E") || elements[i].equals("O")) {
                    i+=1;
                }
            }

            System.out.println(calcularArea(vertex));

        }



    }
}
