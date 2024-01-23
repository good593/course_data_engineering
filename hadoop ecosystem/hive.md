---
style: |
  img {
    display: block;
    float: none;
    margin-left: auto;
    margin-right: auto;
  }
marp: true
paginate: true
---
# [Hive](https://spidyweb.tistory.com/238)
- 하둡 기반의 데이터웨어하우징용 솔루션 
- 페이스북에서 만든 오픈소스로, SQL과 매우 유사한 HiveQL이라는 쿼리를 제공한다. 
- HiveQL은 내부적으로 MapReduce 잡으로 변환되어 실행된다.

---
## Hive 구성요소 
![Alt text](./img/hive/image.png)

---
- UI
    - 사용자가 쿼리 및 기타 작업을 시스템에 제출하는 사용자 인터페이스
    - CLI, Beeline, JDBC 등
- Driver
    - 쿼리를 입력받고 작업을 처리
    - 사용자 세션을 구현하고, JDBC/ODBC 인터페이스 API 제공
- Compiler
    - 메타 스토어를 참고하여 쿼리 구문을 분석하고 실행계획을 생성
- Metastore
    - 디비, 테이블, 파티션의 정보를 저장
- Execution Engine
    - 컴파일러에 의해 생성된 실행 계획을 실행
---
## Hive 실행순서 
1. 사용자가 제출한 SQL문을 드라이버가 컴파일러에 요청하여 메타스토어의 정보를 이용해 처리에 적합한 형태로 컴파일
2. 컴파일된 SQL을 실행엔진으로 실행
3. 리소스 매니저가 클러스터의 자원을 적절히 활용하여 실행
4. 실행 중 사용하는 원천데이터는 HDFS등의 저장장치를 이용
5. 실행결과를 사용자에게 반환



