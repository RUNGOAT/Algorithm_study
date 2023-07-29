import java.util.*;
import java.io.*;

class Person implements Comparable<Person> {

    int idx;
    int score;

    public Person(int idx, int score) {
        this.idx = idx;
        this.score = score;
    }

    @Override
    public int compareTo(Person o) {
        return o.score - this.score;
    }
}

public class Main {

    public static void main(String args[]) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        int[] total = new int[N];
        int[] arr = new int[N];
        Person[] people = new Person[N];

        for (int i = 0; i < 3; i++) {
            calculateRanks(br, sb, N, total, arr, people);
        }
        calculateFinalRanks(sb, N, total, arr, people);

        System.out.println(sb.toString());
    }

    static void calculateRanks(BufferedReader br, StringBuilder sb, int N, int[] total, int[] arr, Person[] people) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        for (int n = 0; n < N; n++) {
            people[n] = new Person(n, Integer.parseInt(st.nextToken()));
            total[n] += people[n].score;
        }

        assignRank(arr, people, N);

        for (int n = 0; n < N; n++) {
            sb.append(arr[n] + " ");
        }
        sb.append("\n");
    }

    static void calculateFinalRanks(StringBuilder sb, int N, int[] total, int[] arr, Person[] people) {
        for (int n = 0; n < N; n++) {
            people[n] = new Person(n, total[n]);
        }

        assignRank(arr, people, N);

        for (int n = 0; n < N; n++) {
            sb.append(arr[n] + " ");
        }
        sb.append("\n");
    }

    static void assignRank(int[] arr, Person[] people, int N) {
        Arrays.sort(people);

        int size = 1;
        int rank = 1;
        int stack = people[0].score;
        arr[people[0].idx] = rank;

        for (int n = 1; n < N; n++) {
            if (people[n].score < stack) {
                rank += size;
                size = 1;
                stack = people[n].score;
            } else {
                size++;
            }
            arr[people[n].idx] = rank;
        }
    }
}
