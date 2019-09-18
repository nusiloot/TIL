# [SSAFY]Django_#2(written by wally-wally)

----

**※참고사항※**

- `[SSAFY]Django_#2`은 정규과정 `Django`을 진행하면서 강의파일에 없는 추가적인 내용이나 중요하게 다루었던 내용을 상세하게 작성했음.
- 최대한 수업 시간의 모든 내용을 담으려했으나 없는 내용이 있을 수도 있음.

------

<br>

## 5. 9월11일(05일차)

### 5.1 Django Modeling, Migrations 주의사항

- Modeling

```python
class Articles(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 기본값
    updated_at = models.DateTimeField(auto_now=True) # 기본값

    def __str__(self):
        return self.title
```

- migrations  과정

```bash
[1] python manage.py makemigrations
```

```bash
[optional과정] python manage.py sqlmigrate articles 0001

# 단순히 확인하는 과정
BEGIN;
--
-- Create model Articles
--
CREATE TABLE "articles_articles" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(20) NOT NULL, "content" text NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL);
COMMIT;
```

```bash
[2]python manage.py migrate => 테이블 실질적으로 만드는 과정
```

```bash
[3]python manage.py createsuperuser => 테이블 생성 후 슈퍼유저 생성하기
```

:warning: 만약에 migrations 과정 중 중간에 실수(`admin.py` 잘못 작성하는 것)하면 migratinos 폴더 내에 있는 파이썬 파일과 생성된 `db.sqlite3` 을 지우고 다시 처음부터 수행한다.

<br>

### 5.2 git 응용 <a href="https://github.com/wally-wally/TIL/blob/master/00_startcamp/README_divide/00_startcamp_day02.md#22-git의-특징-및-작업-흐름">:rocket:(Go to git basic)</a>

#### (1) git branch의 특징

- branch는 나뭇가지의 비유적 표현을 가져온 것이다.
- master는 유지한 채 새로운 branch를 만들어서 다른 사용자가 수정할 수 있다.

- 매우 가볍다.
- 순식간에 branch를 만들고 branch 사이를 이동할 수 있다.
- git이 가지고 온 혁신 중 하나는 branch 기능을 매우 쓸 만한 수준까지 만들었다는 것이다.

<br>

#### (2) git branch 사용

---

:heavy_check_mark: 사전 준비 : `master` 상태에서 `touch a.txt`, `touch b.txt`로 파일 먼저 생성

```bash
student@DESKTOP MINGW64 ~/Desktop/git_branch
$ git init
Initialized empty Git repository in C:/Users/student/Desktop/git_branch/.git/

student@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ git branch

student@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ touch a.txt

student@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ touch b.txt

student@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ ls
a.txt  b.txt

student@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        a.txt
        b.txt

nothing added to commit but untracked files present (use "git add" to track)

student@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ git add .

student@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ git commit -m "first commit"
[master (root-commit) a60972a] first commit
 2 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 a.txt
 create mode 100644 b.txt

student@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ git log
commit a60972accc54169981ef6729e473745869e19900 (HEAD -> master)
Author: wally-wally <wallys0213@gmail.com>
Date:   Wed Sep 11 11:44:46 2019 +0900

    first commit
```

---

- `git branch` : branch 목록 확인
  - 초록색으로 현재 있는 위치를 알 수 있음
- `git branch 이름명` : 이름명으로 branch 생성(ex. `git branch ssafy`)

- `git checkout 이름명` : 이름명 branch로 이동(ex. `git checkout ssafy`)

- branch명이 `ssafy`인 상태에서 `touch c.txt`로 파일 생성 후 commit 후 다시 `master`로 돌아가면...
  - `master` 상태 : `a.txt`, `b.txt`만 보임
  - `ssafy` 상태 : `c.txt`도 같이 보임

```bash
student@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ ls
a.txt  b.txt

student@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ git checkout ssafy
Switched to branch 'ssafy'

student@DESKTOP MINGW64 ~/Desktop/git_branch (ssafy)
$ ls
a.txt  b.txt  c.txt
```

- branch를 지우고 싶으면 `master`로 돌아가서 수행한다.

