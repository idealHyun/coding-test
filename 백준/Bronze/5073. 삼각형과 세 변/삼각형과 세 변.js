// 입력 처리
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");
inputLine = [];
input.forEach((line) => {
	inputLine.push(line.trim().split(" "));
});
inputLine.pop();

// 문제 풀이

// Equilateral :  세 변의 길이가 모두 같은 경우
// Isosceles : 두 변의 길이만 같은 경우
// Scalene : 세 변의 길이가 모두 다른 경우
// Invalid : 가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 길지 않은 경우

inputLine.forEach((line) => {
	line.sort((a, b) => a - b);
	if (+line[0] + +line[1] > +line[2]) {
		const set = new Set(line);
		switch (set.size) {
			case 1:
				console.log("Equilateral");
				break;
			case 2:
				console.log("Isosceles");
				break;
			case 3:
				console.log("Scalene");
				break;
		}
	} else {
		console.log("Invalid");
	}
});
