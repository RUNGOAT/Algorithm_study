import java.util.*;

class Solution {
    
    static int[] answer;
    static String[] language = {"cpp", "java", "python"};
    static String[] job = {"backend", "frontend"};
    static String[] career = {"junior", "senior"};
    static String[] food = {"chicken", "pizza"};
    
    int binary(List<Integer> list, int target) {
        int start = 0;
        int end = list.size();
        
        while (start < end) {
            int mid = (start + end) / 2;
            if (list.get(mid) < target) {
                start = mid + 1;
            } else {
                end = mid;
            }
        }
        return end;
    }
    
    void dfs(Object obj, int depth, String[] condition, int idx) {
        if (depth == 4) {
            List<Integer> scores = (ArrayList<Integer>) obj;
            int score = Integer.parseInt(condition[depth]);
            int start = binary(scores, score);
            answer[idx] += scores.size() - start;
            return;
        }
        
        Map<String, Object> map = (HashMap<String, Object>) obj;
        if (condition[depth].equals("-")) {
            for (String key : map.keySet()) {
                dfs(map.get(key), depth + 1, condition, idx);
            }
        } else {
            dfs(map.get(condition[depth]), depth + 1, condition, idx);
        }
    }
    
    public int[] solution(String[] info, String[] query) {
        answer = new int[query.length];
        Map<String, Map<String, Map<String, Map<String, List<Integer>>>>> map = new HashMap<>();
        
        for (String l : language) {
            map.put(l, new HashMap<>());
            for (String j : job) {
                map.get(l).put(j, new HashMap<>());
                for (String c : career) {
                    map.get(l).get(j).put(c, new HashMap<>());
                    for (String f : food) {
                        map.get(l).get(j).get(c).put(f, new ArrayList<>());
                    }
                }
            }
        }
        
        for (String information : info) {
            String[] line = information.split(" ");
            map.get(line[0]).get(line[1]).get(line[2]).get(line[3]).add(Integer.parseInt(line[4]));
        }
        
        for (String l : language) {
            for (String j : job) {
                for (String c : career) {
                    for (String f : food) {
                        Collections.sort(map.get(l).get(j).get(c).get(f));
                    }
                }
            }
        }
        
        for (int i = 0; i < query.length; i++) {
            String[] condition = query[i].replace(" and ", " ").split(" ");
            dfs(map, 0, condition, i);
        }
        return answer;
    }
    
}