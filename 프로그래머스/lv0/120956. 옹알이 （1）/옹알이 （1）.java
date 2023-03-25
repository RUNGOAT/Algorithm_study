class Solution {
    String[] words = {"aya", "ye", "woo", "ma"};
    public int solution(String[] babbling) {
        int answer = 0;
		for (int i = 0; i < babbling.length; i++) {
			for (String word: words) {
				babbling[i] = babbling[i].replaceFirst(word, "0");
			}
			babbling[i] = babbling[i].replace("0", "");
			if (babbling[i].equals("")) answer++;
		}
        return answer;
    }
}