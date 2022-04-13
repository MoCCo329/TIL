## Forign Key, Customizing authentication in Django

### 1. Foreign Key란

- 외래 키(외부 키)이며, 관계형 DB에서 한 테이블의 필드 중 다른 테이블의 행을 식별할 수 있는 키이다.
- 참조하는 테이블에서 속성(필드)에 해당하고, 참조되는 테이블의 기본키(Primary Key)를 가리킨다.

- 외래 키의 값이 반드시 부모 테이블의 기본 키일 필요는 없지만 유일한 값이여야 한다.



### 2. Foreign Key를 포함하는 모델 작성

```python
# articles/models.py

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    context = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content
```

- 보통 1:N에서 모델의 이름은 참조되는 모델의 단수형 소문자로 작성한다.

- on_delete : 외래 키가 참조하는 객체가 사라졌을 때 외래키를 가진 객체를 어떻게 처리할 지를 정의한다. 데이터 무결성을 위해 중요한 설정이며 6개의 옵션을 가진다.

  CASCADE : 부모 객체가 삭제 됐을 때 이를 참조하는 객체도 삭제한다.

  PROTEXT

  SET_NULL

  SET_DEFAULT

  SET()

  DO_NOTHING

  RESTRICT

- 데이터 무결성

  1. 개체 무결성(Entity integrity) : 모든 테이블이 PK를 가져야 하며 PK로 선택된 열은 고유해야 한다.

  1. 참조 무결성(Referential integrity) : FK 값이 데이터베이스의 특정 테이블의 PK값을 참조하는 것.
  2. 범위 무결성(Domain integrity) : 정의된 형식에서 관계형 데이터베이스의 모든 컬럼이 선언되도록 규정.



### 3. ORM 이용해 댓글 달아보기

```shell
article = Article.object.create(title='title', content='content')  # 참조될 객체 생성


comment = Comment()
comment.content = 'first comment'  # 이 상태에서 .save()하면 NOT NULL 에러 발생
comment.article_id = article.pk  # comment.article = article 와 같으며 이를 권장
comment.save()


comment.pk
# 1
comment.content
# 'first comment'

comment.article
# <ArticleL: title>
comment.article.pk
# 1
comment.article.content
# 'content'
```

