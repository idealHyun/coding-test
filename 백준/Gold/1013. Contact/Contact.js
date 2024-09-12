// 입력 처리
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");
const inputWords = [];
for (let i = 1; i < input.length; i++) {
	inputWords.push(input[i].trim());
}
// console.log(inputWords);

// 문제 풀이

// (100+1+ | 01)+

const patternReg = /^(100+1+|01)+$/;

inputWords.forEach((pattern) => {	
	patternReg.test(pattern) ? console.log("YES") : console.log("NO");
});
