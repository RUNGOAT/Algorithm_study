import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static long answer;
    static int[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }
        calculateDifference(0, N, findMaxValue(0, N));
        System.out.println(answer);
    }

    static void calculateDifference(int start, int end, int max) {
        if (end <= start) {
            return;
        }
        if (end - start == 1 || checkIfAllSame(start, end)) {
            answer += max - arr[start];
            return;
        }
        int maxIdx = findMaxIndex(start, end);
        calculateDifference(start, maxIdx, arr[maxIdx]);
        calculateDifference(maxIdx + 1, end, arr[maxIdx]);
        answer += max - arr[maxIdx];
    }

    static int findMaxIndex(int start, int end) {
        int max = Integer.MIN_VALUE;
        int index = -1;
        for (int i = start; i < end; i++) {
            if (max < arr[i]) {
                max = arr[i];
                index = i;
            }
        }
        return index;
    }

    static int findMaxValue(int start, int end) {
        int max = Integer.MIN_VALUE;
        for (int i = start; i < end; i++) {
            if (max < arr[i]) {
                max = arr[i];
            }
        }
        return max;
    }

    static boolean checkIfAllSame(int start, int end) {
        int first = arr[start];
        for (int i = start + 1; i < end; i++) {
            if (first != arr[i]) {
                return false;
            }
        }
        return true;
    }
}
