function solution(s)
{
    var answer = -1;
    let array=s.split('')
    let length=s.length;
    // 길이 홀수면 0 반환
    if(s.length % 2 ===1)
        return 0;
    
    // 문자열 줄이는 과정
    let stack = [];
    for (let i = 0; i < s.length; i++) {
        stack.push(s[i]);
        if (stack.length > 1 && stack[stack.length - 1] === stack[stack.length - 2]) {
            stack.pop();
            stack.pop();
        }
    }
    
    if(stack.length>0)
        return 0;
    else
        return 1;
}