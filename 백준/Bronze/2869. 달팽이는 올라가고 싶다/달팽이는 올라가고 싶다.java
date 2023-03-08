import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int v = Integer.parseInt(st.nextToken());

        if (v == a) {
            System.out.println(1);
        } else {
            v = v - a;
            int result = 1 + (v % (a - b) > 0 ? v / (a - b)+1 : v / (a - b));
            System.out.println(result);
        }
    }
}
