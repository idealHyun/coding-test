function solution(a, b) {
    var count=0;
    var day=[31,29,31,30,31,30,31,31,30,31,30,31]
    var week=["FRI","SAT","SUN","MON","TUE","WED","THU"];
    for(let i=0;i<a-1;i++){
        count=count+day[i];
    }
    var answer=week[(count+b-1)%7];
    return answer;
}