// 입력 처리
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");
const inputWords = [];
for (let i = 1; i < input.length; i++) {
	inputWords.push(
		input[i].trim()
	);
}
// console.log(inputWords);

// 문제 풀이

// 중복 제거 -> 길이가 짧은것 -> 길이가 같으면 사전순

const wordSet = new Set(inputWords);
const wordArr = Array.from(wordSet);
wordArr.sort((a, b) => {
	if (a.length === b.length) {
	  // 길이가 같을 때는 사전순 정렬
	  return a.localeCompare(b);
	}
	// 길이로 오름차순 정렬
	return a.length - b.length;
  });

wordArr.forEach((word)=>console.log(word))