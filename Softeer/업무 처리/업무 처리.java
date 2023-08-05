import java.util.*;
import java.io.*;


public class Main
{
    static Queue<Integer>[][] tasks;

    public static void main(String args[]) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int h = Integer.parseInt(st.nextToken()); // 이진트리 높이
        int k = Integer.parseInt(st.nextToken()); // k개의 일
        int r = Integer.parseInt(st.nextToken()); // r일 동안 처리

        int leaf = (int) Math.pow(2, h);        // 말단 직원 수
        int n = (int) Math.pow(2, h+1) - 1;     // 전체 직원 수

        tasks = new Queue[n][2];
        for (int i = 0; i < n; i++) {
            tasks[i][0] = new LinkedList<>();
            tasks[i][1] = new LinkedList<>();
        }

        for (int i = n - leaf; i < n; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < k; j++) {
                // 말단 직원의 업무는 편의상 left(= 0)에 등록한다.
                tasks[i][0].add(Integer.parseInt(st.nextToken()));
            }
        }

        int answer = 0;
        for (int day = 1; day <= r; day++) {
            boolean isOddDay = (day & 1) == 1 ? true : false;
            // 부서장 업무 처리
            if (isOddDay) {
                if (!tasks[0][0].isEmpty()) {
                    answer += tasks[0][0].poll();
                }
            } else {
                if (!tasks[0][1].isEmpty()) {
                    answer += tasks[0][1].poll();
                }
            }

            // 중간 직원 업무 처리
            for (int i = 1; i < n-leaf; i++) {
                int parent = (i - 1) / 2;
                if (isOddDay) {
                    addTask(i, 0, parent);
                } else {
                    addTask(i, 1, parent);
                }
            }

            // 말단 직원 업무 처리
            for (int i = n - leaf; i < n; i++) {
                int parent = (i - 1) / 2;
                addTask(i, 0, parent);
            }
        }
        System.out.println(answer);
    }

    static void addTask(int i, int d, int parent) {
        if (!tasks[i][d].isEmpty()) {
            int task = tasks[i][d].poll();
            if ((i & 1) == 1) {
                tasks[parent][0].offer(task);
            } else {
                tasks[parent][1].offer(task);
            }
        }
    }
}
