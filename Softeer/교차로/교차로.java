import java.util.*;
import java.io.*;

interface ICrossroad {
    void queueAdd(int num, int t, char w);
    boolean isEmptyRoad();
    boolean isDeadLock();
    void carMove();
    int[] getAnswer();
}

class Car {
    private final int num;
    private final int t;

    Car(int num, int t) {
        this.num = num;
        this.t = t;
    }

    public int getNum() {
        return this.num;
    }

    public int getT() {
        return this.t;
    }
}

class Crossroad implements ICrossroad {
    private Deque<Car>[] carWidth;
    private boolean isDeadLock;
    private int time;
    private int[] answer;

    public Crossroad(int N) {
        this.carWidth = new LinkedList[4];
        this.isDeadLock = false;
        this.time = 0;
        this.answer = new int[N];
        for (int i = 0; i < 4; i++) {
            this.carWidth[i] = new LinkedList<>();
        }
        for (int i = 0; i < N; i++) {
            this.answer[i] = -1;
        }
    }

    public void queueAdd(int num, int t, char w) {
        int idx = w - 'A';
        carWidth[idx].addLast(new Car(num, t));
    }

    public boolean isEmptyRoad() {
        return carWidth[0].isEmpty() && carWidth[1].isEmpty() && carWidth[2].isEmpty() && carWidth[3].isEmpty();
    }

    public boolean isDeadLock() {
        return this.isDeadLock;
    }

    public void carMove() {
        int[] crossroads = new int[4];
        int minTime = Integer.MAX_VALUE;
        for (int d = 0; d < 4; d++) {
            Car car = carWidth[d].peek();
            if (car != null) {
                minTime = Math.min(minTime, car.getT());
                if (car.getT() <= time) {
                    crossroads[d] = 1;
                }
            }
        }

        int count = sum(crossroads);
        if (count == 4) {
            isDeadLock = true;
            return;
        } else if (count == 0) {
            time = minTime;
            return;
        }

        for (int i = 0; i < 4; i++) {
            if (crossroads[(i + 3) % 4] == 1) {
                // 오른쪽에 차량이 있음.
                continue;
            }
            if (crossroads[i] == 0) {
                continue;
            }
            Car car = carWidth[i].poll();
            answer[car.getNum()] = time;
        }
        time++;
    }

    public int[] getAnswer() {
        return this.answer;
    }

    private static int sum(int[] arr) {
        int sum = 0;
        for (int num : arr) {
            sum += num;
        }
        return sum;
    }
}

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        ICrossroad crossroad = new Crossroad(N);

        for (int num = 0; num < N; num++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int t = Integer.parseInt(st.nextToken());
            char w = st.nextToken().charAt(0);
            crossroad.queueAdd(num, t, w);
        }

        while (!crossroad.isEmptyRoad()) {
            if (crossroad.isDeadLock()) {
                break;
            }
            crossroad.carMove();
        }

        StringBuilder sb = new StringBuilder();
        for (int i : crossroad.getAnswer()) {
            sb.append(i).append("\n");
        }
        System.out.println(sb.toString());
    }
}
