## git

### 1. git 저장소 만들기

```bash
$ git init
Initialized empty Git repository in C:/Users/K/Desktop/startcamp/first/.git/
```

- .git 폴더가 생성 => 버전이 기록되는 저장소
  - 해당 폴더를 지우게 되면 모든 버전이 삭제되니 주의!

- (master) 라는 브렌치가 표시된다. 

- 만약 git 이용이 처음이라면 이름과 이메일을 등록하라는 메시지가 뜬다.

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

<br>

### 2. 버전 기록하기

- Working Directory - Staging Area - Local Repository - Remote Repository 의 단계가 있다.

- add

  add는 Working Directory 에서 Staging Area로 작업 내용을 선별하는 것이다.

  ```bash
  git add 파일명
  git add a.txt
  git add my_folder/
  git add a.txt b.txt
  ```

- commit

  커밋은 Staging Area에서 Local Repository로 작업 내용을 저장하는 것이다.

  커밋 메시지는 항상 버전의 내용(변경사항)에 대해서 나타낼 수 있도록 기록한다.

  ```bash
  git commit -m '커밋메시지'
  ```

- git init : 해당 위치에서 git을 처음 실행

- git status : Working Directory 와 Stating area의 내용이 표시

  ```bash
  $ git status
  # 다음 세가지 사항들을 보여준다
  
  # 커밋할 변경사항들 (staging area) (staging area)
  # 커밋을 위해 준비되지 않은 변경사항 (staging area x => working directory)
  # 트래킹 되지 않은 파일들 (working directory)
  ```

- git log : 커밋한 해쉬값, 작가, 날짜 등이 표시된다

  - git log --oneline : 커밋된 주소와 이름 나열
  - git log -1 : log 의 첫번째 해쉬값, 작자, 날짜 등 정보를 보여준다.

  ```bash
  git log
  # repository에 저장된 목록을 보여준다
  ```

- git commit --amend : 최근 커밋한 것을 다시 현재상태로 커밋한다. -m '메시지' 를 추가해 커밋메시지를 바꿀 수 있다. 커밋 해시값이(SHA-1에 의해 만들어진) 달라진다

<br>

### 3. 파일 변경사항 상태

- untracked : 커밋에 포함된 적 없는 파일
- tracked
  - modified : 커밋에 비해서 수정된 경우
  - staged : 커밋 되기 전 목록 (staging area)
  - commited : 커밋된 상태

<br>

### 4. 원격 저장소 활용(GitHub)

#### 1. 조회

```bash
$ git remote -v
origin  https://github.com/MoCCo329/first.git (fetch)
origin  https://github.com/MoCCo329/first.git (push)
```

#### 2. 추가

```bash
$ git remote add <원격저장소이름> <url>
$ git remote add origin https://github.com/username/repository.git
```

- origin : 일반적으로 많이 활용되는 원격저장소 이름

#### 3. 삭제

```bash
$ git remote rm <원격저장소이름>
```



#### 4. 원격 저장소 push

> Update remote refs along with associated objects (commit)

```bash
$ git push <원격저장소이름> <브랜치이름>
$ git push origin master
```

#### 5. 원격 저장소 pull

> fetch from and integrate(merge) with another repository or a local branch

```bash
$ git pull <원격저장소이름> <브랜치이름>
$ git pull orgin master
```

#### 6. 원격 저장소 clone

> Clone a repository into a new directory

```bash
$ git clone <원격저장소주소>
$ git clone https://github.com/username/repository.git
```

<br>

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

<br>

### 5. merge

1. fast-forward: 가지가 생성된 후 master가 변하지 않아 master가 브렌치와 병합되며 나아간다.

2. 3-way merge(merge commit): 가지가 생성된 후 master가 변한경우 진행된다.

3. rebase merge: sub branch의 시작지점을 master의 최근위치로 이동시키고 merge 하는 것이다.

   ```bash
   git rebase master(중심 브랜치명)
   ```

4. squash & merge: 서브브랜치의 커밋기록을 없애고 merge commit 하나만 남기는 방법이다.

   ```bash
   git merge --squash (서브브랜치)
   ```

