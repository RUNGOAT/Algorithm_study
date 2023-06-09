import java.util.*;
import java.time.*;
import java.time.format.DateTimeFormatter;

class Solution {
    public List<Integer> solution(String today, String[] terms, String[] privacies) {
        List<Integer> answer = new ArrayList<>();
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy.MM.dd");
        LocalDate todayDate = LocalDate.parse(today, dtf);
        
        Map<String, Integer> termsMap = new HashMap<>();
        
        for (String term : terms) {
            String[] split = term.split(" ");
            termsMap.put(split[0], Integer.parseInt(split[1]));
        }
        
        int idx = 1;
        for (String temp : privacies) {
            String[] privacy = temp.split(" ");
            LocalDate privacyDate = LocalDate.parse(privacy[0], dtf);
            int period = termsMap.get(privacy[1]);
            privacyDate = privacyDate.plusMonths(period).minusDays(1);
            
            if (check(todayDate, privacyDate)) {
                answer.add(idx);
            }
            idx++;
        }
        return answer;
    }
    
    boolean check(LocalDate today, LocalDate date) {
        return date.isBefore(today);
    }
}