```bash
student@DESKTOP MINGW64 ~/Desktop/git_branch (ssafy)
$ git checkout master
Switched to branch 'master'

student@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ git branch -d ssafy
error: The branch 'ssafy' is not fully merged.
If you are sure you want to delete it, run 'git branch -D ssafy'. # 병합 안했는데 진짜로 지울래? 그러면 대문자 D로 쳐!

student@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ git branch -D ssafy
Deleted branch ssafy (was 580d458).

student@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ git branch
* master
```

- `git checkout -b branch_name` : `git branch branch_name` + `git checkout branch_name` 두 명령어를 하나로 명령할 때(앞으론 이 한 줄로 작성하자)

<br>

#### (3) git merge

- `git merge branch_name` : 병합(merge)은 `master` 에서 수행하자

**:heavy_check_mark: merge(병합)가 되는 상황**

**① Fast-forward**

```bash
student@DESKTOP MINGW64 ~/Desktop/git_branch (feature/test)
$ touch test.txt

student@DESKTOP MINGW64 ~/Desktop/git_branch (feature/test)
$ git add .

student@DESKTOP MINGW64 ~/Desktop/git_branch (feature/test)
$ git commit -m "complete test.txt"
[feature/test 0c73ba2] complete test.txt
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 test.txt

student@DESKTOP MINGW64 ~/Desktop/git_branch (feature/test)
$ git checkout master
Switched to branch 'master'

student@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ git merge feature/test
Updating a60972a..0c73ba2
Fast-forward
 test.txt | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 test.txt

student@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ git log
commit 0c73ba206953949282ba9e6013e8e9340dfb1650 (HEAD -> master, feature/test)
Author: wally-wally <wallys0213@gmail.com>
Date:   Wed Sep 11 13:40:13 2019 +0900

    complete test.txt

commit a60972accc54169981ef6729e473745869e19900
Author: wally-wally <wallys0213@gmail.com>
Date:   Wed Sep 11 11:44:46 2019 +0900

    first commit
```

- log 정보가 많을 때 `git log --oneline --graph`로 입력하면 한 눈에 branch 상태를 알 수 있다.

**② Merge-commit**

```bash
student@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ git merge feature/signout
Merge made by the 'recursive' strategy.
 login.txt   | 0
 signout.txt | 0
 2 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 login.txt
 create mode 100644 signout.txt
 
# 위 커멘드 입력 후 상황에서 빠져나올 때 [Esc] 누르고 :wq 를 입력 후 [Enter] 치면 된다.

student@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ git log --oneline --graph
*   b9bf4c8 (HEAD -> master) Merge branch 'feature/signout'
|\
| * 4ea2154 (feature/signout) Complete login.txt
| * fe480fa Complete signout.txt
* | 6ec542b Make master.txt
|/
* 0c73ba2 complete test.txt
* a60972a first commit

```

**③ Merge-conflict**

- 사람이 직접 수정하는 방식

```bash
student@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ git commit -m "fix a.txt master"
[master 711e35a] fix a.txt master
 1 file changed, 1 insertion(+)

student@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ git merge feature/article
Auto-merging a.txt
CONFLICT (content): Merge conflict in a.txt
Automatic merge failed; fix conflicts and then commit the result.
```

> `a.txt`
>
> ```
> <<<<<<< HEAD
> 이건 master 가 작성한 글.
> =======
> 이건 feature/article에서 작성한 글.
> >>>>>>> feature/article
> 
> 
> 아래와 같이 수정
> 
> 이건 master 가 작성한 글.
> ```

```bash
student@DESKTOP MINGW64 ~/Desktop/git_branch (feature/article)
$ git checkout master
Switched to branch 'master'

student@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   a.txt

no changes added to commit (use "git add" and/or "git commit -a")

student@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ git add .

student@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ git commit -m "fix a.txt master"
[master 711e35a] fix a.txt master
 1 file changed, 1 insertion(+)

student@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ git merge feature/article
Auto-merging a.txt
CONFLICT (content): Merge conflict in a.txt
Automatic merge failed; fix conflicts and then commit the result.

student@DESKTOP MINGW64 ~/Desktop/git_branch (master|MERGING)
$ git add .

student@DESKTOP MINGW64 ~/Desktop/git_branch (master|MERGING)
$ git commit
[master 9897c23] Merge branch 'feature/article'

student@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ git log --oneline --graph
*   9897c23 (HEAD -> master) Merge branch 'feature/article'
|\
| * 977313c (feature/article) fix a.txt
* | 711e35a fix a.txt master
|/
*   b9bf4c8 Merge branch 'feature/signout'
|\
| * 4ea2154 Complete login.txt
| * fe480fa Complete signout.txt
* | 6ec542b Make master.txt
|/
* 0c73ba2 complete test.txt
* a60972a first commit
```

