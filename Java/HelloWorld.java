import java.util.Random;
import java.util.Scanner;

/**
 * HelloWorld
 */

public class HelloWorld {
    public static int f(int n) {
        if (n == 0) {
            return 0;
        } else
            return 2 * f(n - 1) + n * n;
    }

    public static void main(String[] args) {
        Random a = new Random();
        for(int i=0; i < 100; ++i){
            System.out.println(a.nextInt(10));
        }
    }
}
