# T = int(input())
# for tc in range(1, T+1):
#     up = ['www', 'www', 'www']
#     down = ['yyy', 'yyy', 'yyy']
#     front = ['rrr', 'rrr', 'rrr']
#     reat = ['ooo', 'ooo', 'ooo']
#     left = ['ggg', 'ggg', 'ggg']
#     right = ['bbb', 'bbb', 'bbb']
#     N = int(input())
#     turns = list(input().split())


# 윗면 u, 아랫면 d, 앞면 f, 뒷면 b, 왼쪽면 l, 오른쪽면 r   + 이면 시계, - 이면 반시계
# 흰색 w 노란색 y 빨간색 r 오렌지색 o 초록색 g 파란색 b

# turn = {'U+': , 'U-': , 'D+': , 'D-': .'F+': , 'F-': , 'B+': , 'B-': , 'L+': , 'L-': , 'R+': , 'R-': }
# -는 +를 세번 반복하면 된다.
#
#
# 위를 돌리면 위의 방향과 앞뒤왼오의 1행 방향이 바뀐다.
# 아래를 돌리면 아래의 방향과 앞뒤왼오의 3행 방향이 바뀐다.
#
# 앞을 돌리면 앞의 방향과 위의 3행 아래의 1행 왼쪽의 3열 오른쪽의 1열 방향이 바뀐다.
# 뒤를 돌리면 위의 1행 아래의 3행 왼쪽의 1열 오른쪽의 3열 방향이 바뀐다.
#
# 왼쪽을 돌리면 위의 1열 아래의 1열 앞쪽의 1열 뒤쪽의 3열이 바뀐다
# 오른쪽을 돌리면 위의 3열 아래의 3열 앞쪽의 3열 뒤쪽의 1열이 바뀐다.


# right = ['gbb', 'gbb', 'gbb']
def face_switch(face):  # 면을 시계방향으로 돌리는 함수
    temp = [[face[i][j] for i in range(2,-1,-1)] for j in range(3)]
    return temp

# face_switch(right)