<br>

### 5.3 merge 종류

#### (1) feature branch workflow

- `Pull request`
  - 기능 개발을 끝내고 master에 바로 병합시키는게 아니라, branch를 중앙 원격 저장소에 올리고(push) master에 병합을 요청(merge)
  - **중앙에서 병합을 했다면, 다른 팀원들은 master branch를 pull 받아야 한다!**

#### (2) forking workflow

- git remote add upstream [중앙 원격 저장소 주소]
  - [중앙 원격 저장소 주소] : master의 원래 주소
- git remote -v
- git checkout -b feature/login
- 내용 수정 후
- git push -u origin feature/login

---

:ballot_box_with_check: Merge가 되는 상황들

**1.fast-forward**

- feature/test branch 이동

```bash
$ git checkout -b feature/test
$ (feature/test)
```

- 작업 완료 후 commit

```bash
$ touch test.md
$ git add .
$ git commit -m "Complete test.md"
```

- master 이동

```bash
$ git checkout master
$ (master)
```

- master에 병합

```bash
$ git merge feature/test
```

- 결과
  - 단순히 HEAD가 최신 commit으로 이동
  - `feature/test` branch 생성 이후 `master` branch의 이력에 변화가 없었기 때문
- branch 삭제

```bash
$ git branch -d feature/test
```

<br>

**2.megre commit**

- `feature/login` branch 이동

```bash
$ git checkout -b feature/login
```

- 작업 완료 후 commit

```bash
$ touch login.md
$ git add .
$ git commit -m "complete login.md"
```

- `master`로 이동

```bash
$ git checkout master
```

- `master`에 추가 commit 생성

```bash
$ touch master.md
$ git add .
$ git commit -m "fix master.md"
```

- `master`에 병합

```bash
$ git merge feature/login
```

- 자동으로 merge commit 발생
  - Vim 에디터로 열림
  - 메세지를 수정하고자 하면 `i`로 편집 모드 바꾼다음에 commit을 수정하고
  - `Esc` + `:wq`를 통해 저장 및 종료

```bash
Merge branch 'feature/login'

# Please enter a commit ...
...
```

- commit 그래프 확인하기

```bash
$ git log --oneline --graph
```

```bash
*   9897c23 (HEAD -> master) Merge branch 'feature/login'
|\
| * 977313c (feature/article) fix a.txt
* | 711e35a fix a.txt master
|/
*   b9bf4c8 Merge branch 'feature/signout'
|\
| * 4ea2154 Complete login.txt
| * fe480fa Complete signout.txt
* | 6ec542b Make master.txt
|/
* 0c73ba2 complete test.txt
* a60972a first commit
```

- branch 삭제

```bash
$ git branch -d feature/login
```

<br>

**3. merge comflict**

- `feature/article` branch 생성 및 이동

```bash
$ git checkout -b feature/aritcle
```

- 작업 완료 후 commit

```bash
# 충돌을 만들어 낼 파일에 코드를 작성
$ git add .
$ git commit -m "fixed minor update"
```

- `master`로 이동

```bash
$ git checkout master
```

- `master`에 추가 commit 만들기

```bash
# feature/article branch 에서 수정한 파일과 동일 파일의 같은 위치를 수정
$ git add .
$ git commit -m "fixed master update"
```

- `master`에 병합

```bash
$ git merge feature/article
```

- merge conflict 발생

```bash
$ git merge feature/article
Auto-mergin a.txt
CONFLICT ...
Automatic merge failed; fix conflicts and then commit result.
```

- 충돌 확인 및 해결

```bash
# 충돌이 일어난 파일 열기
# 그럼 아래와 같은 내용이 있다.

<<<<<<<< HEAD
master 에서 작성한 내용
========
feature/article 에서 작성한 내용
>>>>>>>> feature/article

# 원하는 코드로 수정
```

- merge commit 진행
  - 여기서는 commit 메세지는 미리 작성되어 있으므로 안 써도 된다.

```bash
$ git add .
$ git commit
```

