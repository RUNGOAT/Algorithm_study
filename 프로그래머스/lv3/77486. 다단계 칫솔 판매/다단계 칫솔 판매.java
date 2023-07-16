import java.util.*;

class Solution {
    
    static int[] answer;
    static String[] parent;
    static Map<String, Integer> indexMap;
    static Map<String, List<Integer>> map;
    
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
        
        map = new HashMap<>();
        for (int i = 0; i < seller.length; i++) {
            map.put(seller[i], new ArrayList<>());
        }
        
        for (int i = 0; i < seller.length; i++) {
            List<Integer> list = map.get(seller[i]);
            list.add(amount[i] * 100);
        }
        
        for (String key : map.keySet()) {
            dfs(key, map.get(key));
        }
        
        return answer;
    }
    
    void dfs(String key, List<Integer> list) {
        if (key.equals("-")) {
            return;
        }
        int sum = 0;
        List<Integer> next = new ArrayList<>();
        for (int amount : list) {
            int rest = amount / 10;
            sum += amount - rest;
            next.add(rest);
        }
        answer[indexMap.get(key)] += sum;
        if (sum != 0) {
            dfs(parent[indexMap.get(key)], next);   
        }
    }
}