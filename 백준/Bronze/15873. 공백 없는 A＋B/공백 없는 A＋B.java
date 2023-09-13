import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int b = 0, a = sc.nextInt();
        
        if (a == 1010){         //1010
            System.out.println(20);
        }
        else if (a % 10 == 0){  //a10
            a /= 100;
            System.out.println(a+10);
        }
        else{
            b += a % 10;
            a /= 10;
            if (a == 10){       //10b
                System.out.println(10+b);
            }
            else{               //ab
                System.out.println(a+b);
            }
        }
    }
}