- commit 그래프 확인

```bash
$ git log --oneline --graph

*   9897c23 (HEAD -> master) Merge branch 'feature/article'
|\
| * 977313c (feature/article) fix a.txt
* | 711e35a fix a.txt master
|/
*   b9bf4c8 Merge branch 'feature/signout'
|\
| * 4ea2154 Complete login.txt
| * fe480fa Complete signout.txt
* | 6ec542b Make master.txt
|/
* 0c73ba2 complete test.txt
* a60972a first commit
```

- branch 삭제

```bash
$ git branch -d feature/article
```

<br>

## 6. 9월18일(06일차)

### 6.1 URL Namespace

#### (1) 하드코딩 URL 제거

- `{% url %}`template tag를 사용하여 하드코딩 URL을 제거한다.

> `urls.py`
>
> - `name` 속성을 추가하여 일일히 url을 작성하는 번거로움을 줄여준다.
>
> ```django
> urlpatterns = [
>     path('', views.index, name='index'),
>     path('new/', views.new, name='new'),
>     path('create/', views.create, name='create'),
>     path('<int:pk>/', views.detail, name='detail'),
>     path('<int:pk>/delete/', views.delete, name='delete'),
>     path('<int:pk>/edit/', views.edit, name='edit'),
>     path('<int:pk>/update/', views.update, name='update'),
> ]
> ```

> `detail.html`
>
> ```django
> {% extends 'base.html' %}
> 
> {% block content %}
>   <h1 class="text-center">DETAIL</h1>
>   <h2>{{ article.pk }} 번째 글</h2>
>   <hr>
>   <p>제목: {{ article.title }}</p>
>   <p>내용: {{ article.content }}</p>
>   <p>작성 시각: {{ article.created_at }}</p>
>   <p>수정 시각: {{ article.updated_at }}</p>
>   <hr>
>   <a href="/articles/{{ article.pk }}/edit/">[EDIT]</a>
>   <a href="/articles/{{ article.pk }}/delete/">[DELETE]</a><br>
>   <a href="{% url 'index' %}">[back]</a>
> {% endblock %}
> ```

> `index.html`
>
> ```django
> {% extends 'base.html' %}
> 
> {% block content %}
>   <h1 class="text-center">Articles</h1>
>   <a href="/articles/new/">[NEW]</a>
>   <hr>
>   {% for article in articles %}
>     <p>글 번호: {{ article.pk }}</p>
>     <p>글 제목: {{ article.title }}</p>
>     <p>글 내용: {{ article.content }}</p>
>     <a href="{% url 'detail' article.pk %}">[DETAIL]</a>
>     <hr>
>   {% endfor %}
> {% endblock %}
> ```

<br>

#### (2) URL Namespace 설정

- 문제점 발생 : app이 여러 개가 되면, 단순히 url name만 가지고는 어떤 app의 url 인지 알 수 없다.

- 문제점 해결 : app의 `urls.py`에 `app_name`을 선언한다.

>`urls.py`
>
>```django
>app_name = 'articles'
>urlpatterns = [
>    path('', views.index, name='index'),
>    path('new/', views.new, name='new'),
>    path('create/', views.create, name='create'),
>    path('<int:pk>/', views.detail, name='detail'),
>    path('<int:pk>/delete/', views.delete, name='delete'),
>    path('<int:pk>/edit/', views.edit, name='edit'),
>    path('<int:pk>/update/', views.update, name='update'),
>]
>```

> `detail.html`
>
> - `{% url 'articles:edit' article.pk %}` 에서 공백으로 `'articles:edit'` 과 `article.pk`를 구분한다.
>
> ```django
> {% block content %}
>   <h1 class="text-center">DETAIL</h1>
>   <h2>{{ article.pk }} 번째 글</h2>
>   <hr>
>   <p>제목: {{ article.title }}</p>
>   <p>내용: {{ article.content }}</p>
>   <p>작성 시각: {{ article.created_at }}</p>
>   <p>수정 시각: {{ article.updated_at }}</p>
>   <hr>
>   <a href="{% url 'articles:edit' article.pk %}">[EDIT]</a>
>   <a href="{% url 'articles:delete' article.pk %}">[DELETE]</a><br>
>   <a href={% url 'articles:index' %}[back]</a>
> {% endblock %}
> ```

