## 사슴사냥대회(게임이론)

### 1. 문제 설명

어느 산속에 사냥꾼 둘이 살고 있었다. 사냥꾼 A와 B는 사전 협의 없이 그날 어떤 짐승을 사냥할지 결정한다. 사슴을 사냥하는 데는 둘의 협력이 필요하고, 토끼를 사냥하는 데는 혼자의 힘으로도 충분하다. 뱀을 사냥하는 데에도 혼자의 힘으로 충분하며, 만약 상대방이 토끼를 사냥했다면 뱀을 이용하여 상대방이 획득한 토끼를 상대방 몰래 훔칠 수 있다. 결과적으로 사슴을 사냥하기로 결정했다면, 상대방도 사슴을 택했을 경우,  사냥에 성공하여 둘 다 50의 이득을 취한다. 하지만, 상대방이 토끼나 뱀을 택했을 경우 나는 아무런 이득도 취할 수 없다. (이때, 상대방이 토끼를 택했다면 20의 이득을 뱀을 택했다면 10의 이들을 취득) 토끼를 사냥하기로 결정한 사냥꾼은 상대방이 사슴이나 토끼를 선택할 경우 20의 이득을 취하지만, 뱀을 취할 경우 아무런 이득도 취할 수 없다. 뱀을 사냥하기로 결정한 사냥꾼은 상대방의 결정에 상관없이 10의 이득을 취할 수 있으며, 상대방이 토끼를 택할 경우 20의 이득을 추가로 획득하여 총 30의 이득을 취할 수 있다.

| A \ B | 사슴         | 토끼         | 뱀           |
| ----- | ------------ | ------------ | ------------ |
| 사슴  | A: 50, B: 50 | A: 0, B: 20  | A: 0, B: 10  |
| 토끼  | A: 20, B: 0  | A: 20, B: 20 | A: 0, B: 30  |
| 뱀    | A: 10, B: 0  | A: 30, B: 0  | A: 10, B: 10 |

본인은 사냥꾼 1명의 입장으로 대회에 참석한다. 사냥꾼들은 산에 차례대로 올라가 10일씩 지내게 된다. 예를 들어 전체 사냥꾼이 5명이면 1번 사냥꾼은 2번, 3번, 4번, 5번 사냥꾼 각각과 산속에서 10일씩 총 40일을 지내게 된다. 같은 상대방과는 무조건 2번씩만 올라가며, 리그전을 치른다고 생각해도 좋다. 첨부에서 주어진 코드(main.py, Main.java, main.cpp) 에서는 가상의 상대편 사냥꾼 3인과 경쟁을 펼치게 되며, 제출 후에는 팀간 실제 매치가 이루어진다. 이때 가장 많은 이득을 취할 수 있도록, python, c, c++언어를 선택할 경우는 Me()함수를, java언어를 선택할 경우는 hunt()메소드를 구현하여 제출한다.



[페널티] 같은 동물을 연속해서 고르게 되면(리턴하게 되면) 다음과 같은 페널티가 적용된다.

|      | 사슴 | 토끼 | 뱀   |
| ---- | ---- | ---- | ---- |
| 1회  | 0    | 0    | 0    |
| 2회  | -1   | -2   | -3   |
| 3회  | -2   | -4   | -6   |
| ...  |      |      |      |
| 10회 | -9   | -18  | -27  |

예를 들어 세 번 연속 토끼를 선택한 상황에서 네 번째로 다시 토끼를 선택했다면 20 – 6 = 14점을 획득하게 된다. 상대방 사냥꾼이 바뀌거나 이전 선택과 다른 동물을 선택하면 페널티 정보는 0으로 초기화된다.



[운] 매 턴마다 0,1,2 중 하나의 점수가 랜덤 하게 가산된다



### 2. 문제 구현 방법

인수를 통해 몇가지 정보가 주어질 때, 본인이 이번 턴에 어떤 행동을 선택할 지 결정하는 함수를 만든다.

opp: 대결할 상대방 플레이어의 번호를 나타낸다.

turn: 0이상 9이하, 해당 플레이어와의 현재 진행 턴을 나타낸다. (총 10회)

