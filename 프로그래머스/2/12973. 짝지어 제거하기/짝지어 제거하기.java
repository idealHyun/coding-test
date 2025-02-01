import java.util.*;

class Solution
{
    public int solution(String s)
    {
        int answer = -1;
        Deque<Character> stack = new ArrayDeque<Character>();
        
        for(int i=0;i<s.length();i++){
            if(stack.isEmpty()){
                stack.push(s.charAt(i));
            }else{
                Character prev = stack.peek();
                if(prev==s.charAt(i)){
                    stack.pop();
                }else{
                    stack.push(s.charAt(i));
                }
            }
        }

        if(stack.isEmpty()){
            return 1;
        }else{
            return 0;
        }
    }
}