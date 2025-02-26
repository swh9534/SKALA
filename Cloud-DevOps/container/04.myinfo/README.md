# 실습 명령어

## 이미지 생성
### 1. my-info.txt 생성
$ echo "Hello! my name is yi yongwoo" > my-info.txt

### 2. docker build
$ sudo docker build --tag welcome-server:1.0 .
STEP 1/6: FROM busybox:latest
Getting image source signatures
Copying blob 9c0abc9c5bd3 done  
Copying config af47096251 done  
Writing manifest to image destination
Storing signatures
STEP 2/6: WORKDIR /app
--> 638c012286a
STEP 3/6: COPY info.txt /app/my-info.txt
--> 4c6b3e67914
STEP 4/6: COPY start.sh /app/start.sh
--> 31306cd795d
STEP 5/6: RUN chmod +x /app/start.sh
--> 4ad48e11d23
STEP 6/6: CMD ["/app/start.sh"]
COMMIT welcome-server:1.0
--> 28c7004dacf
Successfully tagged localhost/welcome-server:1.0
28c7004dacf6b32edf3daa32913ee919adeaca97739cd8abe6fc223bad2a5232

### 3. 생성된 docker 검색
sudo docker images                          
REPOSITORY                                              TAG         IMAGE ID      CREATED         SIZE
localhost/welcome-server                                1.0         28c7004dacf6  36 seconds ago  4.52 MB


## 생성된 컨테이너 실행
### 3. 생성된 docker 검색
$sudo docker images                          
REPOSITORY                                              TAG         IMAGE ID      CREATED         SIZE
localhost/welcome-server                                1.0         28c7004dacf6  36 seconds ago  4.52 MB

### 4. 나의 info 만들기
$ echo “Hello! my name is yi yongwoo” > my-info.txt   # 자신의 텍스트로 변경

# 5. Docker 실행하기
$ sudo docker run --rm -it --name welcome-server welcome-server:1.0
Container is now waiting... Press Ctrl+C to stop.

Welcome to the SKALA course. Nice to see everyone!   # info.txt 내용을 프린트


### 6. my-info.txt를 container에 마운트해서 실행하기
$ sudo docker run --rm -it --name welcome-server -v ./my-info.txt:/app/my-info.txt welcome-server:1.0
Container is now waiting... Press Ctrl+C to stop.


Hello! my name is yi yongwoo  # 변경 된 것 확인

### 7. container의 backgroup 실행
$sudo docker run --name welcome-server -v ./my-info.txt:/app/my-info.txt -d welcome-server:1.0
a3c670cc7abcb946184a2a9a9e056453febef52b5ee83c2b8e793d3deb1f453a

### 8. container에 직접 접속하기
$ sudo docker exec -it welcome-server /bin/sh  
/app # ls /app/
my-info.txt  start.sh

### 9. –v 를 통해 마운트 된 my-info.txt 확인
/app # cat /app/my-info.txt
/app # hostname
/app # exit

### 10. 실행 중인 container 종료하기
$ sudo docker stop welcome-server
$ sudo docker rm welcome-server