> `views.py`
>
> - `return redirect(f'/articles/{article.pk}/')` => `return redirect('articles:detail', article.pk)`
>
> ```python
> def create(request):
>     try: 
>         title = request.POST.get('title')
>         content = request.POST.get('content')
>         article = Article(title=title, content=content)
>         article.full_clean() # 유효성 검증
>     except ValidationError:
>         raise ValidationError('Error')
>     else:
>         article.save()
>         return redirect('articles:detail', article.pk)
> ```

<br>

### 6.2 HTTP

#### (1) HTTP의 속성

- 비연결성(Connectionless) : 클라이언트와 서버가 한 번 연결을 맺은 후, 클라이언트 요청에 대해 서버가 응답을 마치면 맺었던 연결을 끊어버리는 성질
- 무상태(Stateless) : Connectionless로 인해 서버는 클라이언트를 식별할 수가 없는데, 이를 Stateless라고 함
  - 매번 새로운 인증을 해야하는 번거로움이 발생하는데 이를 해결하기 위해 상태를 기억하는 방법 중 `쿠키`와 `세션`이 있다.

<br>

#### (2) Cookie, Session

- `쿠키(Cookie)` : 브라우저가 가지고 있는 쿠키
  - 하지만 이 쿠키는 보안에 취약한 특징이 있어 서버가 쿠키를 들고 있는 `세션` 개념이 새로 생김
  - 보통 브라우저에서 사용자 기록 삭제하는 것이 쿠키 삭제하는 것임
- `세션(Session)` : 서버가 가지고 있는 쿠키
  - 보통 회원탈퇴하는 것이 세션이 들고 있는 쿠키 삭제하는 것임

<br>

#### (3) <a href="https://developer.mozilla.org/ko/docs/Web/HTTP/Status">HTTP 응답 코드</a>

#### (4) <a href="https://developer.mozilla.org/ko/docs/Web/HTTP/Methods">HTTP Method</a>

- GET / POST / PATCH(PUT) / DELETE

- 실제로는 네 가지 메소드 중 공식적으로 GET, POST로만 사용된다.

<br>

### 6.3 URI, URL

| 구분                                 | 내용                                                         |
| ------------------------------------ | ------------------------------------------------------------ |
| URI<br>(Uniform Resource Identifier) | <ul><li>인터넷에 자원을 나타내는 유일한 주소</li><li>인터넷에서 요구되는 기본조건으로서 http에 항상 붙어다닌다.</li></ul> |
| URL<br>(Uniform Resource Locator)    | <ul><li>인터넷 상에서 자원이 어디 있는지 알려주기 위한 규약</li></ul> |
| URN<br>(Uniform Resource Name)       | <ul><li>사람이 쓰는 것이 아니고 기계 간 통신할 때 쓰는 주소이다. <a href="https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-models-tdm-urnscheme.html">(URN 예시)</a></li><li>우리가 직접 쓸 일은 없다.</li></ul> |

---

**:heavy_check_mark: [Example] URI, URL 구분하기**

- `https://www.google.com`
  - 서버 주소(URL 이면서 URI)
- `https://github.com/wally-wally/TIL/blob/master/README.md`
  - 주소(`https://github.com/`) + 디렉토리 파일의 주소(자원의 위치)(`이하 부분`)
  - URL 이면서 URI
- `https://www.google.com/search?q=삼성`
  - 주소 + 특정 문자열(query string)(`search?q=`)
  - `search` 까지가 URL + `q=삼성` 이라는 **<u>식별자가 필요</u>**하므로 URI 이지만 URL은 아니다.
- `https://getbootstrap.com/docs/4.3/components/dropdowns/#single-button`
  - `#single-button` : fragment 부분으로 페이지에서 특정 헤딩 위치로 바로 이동시켜줄 때 사용 

---

<br>

### 6.4 REST(Representational State Transfer)

#### (1) REST의 구성 및 규칙

- REST의 구성 : 자원(URI) + 행위(HTTP Method) + 표현(Representations)
- REST는 반드시 꼭 지켜야하는 것은 아니다. 프레임워크마다 달라질 수 있다.
- <font color="red"><b>REST 중심 규칙</b></font>
  - URI는 <b>정보의 자원</b>을 표현해야 한다.
  - 자원에 대한 행위는 <b>HTTP Method</b>로 표현한다.
