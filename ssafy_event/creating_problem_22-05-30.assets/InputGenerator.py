import json
import random

with open('input.txt', 'a', encoding="UTF-8") as input_file: # input.txt 에 텍스트를 append하기 위해 'a' parameter 사용

    with open("./movie.json", "r", encoding="UTF-8") as json_file:
        df = json.load(json_file)
        length = len(df)
        idxs_lst = []
        testcase_num = [10, 10, 12, 12, 15, 15, 20, 20, 23, 25, 25, 30, 30, 35, 35, 40, 40, 42, 45, 45, 50, 50, 20, 55, 55, 60, 60, 65, 65, 8, 70, 70, 75, 75, 80, 80, 10, 85, 85, 90, 90, 95, 95, 100, 100] #45개의 테케들, 각각의 숫자는 N+1값
        print(len(testcase_num))
        input_file.write(f'{len(testcase_num)} \n') # 인풋 파일에 총 테케 개수 쓰기.
        for n in testcase_num: # 각 테케 당 N+1개의 랜덤 인덱스들을 생성한다.
            random_idxs = random.sample(range(length), n) 
            idxs_lst.append(random_idxs)
        for i in range(len(idxs_lst)): # idxs_lst에서 인덱스들을 가져옴.
            input_file.write(f'{len(idxs_lst[i])-1} \n') # 각 테케 당 영화 개수 N, 첫 영화는 견본 영화이므로 1을 빼준다.
            for j in range(len(idxs_lst[i])):
                date = str(df[idxs_lst[i][j]]['fields']['release_date'])[5:].replace('-', '/')
                title = (df[idxs_lst[i][j]]['fields']['title'])
                rate = str(df[idxs_lst[i][j]]['fields']['vote_average'])
                if not j: # 견본 영화는 rate가 없다.
                    input_file.write(f'{date} {title}')
                else: # 다른 영화들은 날짜, 제목, 평점 데이터를 input.txt에 기록해준다.
                    testcase = date + ' ' + title + ' ' + rate
                    input_file.write(testcase)
                input_file.write('\n') # 영화 하나 만들면 줄바꿈.
    
