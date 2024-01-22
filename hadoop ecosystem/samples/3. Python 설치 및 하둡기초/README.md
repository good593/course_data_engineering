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
# 파이썬 설치 
```shell
# 파이썬 설치 
sudo apt-get install -y python3-pip
pip3 install --upgrade pip
# 버전 확인 
python3 --version
```
---
![Alt text](./img/image.png)

---
# master > 하둡 실행 
```shell
# 실행
. cluster-start-all.sh
# 확인 
jps
```
---
![Alt text](./img/image-1.png)

---
# [1. hadoop 명령어](./1.%20hadoop%20명령어.md)

---
# [2. yarn 명령어](./2.%20yarn%20명령어.md)

---
# [3. mapreduce](./3.%20mapreduce.md)

---
# master > 하둡 정지 
```shell
# 정지
. cluster-stop-all.sh
# 확인 
jps
```
---
![Alt text](./img/image-23.png)







