| 파일명                         | 링크                                      |
| ------------------------------ | ----------------------------------------- |
| 1. 시간, 공간복잡도            | [링크1](./1.시간_공간복잡도.md)           |
| 2. 자료구조1. 배열, 연결리스트 | [링크2](./2.자료구조1_배열_연결리스트.md) |
| 3. 정렬                        | [링크3](./3.정렬.md)                      |
| 4. 이진탐색                    | [링크4](./4.이진탐색.md)                  |
| 5. 자료구조2. 스택, 큐, 덱     | [링크5](./5.자료구조2_스택_큐_덱.md)      |
| 6. 자료구조3. 트리             | [링크6](./6.자료구조3_트리.md)            |
| 7. 해싱                        | [링크7](./7.해싱.md)                      |
| 8. dp                          | [링크8](./8.dp.md)                        |
| 9. 그래프탐색                  | [링크9](./9.그래프탐색.md)                |
| 10. 그래프알고리즘             | [링크10](./10.그래프알고리즘.md)          |
| 11. 자료구조4. 해시맵, 트리맵  | [링크11](./11.자료구조4_해시맵_트리맵.md) |
| 12. 시간효율 테크닉            | [링크12](./12.시간효율_테크닉.md)         |
| 13. 패턴일치                   | [링크13](./13.패턴일치.md)                |



- 내용 renewal 예정 (~ 23/07)

<자료구조> (C나 Java로 다 직접 구현)

자료구조는 기본적으로 메모리가 연결된 형태의 array 와 떨어져 있지만 참조값으로 연결된 방식으로 구현된다.

List는 추상 개념(무엇인가 순서대로 들어있는 저장고가 있다) - STACK, QUEUE, DEQUEUE

Tree - TRIE(접미사트리, 접미사 배열(맨버-마이어스))(알고리즘?), 이진탐색트리(TreeSet, TreeMap), HEAP, SegmentTree, sqrt decomposition, Binary Indexed Tree, BST, B tree, B+tree, ATL tree, RB tree

Graph - adjList, adjMatrix

Hash - HashSet, HashMap, channing, open addressing



<알고리즘>

기본 - 점근적표기법, N NP문제, 브루트포스, 그리디, 디바이드 퀀쿼, DP



정렬(버블, 삽입, 선택, 병합, 퀵, 기수, 힙, 쉘, 카운트)



BFS, DFS

다익스트라, 벨만포드, 플루이드워셜

프림, 크루스칼

위상정렬

단절점



DP - tsp, knapsack



문자열 패턴 매칭 - 카프라빈, KMP, 보이어 무어



트리 - lca, 트리지름

uf, rank-compression, path-compression



binary search, Parametric search



(순열과 조합 - 비트마스킹, 순열의 다음값구하기)

Preprocessing - Prefix, Suffix sum

Grid-compression

LR technique

+1-1 Technique : 막대문제

Two pointer





### etc)

- 표준 문자 코드

  - 영문 알파벳은 6bits(6-bit)만으로도 표현 할 수 있다. 하지만 네트워크가 발전하며 지역별로 표현하는 방법이 달랐고, 이를 위해 7bits 기준 표준안인 ASCII(American Standard Code for Information Interchange)를 만들었다. 이는 33개의 출력 불가능한 제어문자와, 95개의 출력 가능한 문자들로 이루어져 있다.

    확장아스키는 8bits를 사용하며, 이는 정해진 값이 없이 서로 다른 프로그램이나 컴퓨터간 교환되지 못한다.


  - 영어 뿐 아니라 다국어 처리를 위해 유니코드가 만들어 졌다. 유니코드도 다시 character set에 따라 UCS-2(2바이트)와 UCS-4(4바이트)로 나뉘는데, 바이트 순서에 대해 표준화 하지 못했다. 즉 둘 중 어느 타입인지 인식을 해야 하는 문제가 발생했다.


  - big-endian은 낮은 자리수를 높은 주소에, little-endian은 낮은자리수를 낮은주소에 저장하는 방식이며 기본은 big-endian이다.


  - 인코딩 방식에는 UTF-8, UTF-16, UTF-32가 있다.

- 표준 입출력 방법

  파일의 내용을 표준 입력으로 읽어오는 방법

```python
# 입출력을 콘솔로 보내는 것이 아니라 파일을 거치도록 한다.
import sys
sys.stdin = open("a.txt", "r")
sys,stdout = open("output.txt", "w")
```