- RESTful하게 바꾸기
  - `GET/users/1/read/`(X) => `GET/users/1/`(O) : URI에 불필요한 정보가 포함.
  - `GET/users/1/delete/`(X) => `DELETE/users/1/`(O) : URI는 자원을 표현하는데에만 중점을 둬야함
  - `GET/users/1/create/`(X) => `POST/users/1/`(O) : GET 메소드는 적절하지 않음.

<br>

#### (2) RESTful한 URL

- URL 작성 Tip : URL는 소문자를 사용, 파일 확장자는 미포함, 밑줄(_) 대신에 하이픈(-) 사용

- django에서 RESTful하게 URL 주소 확인하기
  - `pip install django-extensions` 설치
  - `settings.py`의 `INSTALLED_APPS`에 `'django_extensions,'` 추가
  - `python manage.py show_urls`

- RESTful하게 URL 바꾸기
  - <b>같은 주소로 들어가는데 GET이냐 POST 냐에 따라 행동을 다르게 할 것이다.(NEW+CREATE)</b>
  - GET `articles/create/` : 글을 작성하는 페이지로 이동
  - POST `articles/create/` : 글이 실제로 작성
  - `NoReverseMatch` 오류가 뜨면 url 주소를 다시 확인하자!

> `views.py` ( `new` 함수는 삭제 )
>
> ```python
> def create(request):
>     # CREATE 동작
>     if request.method == 'POST': 
>         title = request.POST.get('title')
>         content = request.POST.get('content')
>         article = Article(title=title, content=content)
>         article.save()
>         return redirect('articles:detail', article.pk)
>     # NEW 동작
>     else:
>         return render(request, 'articles/new.html')
> ```

> `urls.py` 에서 `new` 구문 제거

> `create.html` (`new.html`의 이름이 바뀜)
>
> - `{% url 'articles:new' %}` => `{% url 'articles:create' %}`
> - POST 방식으로 자기 자신 페이지로 보내는 것이므로 `{% url 'articles:create' %}` 이 action 구문마저 필요 없으므로 빈 칸으로 둬도 올바르게 동작한다.(`<form action="" method="POST">`)
>   - 즉, form tag에 action이 없다면 현재 머물고 있는 URL로 요청을 보낸다.
>
> ```django
> {% extends 'base.html' %}
> 
> {% block content %}
>   <h1 class="text-center">CREATE</h1>
>   <form action="{% url 'articles:create' %}" method="POST">
>     {% csrf_token %}
>     <label for="title">TITLE</label>
>     <input type="text" name="title" id="title"><br>
>     <label for="content">CONTENT</label>
>     <textarea name="content" id="content" cols="30" rows="5"></textarea><br>
>     <input type="submit" value="submit">
>   </form>
> {% endblock %}
> ```

- RESTful하게 DELETE 구문 수정

> `views.py`
>
> - POST 방식으로 올 때만 삭제할 수 있도록 구문 수정 (즉, 주소창에 직접 입력하여 지울려고 하면 GET 방식으로 삭제할 수 없다.)
>
> ```python
> def delete(request, pk):
>     article = Article.objects.get(pk=pk)
>     if request.method == 'POST':
>         article.delete()
>         return redirect('articles:index')
>     else:
>         return redirect('articles:detail', article.pk)
> ```

> `detail.html`
>
> ```django
> {% extends 'base.html' %}
> 
> {% block content %}
>   <h1 class="text-center">DETAIL</h1>
>   <h2>{{ article.pk }} 번째 글</h2>
>   <hr>
>   <p>제목: {{ article.title }}</p>
>   <p>내용: {{ article.content }}</p>
>   <p>작성 시각: {{ article.created_at }}</p>
>   <p>수정 시각: {{ article.updated_at }}</p>
>   <hr>
>   <a href="{% url 'articles:update' article.pk %}">[EDIT]</a>
>   {% comment %} 이렇게 쓰면 url로 삭제할 수 없게 할 수 있다. {% endcomment %}
>   <form action="{% url 'articles:delete' article.pk %}" method="POST" onclick="return confirm('진짜 지울꺼야??')">
>     {% csrf_token %}
>     <input type="submit" value="DELETE">
>   </form>
>   <a href={% url 'articles:index' %}>[back]</a>
> {% endblock %}
> ```

