class Solution {
    public String solution(String phone_number) {
        StringBuilder answer = new StringBuilder();
        int starCount = phone_number.length() - 4;

        for (int i = 0; i < starCount; i++) {
            answer.append('*');
        }

        answer.append(phone_number.substring(starCount));

        return answer.toString();
    }
}