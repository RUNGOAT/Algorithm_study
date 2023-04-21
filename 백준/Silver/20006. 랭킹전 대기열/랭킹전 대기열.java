import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

class Player implements Comparable<Player> {
	int level;
	String name;

	public Player(String[] split) {
		this.level = Integer.parseInt(split[0]);
		this.name = split[1];
	}

	@Override
	public int compareTo(Player o) {
		return this.name.compareTo(o.name);
	}

	@Override
	public String toString() {
		return level + " " + name;
	}
}

public class Main {

	static int P;
	static int M;
	static List<List<Player>> list;

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		P = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		list = new ArrayList<>();
		list.add(new ArrayList<Player>());

		for (int i = 0; i < P; i++) {
			Player player = new Player(br.readLine().split(" "));

			boolean isAdmin = false;
			for (List<Player> players : list) {
				if (check(players, player)) {
					players.add(player);
					isAdmin = true;
					break;
				}
			}
			if (!isAdmin) {
				List<Player> players = new ArrayList<Player>();
				players.add(player);
				list.add(players);
			}
		}

		StringBuilder sb = new StringBuilder();
		for (List<Player> players : list) {
			if (players.size() == M) {
				sb.append("Started!\n");
			} else {
				sb.append("Waiting!\n");
			}
			game(sb, players);
		}
		System.out.println(sb);
	}

	static boolean check(List<Player> players, Player player) {

		if (players.size() == M) {
			return false;
		}

		if (players.size() != 0 
				&& Math.abs(players.get(0).level - player.level) > 10)
			return false;

		return true;
	}

	static void game(StringBuilder sb, List<Player> players) {
		Collections.sort(players);
		for (Player player : players) {
			sb.append(player.toString() + "\n");
		}
	}
}