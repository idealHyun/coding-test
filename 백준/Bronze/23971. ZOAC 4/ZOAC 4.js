// 입력 처리
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = fs.readFileSync(filePath).toString().trim().split(" ");

// 문제 풀이

// H, W, N, M  , 세로 N칸 , 가로 M칸

const H = +input[0]; // 행(row) 수
const W = +input[1]; // 열(column) 수
const N = +input[2]; // 행(row) 수
const M = +input[3]; // 열(column) 수

console.log(Math.ceil(H/(N+1)) * Math.ceil(W/(M+1)));
