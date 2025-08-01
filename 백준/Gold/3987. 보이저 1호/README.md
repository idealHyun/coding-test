# [Gold V] 보이저 1호 - 3987 

[문제 링크](https://www.acmicpc.net/problem/3987) 

### 성능 요약

메모리: 68956 KB, 시간: 280 ms

### 분류

그래프 이론, 그래프 탐색, 구현, 시뮬레이션

### 제출 일자

2025년 7월 31일 15:19:31

### 문제 설명

<p>보이저 1호는 1977년에 발사된 NASA의 태양계 무인 탐사선이다. 현재 보이저 1호는 태양권덮개 (헬리오시스)에 있다.</p>

<p>보이저 1호와 같이 오랜 기간동안 활동하는 탐사선은 경로를 항성계를 만날 때 마다 라디오 시그널 메시지를 이용해서 기록하고 있다.</p>

<p>항성계를 N * M개의 직사각형으로 나누어져 있는 N행 M열의 직사각형 그리드라고 생각해보자. 각 칸은 행성, 블랙홀을 포함할 수 있으며, 비어있을 수도 있다. 탐사선은 인접한 네 칸(위, 아래, 오른쪽, 왼쪽)중에서 하나를 골라서 시그널을 보낸다.</p>

<p>시그널은 항상 일직선으로 전파되며, 행성을 만났을 경우에는 전파되는 방향이 90도로 바뀌게 된다. 행성은 '/'와 '\'로 표현되는 두 종류가 있으며, 반사되는 법칙은 아래 그림과 같다.</p>

<p style="text-align:center"><img alt="" src="https://upload.acmicpc.net/d64de82b-5fce-46ac-a54a-315b0a157136/-/preview/" style="width: 641px; height: 134px;"></p>

<p>시그널이 블랙홀이 있는 칸을 만나거나 항성계를 벗어날 때 까지 계속 전파된다. 시그널이 인접한 칸으로 이동하는데 걸리는 시간은 1초이다.</p>

<p>탐사선이 어느 방향으로 시그널을 보내면, 시그널이 항성계 내부에 있는 시간이 최대가 되는지 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 N과 M이 주어진다. (1 ≤ N, M ≤ 500)</p>

<p>다음 N개 줄에는 M개의 문자가 주어지며, '/'와 '\'는 행성을, C는 블랙홀을, '.'는 빈 칸을 나타낸다.</p>

<p>마지막 줄에는 탐사선이 있는 위치 PR과 PC가 주어진다. (1 ≤ PR ≤ N, 1 ≤ PC ≤ M)</p>

### 출력 

 <p>첫째 줄에 시그널을 보내는 방향을 출력한다. (U: 위, R: 오른쪽, D: 아래, L: 왼쪽)</p>

<p>만약, 방향이 여러 가지가 존재한다면, U, R, D, L의 순서 중 앞서는 것을 출력한다.</p>

<p>둘째 줄에는 가장 긴 시간을 출력한다. 만약, 시그널이 항성계 내에서 무한히 전파될 수 있다면 "Voyager"를 출력한다.</p>