<br>

### 6.5 Model Instance Method

#### (1) `get_absolute_url()` <a href="https://wayhome25.github.io/django/2017/05/05/django-url-reverse/">(Go to more infomation)</a>

- 특정 모델에 대해 detail view를 작성할 경우, detail url을 완성하자마자 사용하는 것을 권장한다.
- 반복되는 코드가 줄고 보다 간결해진다.

> `models.py`
>
> - <b>`detail`에 한해서</b> 모든 url 주소는 아래와 같이 작성하면 된다.
>
> - 아래 세 구문 모두 `articles/10` 과 같이 똑같이 작동한다.
>   - `return f'/articles/{self.pk}/'`
>   - `return reverse('articles:detail', args=[self.pk])`
>   - `return reverse('articles:detail', kwargs={'pk': self.pk})`
> - reverse 함수에 args 랑 kwargs 를 동시에 인자로 보낼 수 없다.
>
> ```python
> from django.urls import reverse
> from django.db import models
> 
> class Article(models.Model):
>     title = models.CharField(max_length=20)
>     content = models.TextField()
>     created_at = models.DateTimeField(auto_now_add=True)
>     updated_at = models.DateTimeField(auto_now=True)
> 
>     def __str__(self):
>         return self.title
> 
>     def get_absolute_url(self):
>         # return f'/articles/{self.pk}/'
>         # args는 리스트로 넣는다.
>         # kwargs는 딕셔너리로 넣는다.
>         # return reverse('articles:detail', args=[self.pk])
>         return reverse('articles:detail', kwargs={'pk': self.pk})
>         # 딕셔너리의 key는 views.py의 detail 함수의 pk이다.
> ```

---

:checkered_flag: <b>URL Reverse 를 수행하는 함수들</b>

① `reverse()`

- 리턴 값 : string(문자열)

  ```python
  reverse('articles:index') # '/articles/'
  ```

② `redirect()`

- 리턴값 : HttpResponseRedirect (객체)

- 내부적으로 `resolve_url()` 을 사용

- view 함수에서 특정 url로 돌려보내고자 할 때 사용

  ```python
  redirect('articles:article')
  # <HttpResponsedRedirect status_code=200, "text/html; charset=utf-8, url="/articles/">
  ```

③ url template tag ( `{% url %}` )

- 내부적으로 `reverse()`를 사용

---

> `index.html`
>
> - `{% url 'articles:detail' article.pk %}` => `{{ article.get_absolute_url }}`
> - `redirect(모델 인스턴스)` 를 통해서 모델 인스턴스의 `get_absolute_url()` 함수를 자동으로 호출
>
> ```django
> {% extends 'base.html' %}
> 
> {% block content %}
>   <h1 class="text-center">Articles</h1>
>   <a href="{% url 'articles:create' %}">[NEW]</a>
>   {% comment %} '/articles/create/'와 같은 문자열을 뱉어냄 {% endcomment %}
>   <hr>
>   {% for article in articles %}
>     <p>글 번호: {{ article.pk }}</p>
>     <p>글 제목: {{ article.title }}</p>
>     <p>글 내용: {{ article.content }}</p>
>     <a href="{{ article.get_absolute_url }}">[DETAIL]</a>
>     <hr>
>   {% endfor %}
> {% endblock %}
> ```

> `views.py`
>
> - `'articles:detail', article.pk` => `article`
>
> ```python
> def create(request):
>     # CREATE 동작
>     if request.method == 'POST': 
>         title = request.POST.get('title')
>         content = request.POST.get('content')
>         article = Article(title=title, content=content)
>         article.save()
>         return redirect(article)
>     # NEW 동작
>     else:
>         return render(request, 'articles/create.html')
>     
>     
> def delete(request, pk):
>     article = Article.objects.get(pk=pk)
>     if request.method == 'POST':
>         article.delete()
>         return redirect('articles:index')
>     else:
>         return redirect(article)
>     
>     
> def update(request, pk):
>     article = Article.objects.get(pk=pk)
>     # UPDATE 동작
>     if request.method == 'POST':
>         article.title = request.POST.get('title')
>         article.content = request.POST.get('content')
>         article.save()
>         return redirect(article)
>     # EDIT 동작
>     else:
>         context = {'article': article,}
>         return render(request, 'articles/update.html', context)
> ```