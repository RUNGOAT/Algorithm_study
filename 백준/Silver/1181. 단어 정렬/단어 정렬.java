import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		List<String> alphabet = new ArrayList<>();
		for (int i = 0; i < N; i++) {
			String str = br.readLine();
			if (alphabet.contains(str))
				continue;
			alphabet.add(str);
		}

		Collections.sort(alphabet, new Comparator<String>() {

			@Override
			public int compare(String o1, String o2) {
				if (o1.length() == o2.length()) {
					return o1.compareTo(o2);
				}
				return o1.length() - o2.length();
			}
		});

		for (int i = 0; i < alphabet.size(); i++) {
			System.out.println(alphabet.get(i));
		}
	}
}
