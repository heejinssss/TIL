# 0112 : TIL(TODAY I LEARNED)

<aside>
👩🏻‍💻 git : **분산** 버전 관리 프로그램
github : git으로 관리되는 프로젝트, 폴더(directory) * GitHub Copilot

</aside>

- 절대경로 : 루트 디렉토리부터 목적 지점까지 거치는 모든 경로를 전부 작성
  - 윈도우 바탕화면의 절대 경로 C:\Users\ssafy\Desktop
- 상대경로 : 현재 작업하고 있는 디렉토리를 기준으로 계산된 상대적 위치 작성
  - 현재 작업 중인 디렉토리 C:/Users
  - 윈도우 바탕화면으로의 상대 경로 ssafy/Desktop
- ./ : 현재 작업중인 폴더
- ../ : 현재 작업중인 폴더의 상위 폴더

## ⭐ GIT

- git : **분산** 버전 관리 프로그램
- github : git으로 관리되는 프로젝트, 폴더(directory) * GitHub Copilot

## ⭐ MARKDOWN

- MarkDown : Github 문서의 시작과 끝
  - [README.md](http://readme.md/) 파일을 통해 오픈 소스의 공식 문서 작성
  - 개인 프로젝트의 소개 문서 작성
  - 매일 학습한 내용 정리
  - 마크다운을 이용한 블로그 운영
  - Obsidian, Notion
  - **문서의 구조를 위한 작업일 뿐, 디자인을 위한 작업이 아님**
  - [참고 사이트](https://www.markdownguide.org/cheat-sheet/)

```c
$ git init // .git = git에서 관리 중 (루트 디렉토리에서는 절대 금지)

// 파일 탐색
$ find . -name "000"

// 명령어
$ mkdir / cd
$ ls -a / -l
$ rm -r
```

1. **Working Directory**
  - 내가 작업하고 있는 실제 디렉토리
  - 초기 상태값 : [untracked] or [tracked + up to date]
  - `git add` → **Staging Area**에서 파일 관리 가능
2. **Staging Area**
  - 커밋(commit)으로 남기고 싶은, 특정 버전으로 관리하고 싶은 파일이 있는 곳
  - 예시 : *로그인* 기능 완성 파일, *로그아웃* 기능 미완성 파일
  - `git commit` → **Repository**에서 파일 관리 가능
3. **Repository (Local / Remote)**
  - 커밋(commit)들이 저장되는 곳 → W.D.의 파일 상태값 [modified]
  - github web에서의 커밋(commit)은 지향!

```bash
$ git init
$ git add 000
$ git status # 중요
$ git commit -m '000'

$ git log --oneline
>> d47d9b3 (HEAD -> master) 3rd commit # d47d9b3 : 고유값(아이디)
>> 28d58f6 2nd commit
>> 6f5ea6d initial commit

$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage) # commit을 원하지 않는 경우
        modified:   README.md

$ git remote add origin https://github.com/heejinssss/TIL.git
$ git remote -v
>> origin  https://github.com/heejinssss/TIL.git (fetch) // download
>> origin  https://github.com/heejinssss/TIL.git (push) // upload

$ git push (-u) origin master # remote repo와 연결
# Shift + Insert : 깔끔하게 paste
```

🤩 **git** 시작하기

- **Local Repository**
  
  1. 초기화 : `git init`으로 git local repository 초기화
    - `git init` 후 반드시 `git add`
  2. `git add` : Staging Area로 버전 관리 할 파일 옮기기
    - `git add .` : 현재 위치한 W.D.에 생긴 모든 변화 사항을 옮기기
    - `git add {filename}` : 파일을 지정해서 옮기기
  3. `git commit -m 'message'` : 해당 버전이 어떤 목적으로 생성되었는가를 입력 (길이 제한)
- **Remote Repository**
  
  1. 레포지토리 연결하기 : `git remote add origin {remote_repo URL}`
  2. `git push origin master` : Local → Remote로 (upload)
    - 인증 : Remote Repository에 push할 권한 확인
- 파일 상태
  
  1. 최초 생성 시 : *untracked*
  2. `git add` 후 : *staged*
  3. `git commit` 후 : *tracked*
  4. 파일의 수정 사항이 있을 경우 : *modified*
  5. 최신 파일일 경우 : *up-to-date*