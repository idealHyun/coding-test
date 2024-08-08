function solution(want, number, discount) {
    let answer=0;
    // Map 형태로 변환
    const wantNumber = new Map();
    for (let i = 0; i < want.length; i++) {
        wantNumber.set(want[i], number[i]);
    }
    // 10일 안에 다 원하는게 할인되는지 확인 후 계산
    for(let i=0;i<=discount.length-10;i++){
        let wantNumber_copy = new Map(wantNumber);
        
        for (let j = i; j < i + 10; j++) {
            if (wantNumber_copy.has(discount[j]) && wantNumber_copy.get(discount[j])>0) {
                wantNumber_copy.set(discount[j], wantNumber_copy.get(discount[j]) - 1);
            }
        }
        let sum=0;
        wantNumber_copy.forEach((value)=>{
            sum+=value;
        })
        if(sum===0)
            answer++;
    }
    return answer;
}