opp_prev: 이번 게임에서 현재 상대방의 바로 이전 선택을 나타낸다. (-1: 모름, 0: 사슴, 1: 토끼, 2: 뱀. turn이 0 인경우 0, 주어진 정수가 아닌경우 상대방이 이전에 이상한 값을 제출한 것이다.)

opp_last_pattern[\][10\]: 현재 상대방의 바로 이전 게임 기록을 보여준다. 즉 상대방이 나와 만나기 직전 다른 사람과 게임을 했다면 그 기록을 나타낸다. 상대방 입장에서 내가 첫 상대이면 {-1, -1, ..., -1}로 주어지며, 그렇지 않을 경우 0 또는 1또는 2로 채워진 배열이 주어진다. 예를 들어 {0, 1, 1, 0, 2, 2,  1, 1, 1, 0} 으로 주어진다면 {사슴, 토끼, 토끼, 사슴, 뱀, 뱀, 토끼, 토끼, 토끼, 사슴}  순으로 선택한 경우이다. (이 역시 상대방이 이상한 값을 리턴한 적이 있다면 그 정보가 반영된다)

Return : 0를 리턴하면 현재 턴에서 사슴을 선택한다는 뜻이며, 1을 리턴하면 토끼를, 2를 리턴하면 뱀을 선택한다는 뜻. 그 외의 값을 리턴하면 -100점의 페널티를 매 턴마다 받는다.



### 3. 팀원과 회의 내용

이기적 유전자라는 책을 보며 사회 게임이론을 접한적이 있던 나는, 눈에는 눈 이에는 이로 대응하는 TFT가 게임이론에서 가장 좋은 승률을 가진다는것을 알고 있었다. 그렇기 때문에 상대방의 이전 값이 착한지 나쁜지에 따라 값을 결정하는 방향으로 진행하자고 강하게 어필했다.

약 45분간 각자 코드를 짠 뒤 서로의 코드를 설명하고, 대결도 해 보았다.

```python
# 내 코드
def Me(opp, turn, opp_prev, opp_last_pattern) :
	# 이전 기록이 있는지 확인
    for pre in opp_last_pattern:
        if pre == -1:
            is_prev = False
            break
    else:
        is_prev = True
    
    if is_prev and turn == 0:
        opp = opp_last_pattern[-1]

    # 이전 기록이 있고, trun이 9이면 무조건 배신
    if is_prev and turn == 9:
        if opp == 2:
            return 1
        else:
            return 2

    # 상대방과의 이전 기록이 있다면 기록을 이용
    if opp == 0 or opp == 1 or opp == 2:
        return opp
    else:
        return 0
```

```python
# 동환이 코드
arr = [3] * 10
pre = -1
def Me(opp, turn, opp_prev, opp_last_pattern) :
    global pre
    # 이 부분에 여러분의 알고리즘 구현이 들어갑니다
    arr[turn-1] = opp_prev
    # print(arr)
    if -1 in opp_last_pattern[0]:
        prevs = arr[:turn]
        # print(prevs)
        deer = prevs.count(0) / (turn+1)
        rabbit = prevs.count(1) / (turn+1)
        snake = prevs.count(2) / (turn+1)
        result = max(deer, rabbit, snake)
        if result == snake:
            if pre == 2:
                pre = 0
                return 0
            else:
                pre = 2
                return 2
        elif result == rabbit:
            if pre == 1:
                pre = 2
                return 2
            else:
                pre = 1
                return 1
        else:
            return 0
    elif opp_last_pattern[0].count(1) == 10: # 토끼만 내는 사람이면 뱀으로 대응
        cards = {1:1, 0:2}
        return cards[turn%2]
    elif opp_last_pattern[0].count(2) == 10:
        cards = {1:0, 0:2}
        return cards[turn%2]
    else:
        prevs = arr[:turn]
        deer_weight = opp_last_pattern[0].count(0)
        rabbit_snake_weight = opp_last_pattern[0].count(1)+opp_last_pattern[0].count(2)
        deer = prevs.count(0) / (turn+1) * deer_weight
        rabbit = prevs.count(1) / (turn+1) * rabbit_snake_weight
        snake = prevs.count(2) / (turn+1) * rabbit_snake_weight
        result = max(deer, rabbit, snake)
        if result == snake:
            if pre == 2:
                pre = 0
                return 0
            else:
                pre = 2
                return 2
        elif result == rabbit:
            if pre == 1:
                pre = 2
                return 2
            else:
                pre = 1
                return 1
        else:
            return 0
```

