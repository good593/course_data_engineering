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
### 단계1: [이미지 다운로드](https://releases.ubuntu.com/focal/)
![Alt text](./img/image.png)

---
### 단계2: 새로 만들기 
![Alt text](./img/image-1.png)

---
### 단계3: 가상 머신 이름과 운영 체제 
- 이름: ubuntu_base
- ISO 이미지: 다운로드한 우분투 이미지
- 무인 설치 건너뛰기 
![Alt text](./img/image-2.png)

---
### 단계4: 하드웨어 
- 수정하지 않음  
![Alt text](./img/image-3.png)

---
### 단계5: 가상 하드 디스크 
- 30GB로 수정 
![Alt text](./img/image-4.png)

---
### 단계6: (완료) 만들기
![Alt text](./img/image-5.png)

---
### 단계7: 시작하기 
![Alt text](./img/image-6.png)

---
### 단계9: install ubuntu
![Alt text](./img/image-7.png)

---
![Alt text](./img/image-8.png)

---
![Alt text](./img/image-9.png)

---
![Alt text](./img/image-10.png)

---
![Alt text](./img/image-11.png)

---
![Alt text](./img/image-12.png)

---
- 사용자 계정 생성
![Alt text](./img/image-13.png)

---
- 설치 완료 후 재실행
![Alt text](./img/image-14.png)

---
- ubuntu 접속 
![Alt text](./img/image-15.png)

---
### 단계10: [Virtual Box 게스트 확장 프로그램 설치](https://sidepower.tistory.com/43) 
![Alt text](./img/image-16.png)

---
### 단계11: [클립보드 설정](https://sidepower.tistory.com/61)
![Alt text](./img/image-17.png)

---
- 재기동 
![w:800](./img/image-18.png)
- 마우스 오른쪽 클릭 > Paste(붙여넣기)가 활성화 됨 
![Alt text](./img/image-19.png)

---
### 단계12: 필수 라이브러리 설치 
- 필수 라이브러리
  - `vim` : 텍스트 편집기 
  - `wget` : 웹 서버로부터 파일 다운로드
  - `unzip` : 파일 압축/해제
  - `ssh / openssh-*` : 리눅스 원격 접속
  - `net-tools` : 네트워크 툴
```shell
# 업데이트 목록 갱신
sudo apt-get -y update
# 현재 패키지 업그레이드 
sudo apt-get -y upgrade
# 신규 업데이트 설치 
sudo apt-get -y dist-upgrade
# 필수 라이브러리 설치 
sudo apt-get install -y vim wget unzip ssh openssh-* net-tools
```
---
### 단계13: ssh 실행 
```shell
sudo service ssh start
# ssh 실행 확인 
systemctl status sshd
```

---
### 단계14: Java 8 설치 
```shell
# Java 8 설치 
sudo apt-get install -y openjdk-8-jdk
# Java version 확인 
java -version
# Java 경로 확인 
readlink -f $(which java) # /usr/lib/jvm/java-8-openjdk-amd64
```
![Alt text](./img/image-20.png)

---
- 환경설정 
```shell
# 수정 
sudo vim ~/.bashrc

# 아래내용 입력 
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export PATH=$PATH:$JAVA_HOME/bin

# 적용
source ~/.bashrc
env | grep java # 확인  
```
![Alt text](./img/image-21.png)

---
### 단계15: Apache Hadoop 다운로드  
```shell
# 설치파일 관리용 디렉토리 생성
sudo mkdir /install_dir && cd /install_dir
# 다운로드 
sudo wget https://archive.apache.org/dist/hadoop/core/hadoop-3.3.0/hadoop-3.3.0.tar.gz
# 확인 
ls
```
![Alt text](./img/image-22.png)

---
### 단계16: python3 설치 & pip upgrade
```shell
sudo apt-get install -y python3-pip
sudo pip3 install --upgrade pip
```
### 단계17: Python 환경설정 
```shell
sudo vim ~/.bashrc
# 아래 내용 복사 
export PYTHONPATH=/usr/bin/python3
export PYSPARK_PYTHON=/usr/bin/python3
export PATH=$PATH:/usr/bin/python3

# 수정내용 반영 
source ~/.bashrc
env | grep python3
```
---
### 단계18: Spark 다운로드 
```shell
# 설치 관리용 디렉토리 이동
cd /install_dir
# Spark 3.2.1 설치
sudo wget https://archive.apache.org/dist/spark/spark-3.2.1/spark-3.2.1-bin-hadoop3.2.tgz
```

### 단계19: Zookeeper 설치
```shell
# 설치 관리용 디렉토리 이동
cd /install_dir
# Zookeeper 3.8.0 설치
sudo wget https://archive.apache.org/dist/zookeeper/zookeeper-3.8.0/apache-zookeeper-3.8.0-bin.tar.gz

```
