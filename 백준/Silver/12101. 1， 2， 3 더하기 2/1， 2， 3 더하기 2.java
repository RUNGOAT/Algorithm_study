import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    // 숫자의 조합을 저장할 리스트
    static List<String>[] numberCombinations = new ArrayList[11];
    static int[] dp = new int[11];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        br.close();

        // 초기 숫자 조합 리스트를 초기화하는 메소드
        numberCombinations[1] = new ArrayList<>(Collections.singletonList("1"));
        numberCombinations[2] = new ArrayList<>(Arrays.asList("11", "2"));
        numberCombinations[3] = new ArrayList<>(Arrays.asList("111", "12", "21", "3"));
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;

        for (int i = 4; i < 11; i++) {
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
            numberCombinations[i] = new ArrayList<>();
            createNumberCombination("1", i - 1, i);
            createNumberCombination("2", i - 2, i);
            createNumberCombination("3", i - 3, i);
        }

        if (k > dp[n]) {
            System.out.println(-1);
            System.exit(0);
        }

        System.out.println(String.join("+", numberCombinations[n].get(k - 1).split("")));
    }

    // 주어진 숫자를 기반으로 숫자 조합을 생성하는 메소드
    static void createNumberCombination(String digit, int key, int number) {
        for (String num : numberCombinations[key]) {
            numberCombinations[number].add(digit + num);
        }
    }
}
