import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int A, B;
        A = sc.nextInt();
        B = sc.nextInt();
        if (0<A&&A<10 && 0<B&&B<10){
            System.out.println(A + B);
        }
    }
}