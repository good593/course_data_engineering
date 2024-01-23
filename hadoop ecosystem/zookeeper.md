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
# [Zookeeper](https://xangmin.tistory.com/169) 
분산 코디네이션 서비스를 제공하는 오픈소스 프로젝트로 직접 어플리케이션 작업을 조율하는 것을 쉽게 개발할 수 있도록 도와주는 도구이다.
1. 하나의 서버에만 서비스가 집중되지 않도록 서비스를 알맞게 분산하여 동시에 처리하게 해줌
2. 하나의 서버에서 처리한 결과를 다른 서버들과도 동기화 -> 데이터 안정성 보장
3. 운영(active) 서버에서 문제가 발생해 서비스를 제공할 수 없는 경우, 다른 대기중인 서버를 운영 서버로 바꿔 서비스가 중지없이 제공되게 해줌
4. 분산 환경을 구성하는 서버들의 환경설정을 통합적으로 관리
---
## 분산 코디네이션 서비스
- 분산 시스템에서 시스템 간의 정보 공유, 상태 체크, 서버들 간의 동기화를 위한 락 등을 처리해주는 서비스
![Alt text](./img/zookeeper/image.png)

---
## Znode
- 주키퍼가 상태 성보를 저장하는 곳
- `Persistent Node` : 영구 저장소
- `Ephermeral Node` : Client가 종료되면 사라진다.
- `Sequence Node` : 생성 시 뒤에 숫자가 붙는다.
![Alt text](./img/zookeeper/image-1.png)

---
## Quorum
- Leader가 새로운 트랜잭션을 수행하기 위해서는 자신을 포함하여 과반수 이상의 서버의 합의를 얻어야 한다. 과반수의 합의를 위해 필요한 서버들을 Quorum이라고 한다.
![Alt text](./img/zookeeper/image-2.png)


