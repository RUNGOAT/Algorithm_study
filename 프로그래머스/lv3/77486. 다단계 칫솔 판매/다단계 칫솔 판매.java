import java.util.*;

class Solution {
    
    static int[] answer;
    static String[] parent;
    static Map<String, Integer> indexMap;
    
    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {
        int N = enroll.length;
        answer = new int[N];
        
        indexMap = new HashMap<>();
        for (int i = 0; i < N; i++) {
            indexMap.put(enroll[i], i);
        }
        
        parent = new String[N];
        for (int i = 0; i < N; i++) {
            parent[indexMap.get(enroll[i])] = referral[i];
        }
        
        for (int i = 0; i < seller.length; i++) {
            dfs(seller[i], amount[i] * 100);
        }
        
        return answer;
    }
    
    void dfs(String key, int amount) {
        if (key.equals("-")) {
            return;
        }
        int rest = amount / 10;
        answer[indexMap.get(key)] += amount - rest;
        if (rest != 0) {
            dfs(parent[indexMap.get(key)], rest);   
        }
    }
}