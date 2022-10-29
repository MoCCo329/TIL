| 파일명      | 링크                     |
| ----------- | ------------------------ |
| 1. sql 기본 | [링크1](./1.sql_기본.md) |
| 2. sql 활용 | [링크2](./2.sql_활용.md) |





### cf or Not Classified Yet

- count(*) 는 전체 행의 수 카운트, null 을 포함한다

  count(칼럼명) 은 null을 제외한 행 수를 카운트한다.

- DISTINCT 는 NULL도 단일 행으로 본다

- NULL 은 모르는 값을 상징하고, 값이 없음을 의미한다.

  NULL IS NULL = TRUE

  NULL 과의 모든 비교는 알 수 없음(NULL)을 반환한다.

  NULL 과 0이나 공백' '은 동일하지 않다

- 숫자는 varchar2, char에 입력 가능하며 그럴 경우 숫자로 조회 가능하다.

- DELETE에서 FROM 생략 가능하다.

- WITH tablename AS (SELECT ~) 을 통해 임시테이블이나 뷰처럼 사용 가능하다.

- 서브쿼리는 SELECT문 내에 SELECT문이 또 쓰여있는 쿼리를 말하며 인라인뷰는 서브쿼리가 FROM 절 내에 쓰여진 것이다.

- 통계적 집계함수의 연산은 NULL을 제외하고 계산한다.

- 조회되는 행 수를 제한할 때 ORACLE은 WHERE 절 뒤에 ROWNUM =을, MySQL은 LIMIT를, SQL Server는 TOP()을 사용한다.

- 서브쿼리는 ORDER BY를 사용할 수 없다. 의미가 없다.

- 인덱스는 내림차순으로 생성 및 정렬된다. 실행계획에 따라 성능이 달라지지 결과는 동일하다.