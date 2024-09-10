const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");
const arr=input[1].split(' ');

// 영식 : 30초마다 10원씩
// 민식 : 60초마다 15원씩
let m = 0;
let y =0;

[...arr].forEach((num)=>{
    while(num>=0){
        num-=30;
        y+=10;
    }
});

[...arr].forEach((num)=>{
    while(num>=0){
        num-=60;
        m+=15;
    }
})

if(m>y){
    console.log(`Y ${y}`);
} else if(m<y){
    console.log(`M ${m}`);
} else{
    console.log(`Y M ${m}`);
}