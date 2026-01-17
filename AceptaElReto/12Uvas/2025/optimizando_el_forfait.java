import java.io.IOException;
import java.io.InputStream;

public class optimizando_el_forfait {

    public static void main(String[] args) throws IOException {
        FastReader sc = new FastReader();

        while (true) {

            int nDays = sc.nextInt();
            int nVacationsDay = sc.nextInt();

            if (nDays == 0 && nVacationsDay == 0) {
                break;
            }

            int bestDay = -1;

            long currentWindowSnow = 0;
            long minimumDaySnow = Long.MAX_VALUE;
            long minimumWindowSnow = Long.MAX_VALUE;

            long[] dqValue = new long[nVacationsDay+1];
            int[] dqDays = new int[nVacationsDay+1];
            long[] history = new long[nVacationsDay];
            int pointTail = 0;
            int pointHead = 0;  
            int circularModule = nVacationsDay+1;       
            
            for (int i = 0; i < nDays; i++) {

                long recentSnow = sc.nextLong();

                if (i >= nVacationsDay-1) {
                    currentWindowSnow -= history[(i % nVacationsDay)];
                }

                currentWindowSnow+= recentSnow;
                history[(i % nVacationsDay)] = recentSnow;

                while (pointHead != pointTail) {
                    int lastIdx = (pointTail - 1 + circularModule ) % circularModule;
                    long toCompareSnow = dqValue[lastIdx];
                    if (toCompareSnow > recentSnow) {
                        pointTail = lastIdx;
                    } else {
                        break;
                    }
                }

                dqValue[pointTail] = recentSnow;
                dqDays[pointTail] = i;
                pointTail = (pointTail+1) % circularModule;

                if (dqDays[pointHead] <= (i-nVacationsDay)) {
                    pointHead = (pointHead+1) % circularModule;
                }

                if (i >= nVacationsDay-1) {

                    long toCompareSnowDay = dqValue[pointHead];
                    boolean update = false;

                    if (toCompareSnowDay < minimumDaySnow) {
                        update = true;
                    } else if (toCompareSnowDay == minimumDaySnow && currentWindowSnow < minimumWindowSnow){
                        update = true;
                    }   

                    if (update) {
                        minimumDaySnow = toCompareSnowDay;
                        minimumWindowSnow = currentWindowSnow;
                        bestDay = i - nVacationsDay+2;
                    }
                }
            }
            System.out.println(bestDay + " " + minimumWindowSnow);
        }

    }

    static class FastReader {
        InputStream in;

        public FastReader() {
            in = System.in;
        }

        public int nextInt() throws IOException {
            int ret = 0;
            byte c = read();
            while (c <= ' ') c = read();
            boolean neg = (c == '-');
            if (neg) c = read();
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');
            if (neg) return -ret;
            return ret;
        }

        public long nextLong() throws IOException {
            long ret = 0;
            byte c = read();
            while (c <= ' ') c = read();
            boolean neg = (c == '-');
            if (neg) c = read();
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');
            if (neg) return -ret;
            return ret;
        }

        private byte read() throws IOException {
            return (byte) in.read();
        }
    }
}