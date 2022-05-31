months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

def solution(choice, movies):
    new_movies = []

    # movie를 [score, date, title]형태로 저장하며 제목이 중복되는 경우 개봉일이 빠른 영화만 담기
    for movie in movies:
        # 개봉일
        date = 0
        for month in range(1, int(movie[:2]) + 1):
            date += months[month]
        date += int(movie[3:5])

        # 평점
        score = float(movie[-3:])

        # 제목
        title = movie[5:-3].strip().replace(" ", "").lower()

        # new_movies에 넣기
        i = 0
        while i < len(new_movies):
            if new_movies[i][2] == title:
                if new_movies[i][1] <= date:
                    break
                else:
                    new_movies.pop(i)
                    new_movies.append([score, date, title])
                    break
            else:
                i += 1
        else:
            new_movies.append([score, date, title])
    
    # score 내림차순으로, title는 오름차순으로(a보다 b가 더 크다) 나열
    new_movies.sort(key=lambda x: (-x[0], x[2]))

    # choice의 date를 계산해서 movie date와 비교
    choice_date = 0
    for month in range(1, int(choice[:2]) + 1):
        choice_date += months[month]
    choice_date += int(choice[3:5])

    answer = []
    for limit in [7, 14]:
        for movie in new_movies:
            score, date, title = movie
            if abs(choice_date - date) <= limit:
                answer.append(title)
        # 만약 7일 전후로 영화 개수가 3개를 넘지 않으면 limit을 14로 늘린다
        if len(answer) >= 3:
            return answer[:3]
        else:
            answer = []

    if len(answer) >= 3:
        return answer[:3]
    else:
        return []

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    choice = input()
    movies = []
    for _ in range(N):
        movies.append(input())
    print(f'#{tc} {solution(choice, movies)}')