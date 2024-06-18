function solution(numbers, hand) {
    var answer = '';
    var num_position=[[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]];
    var left_position=[3,0];
    var right_position=[3,2];
    for(let i=0;i<numbers.length;i++){
        if(numbers[i]=='1' || numbers[i]=='4' ||numbers[i]=='7'){
            answer+='L';
            left_position=num_position[numbers[i]];
        }else if(numbers[i]=='3' || numbers[i]=='6' ||numbers[i]=='9'){
            answer+='R';
            right_position=num_position[numbers[i]];
        } else {
            let left_dist=Math.abs(num_position[numbers[i]][0]-left_position[0])+Math.abs(num_position[numbers[i]][1]-left_position[1]);
            let right_dist=Math.abs(num_position[numbers[i]][0]-right_position[0])+Math.abs(num_position[numbers[i]][1]-right_position[1]);
            if(left_dist>right_dist){
                answer+='R';
                right_position=num_position[numbers[i]];
            } else if(left_dist<right_dist){
                answer+='L';
                left_position=num_position[numbers[i]];
            } else{
                if(hand==='right'){
                    answer+='R';
                    right_position=num_position[numbers[i]];
                } else{
                    answer+='L';
                    left_position=num_position[numbers[i]];
                }
            }
        }
    }
    return answer;
}