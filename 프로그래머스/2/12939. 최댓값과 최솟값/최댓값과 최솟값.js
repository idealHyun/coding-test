function solution(s) {
    const array=s.split(' ');
    
    const max=Math.max(...array);
    const min=Math.min(...array);
    
    return `${min} ${max}`
}