나는 단순히 상대방이 이전에 낸 수를 모방했다. 이 방법이 TFT이고, 일반적인 게임이론에서 가장 좋다고 알고 있기 때문이다. 나중에 생각해보니 지금 SSAFY에서 하는것은 변형된 게임이기에 문제에 맞게 Customizing하는게 당연했다.(커스터마이징 하고 싶었는데, 게임이론과 TFT에 대해 찾아보다 쓸데없이 시간이 많이 뺏겼다ㅠ)

동환이는 시작회의때 내가 말했던 방향대로 상대방이 이전에 낸 수를 통해 나쁜 사람인지(토끼와 뱀을 좋아하는), 착한 사람인지(사슴을 좋아하는) 판단하여 값을 내리는 코드를 짰다. 나와 동환이의 코드를 대결한 결과 동환이가 이겼고, (단순히 사슴만 내거나 토끼만 내거나 랜덤으로 내는)다른 참가자도 추가한 결과 내 코드가 이기기도 했다.



두 코드를 합친 결과 아래와 같았다. 회의를 하다보니 시간이 얼마 남지 않았기 때문에 동환이 코드에다 마지막라운드에선 무조건 배신, 이전 기록이 없을땐 TFT로 한다는 점을 끼워 넣었다.

```python
seoul2_2_arr = [3] * 10
seoul2_2_pre = -1
def dong(opp, turn, opp_prev, opp_last_pattern) :
    global seoul2_2_pre, seoul2_2_arr
    seoul2_2_arr[turn-1] = opp_prev

    # 이전 대전 기록이 없으면 TFT

    is_prev = True
    if -1 in opp_last_pattern[0]:
        is_prev = False
        if turn == 0:
            return 0
        
        if opp == 0 or opp == 1 or opp == 2:
            return opp
        else:
            return 0

    # 이전 대전 기록이 있을 떄

    # 마지막 라운드는 무조건 배신
    elif turn == 9:
        if opp == 2:
            return 1
        else:
            return 2
    # 토끼만 내는 사람이면 뱀, 토끼 번갈아
    elif opp_last_pattern[0].count(1) == 10:
        cards = {1:1, 0:2}
        return cards[turn%2]
    # 뱀만 내는 사람이면 뱀, 사슴 번갈아
    elif opp_last_pattern[0].count(2) == 10:
        cards = {1:0, 0:2}
        return cards[turn%2]
    else:
        prevs = opp_last_pattern + seoul2_2_arr[:turn]
        
        # 랜덤으로 낸다고 생각되면 뱀 사슴 번갈아 내기
        arrr = [prevs.count(0), prevs.count(1), prevs.count(2)]
        turns = 10 + turn
        chk3 = 0
        chk2 = 0
        for c in arrr:
            if c >= (3 / turns * 10):
                chk3 += 1
            elif c >= (2 / turns * 2):
                chk2 += 1
        if chk3 == 3 or (chk3 == 2 and chk2 == 1):
            cards = {1:1, 0:2}
            return cards[turn%2]

        deer = prevs.count(0) / (turn+11)
        rabbit = prevs.count(1) / (turn+11)
        snake = prevs.count(2) / (turn+11)
        result = max(deer, rabbit, snake)
        if result == snake:
            if seoul2_2_pre == 2:
                seoul2_2_pre = 0
                return 0
            else:
                seoul2_2_pre = 2
                return 2
        elif result == rabbit:
            if seoul2_2_pre == 1:
                seoul2_2_pre = 2
                return 2
            else:
                seoul2_2_pre = 1
                return 1
        else:
            return 0
```

마지막 제출 기한 몇분을 남기고 코드를 합치는데 문제가 생겼고, 그냥 내 코드를 제출하게 되었다. 차라리 동환이 코드를 제출했어야 했는데, 너무 미안했다... 나중에 검토를 할 수록 합친 코드 보다도 동환이 코드가 매우 좋아보였기 때문이다.

