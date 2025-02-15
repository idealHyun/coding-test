import java.util.*;

class Solution {
    public long solution(long n) {
        char[] charArray = String.valueOf(n).toCharArray();
        
        Arrays.sort(charArray);
        
        StringBuilder sb = new StringBuilder(new String(charArray)).reverse();
        
        return Long.parseLong(sb.toString());
    }
}