<br>

### 6. git undoing things

- git restore:

  git restore <파일명>: 해당 파일을 최근 커밋됐던 상태로 되돌린다.

  - git restore --souce <커밋아이디> <파일명>: 해당 커밋상태로 파일의 상태를 변경
  - git restore --staged <파일명>: staging을 취소시킨다. 만약 커밋이 없는 파일을 staging area 에서 working directory로 옮기려면 git rm --cached <파일명>을 사용한다.


- git reset

  git reset [옵션] \<커밋 ID\> : 특정 커밋상태로 되돌아가며, 해당 커밋 이후로 쌓아놨던 커밋들은 전부 사라진다.   이후 커밋과 관련된 파일들은 아래 세가지 옵션에 따라 상태가 달라진다. (git reflog를 통해 이전 모든 log값을 확인할 수 있으며, git reset --hard 옵션을 통해 지워진 커밋상태로 돌아갈 수 있다.)

  1. --soft 옵션의 경우 돌아간 커밋 이후의 커밋내용들은 staging area로 올려놓는다.
  2. --mixed 옵션은 돌아가려는 커밋으로 되돌아가고, 이후 커밋된 파일들은 working directory로 돌려놓는다.
  3. --hard 옵션은 돌아가려는 커밋으로 되돌아가고, 이후 커밋된 파일들은 전부 삭제된다.

- git revert: 이전 커밋을 취소하며 새롭게 커밋하기

  git revert \<커밋 ID\> :  특정사건을 없었던 일로 만드는 행위로, 이전 커밋을 취소하는 새로운 커밋을 만든다. head가 나아가며 커밋되고, git history가 유지되기 때문에 git reset과 다르다.

- 커밋 내용 수정하기

  git commit --amend : 마지막 커밋 직후에 수정사항이 없으면 커밋메시지만 수정한다. staging area에 새로 올라온 내용이 있다면 이전 커밋을 취소하고 다시 덮어서 커밋한다.

  명령어 입력시 vim이 뜨면 i 를 눌러서 입력상태로 바꿀 수 있다. 입력상태에서 메시지를 바꾼 뒤 esc누르고 :wq로 저장하여 돌아오면 커밋 메시지만 변경된다. 새로운 커밋으로 재정의 되므로 커밋해쉬값도 달라진다.

  커밋 내용까지 수정하는경우 원하는 내용을 add 한 뒤 git commit --amend 명령을 친다. 이 후 :wq를 친 후 복귀하면 역시 새로운 수정된 커밋이 된다.

<br>

### 8. git stash

- git stash는 작업한 내용을 임시로 저장시키고 working directory, staging area는 이전 커밋 상태로 깨끗이 만드는 것이다.
- git stash save 'message': 작업중이던 내용을 메시지와 함께 임시저장시킨다.
- git stash list: stash 기록을 보여준다,
- git stash pop: 최근 stash 기록을 불러와 적용시킨다.
- git stash drop 0: git stash list 시 0번으로 나오는 stash 기록을 지운다.
- git stash clear: stash기록을 모두 지운다.

<br>

### 7. Git workflow

- Feature Branch Workflow(shared repository model) 저장소의 소유권이 있는 경우
  1. 팀원이 작업 후 푸시한다.
  2. pull request를 작성한다.
  3. 여러 사람과 해당 커밋에 대해 의견을 남기거나 비교 가능하다.
  4. 팀장이 Murge pull request하여 master branch에 합친다.

- Forking Workflow(Fork & Pull model) 저장소의 소유권이 없는 경우

  1. Fork 후 포크한 저장소를 clone한다.

  2. 추후 로컬 저장소를 원본 원격 저장소와 동기화하기 위해 URL을 연결한다.

     ```bash
     git remote add upstream URL
     ```

  3. 작업 후 포크 저장소에 push하고 원본 저장소에 pull request한다.

  4. 요청을 승인받은 후 로컬 저장소에서 git pull upstream master 한다.

