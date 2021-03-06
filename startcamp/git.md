## git

### 1. git 저장소 만들기

```bash
$ git init
Initialized empty Git repository in C:/Users/K/Desktop/startcamp/first/.git/
```

- .git 폴더가 생성 => 버전이 기록되는 저장소
  - 해당 폴더를 지우게 되면 모든 버전이 삭제되니 주의!

- (master) 라는 브렌치가 표시된다. 



```bash
git commit -m 'First commit'
Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'K@DESKTOP-ID0QM00.(none)')
```

git config --global user.email "이메일주소"

git config --global user.name "닉네임"

으로 사용자 설정 후 다시 커밋

```bash
$ git commit -m 'First commit'
[master (root-commit) ec44a2f] First commit
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 a.txt
```



### 2. 버전 기록하기

<img src='./git.assets/화면 캡처 2022-01-27 033034-16432218519371.png' alt='git의 이해'>

#### add

```bash
git add 파일명
git add a.txt
git add my_folder/
git add a.txt b.txt
```



#### commit

```bash
git commit -m '커밋메시지'
```

* 커밋 메시지는 항상 버전의 내용(변경사항)에 대해서 나타낼 수 있도록 기록한다.



git init : 해당 위치에서 git을 처음 실행

git status : W.D 와 Stating area의 내용이 표시

git log : 커밋한 해쉬값, 작가, 날짜 등이 표시된다

git log --oneline : 커밋된 주소와 이름 나열

git log -1 : log 의 첫번째 해쉬값, 작자, 날짜 등 정보를 보여준다.

git commit --amend : 최근 커밋한 것을 다시 현재상태로 커밋한다. -m '메시지' 를 추가해 커밋메시지를 바꿀 수 있다. 커밋 해시값이(SHA-1에 의해 만들어진) 달라진다



#### status

```bash
$ git status
# 다음 세가지 사항들을 보여준다

# 커밋할 변경사항들 (staging area) (staging area)

# 커밋을 위해 준비되지 않은 변경사항 (staging area x => working directory)

# 트래킹 되지 않은 파일들 (working directory)
```



#### log

```bash
git log
# repository에 저장된 목록을 보여준다
```



#### git에서 관리하는 파일 변경사항 상태

- untracked : 커밋에 포함된 적 없는 파일
- tracked
  - modified : 커밋에 비해서 수정된 경우
  - staged : 커밋 되기 전 목록 (staging area)
  - commited : 커밋된 상태



#### 기타 내용

- 파일을 조작하는 방법 4가지

  - 생성 Create

  - ~~읽기 Read~~

  - 수정 Update

  - 삭제 Delete

- 관리중인 파일의 이름이나 경로 바꿔도 되지만(상위폴더 변경사항은 저장X), 다른 깃 관리 폴더에 들어가면 곤란, 커밋된 변경사항은 파일이 지워져도 복원가능, but 커밋되지 않으면 불가능.

- fetch vs pull
  - fetch : 받아오기만 하며, 로컬에 영향을 미치지 않는다.
  - pull : fetch + merge 받아온 내용을 로컬에 병합한다.



### 3. 원격 저장소 활용(GitHub)

#### 조회

```bash
$ git remote -v
origin  https://github.com/MoCCo329/first.git (fetch)
origin  https://github.com/MoCCo329/first.git (push)
```

#### 추가

```bash
$ git remote add <원격저장소이름> <url>
$ git remote add origin https://github.com/username/repository.git
```

- origin : 일반적으로 많이 활용되는 원격저장소 이름

#### 삭제

```bash
$ git remote rm <원격저장소이름>
```



#### 원격 저장소 push

> Update remote refs along with associated objects (commit)

```bash
$ git push <원격저장소이름> <브랜치이름>
$ git push origin master
```

#### 원격 저장소 pull

> fetch from and integrate with another repository or a local branch

```bash
$ git pull <원격저장소이름> <브랜치이름>
$ git pull orgin master
```

#### 원격 저장소 clone

> Clone a repository into a new directory

```bash
$ git clone <원격저장소주소>
$ git clone https://github.com/username/repository.git
```



```bash
# git bash 눌렀을 때 vscode가 안뜨면
$ git config --global core.editor "code --wait"
$ git config --global -l
$ git config --global user.email "kd8317@gmail.com"
$ git config --global user.name "MoCCo329"
```



로컬 저장소와 원격 저장소의 커밋 히스토리가 달라 오류가 생기면(원격에서 커밋충돌시)

git pull origin master를 하고 vs코드창이나 vim 이 뜨는데 이 창을 종류하면 커밋이 된다.(merge message)

이후 다시 push한다. but 동일한 파일이 수정되었으면 충돌발생



### 4. git branch

```bash
# 브랜치 상태 표시 (--oneline과 --all 등의 순서는 상관 없다.)
git log --oneline # head가 가리키는 브렌치의 버젼만 보이게 된다.
git log --oneline --all # 모든 브렌치가 보이게 된다. 하지만 가지를 정확히 파악하기엔 힘들다.
git log --oneline --all --graph # 가지를 표현해서 그래프처럼 보여준다.

# 브렌치 목록 확인
git branch

# 새로운 브랜치를 생성
git branch 브랜치이름

# 특정 브렌치 삭제
git branch -d 브렌치이름 # 병합된 브렌치만 삭제가능
git branch -D 브렌치이름 # 강제 삭제

# 다른 브렌치로 이동
git switch 브렌치이름
git switch -c 브렌치이름 # 브렌치 생성과 동시에 이동

# 병합 (병합 후엔 브렌치를 삭제한다)
git merge 병합할 브렌치이름 # merge하기 전에 합치려는 메인 브렌치로 swich해야 한다.
```



- 파일이 staging area로 올리지 않으면 브렌치가 바뀌더라도 해당 파일은 생성된 브렌치에만 남는것이 아니라 따라오게 된다.

- 가지를 병합하는 방식에는 세가지 경우가 존재한다.

1. fast-forward : 가지가 생성된 후 master가 변하지 않아 master가 브렌치와 병합되며 나아간다.

2. 3-way merge(merge commit) : 가지가 생성된 후 master가 변했지만, 가지와 겹치는 부분이 변하지 않아 알아서 합병되는 경우이다.
3. merge conflict : 병합시 충돌이 발생한 경우. merge하는 두 브랜치에서 같은 파일의 같은 부분을 통시에 수정하고 merge하면 git은 해당 부분을 자동으로 merge 해주지 못한다.

- merge confilct 충돌 해결 방법

  충돌부분을 해결한 뒤 별도 메시지 없이 커밋(git commit)하면 vim이 실행된다. vim은 입력모드와 명령모드가 있는데, esc를 눌러 명령모드로 바꾸고 :wq를 적으면 저장 후 나오게 된다.

- checkout은 switch와 restore를 수행하는 이전 명령어이다.

```bash
# 브렌치 이동
git checkout 브랜치명
git switch 브랜치명

# 브렌치 생성 및 이동
git checkout -b 브랜치명
git switch -c 브랜치명

# unstaged 상태의 변경(modified) 파일을 복구
git checkout -- REAEME.md
git restore README.md
```

