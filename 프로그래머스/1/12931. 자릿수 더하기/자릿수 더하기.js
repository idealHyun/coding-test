function solution(n)
{
    var answer = 0;
    
    const array=String(n).split('');
    array.map((num)=>answer+=Number(num))

    return answer;
}