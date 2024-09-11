// 입력 처리
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");
const inputN = +input[0];
const inputLine = [];
for (let i = 1; i < input.length; i++) {
	inputLine.push(
		input[i]
			.toString()
			.trim()
			.split(" ")
			.map((value) => BigInt(value))  // BigInt로 변환
	);
}

// 문제 풀이

for (let k = 0; k < inputN; k++) {
	const N = inputLine[k][0];
	const M = inputLine[k][1];
	if (N === M) {
		console.log(1);
	} else {
		let a = BigInt(1);
		let b = BigInt(1);
		for (let i = 0; i < N; i++) {
			a *= M - BigInt(i);
		}
		for (let i = N; i > 0; i--) {
			b *= BigInt(i);
		}
		console.log((a / b).toString());
	}
}
