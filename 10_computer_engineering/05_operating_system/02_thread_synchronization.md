# 02. Thread Synchronization

<br>

## 1. 스레드 동기화

- 실행 순서 동기화 : 스레드의 실행 순서를 정의하고 이 순서를 반드시 따르도록 하는 것
- 메모리 접근에 대한 동기화
  - 메모리 접근에 있어서 동시 접근을 막는 것
  - 실행의 순서가 중요한 것이 아니라 한 순간에 하나의 스레드만 해당 자원에 접근하도록 하는 것

- 동기화 기법
  - 사용자 수준의 동기화
    - 커널의 힘을 빌리지 않고 사용자가 만든 라이브러리를 사용해서 스레드를 운용하는 동기화 기법으로 커널의 코드가 실행되지 않음
    - 성능상 이점이 있으나 기능상의 제한점이 존재
    - 속도는 빠르지만 구현이 어려움
    - 임계 구역 기반의 동기화, 인터락 함수 기반의 동기화
  - 커널 모드의 동기화
    - 커널에서 제공하는 동기화 기능을 이용하는 방법
    - 커널 모드로의 변경이 필요하고 이는 성능 저하로 이어진다. 그러나 다양한 기능을 활용할 수 있다.
    - 구현은 쉽지만 속도가 느림
    - 세마포어, 뮤텍스, 모니터 등

<br>

## 2. 임계 영역

- 둘 이상의 스레드가 동시에 접근해서는 안 되는 공유 자원을 접근하는 코드의 일부
- 임계 영역에서 동기화를 진행하지 못하면 치명적인 문제 발생
- 임계 영역 문제 해결하기 위한 3가지 필수 조건
  - 상호 배제 : 특정 프로세스가 공유 자원을 사용하고 있을 경우 다른 프로세스가 해당 공유 자원을 사용하지 못하게 제어하는 기법
  - 진행 : 임계 구역에서 실행중인 프로세스가 없고 별도의 동작이 없는 프로세스들만 임계 구역 진입 후보로서 참여될 수 있다.
  - 한정된 대기 : 임계 구역에 진입 신청 후부터 받아들여질때까지, 다른 프로세스들이 임계 구역에 진입하는 횟수는 제한이 있어야 한다.

<br>

## 3. 세마포어, 뮤텍스

### (1) 세마포어(Semaphore)

- 공유된 자원의 데이터를 여러 프로세스, 스레드가 접근하는 것을 막는 것
- 동시에 접근할 수 있는 '허용 가능한 갯수'를 가지고 있는 Counter가 있다.(공유자원에 접근할 수 있는 스레드 혹은 프로세스의 수를 나타내는 값. -> 공통으로 관리하는 하나의 값)
- 세마포어는 소유할 수 없다.
  - 세마포어를 소유하지 않은 스레드가 세마포어를 해제할 수 있는 문제가 발생할 수 있기 때문
- 화장실 예시
  - 화장실이 3칸이 있고 열쇠가 3개라면 3명까지 대기없이 바로 사용할 수 있지만 그 다음부터는 한 명 이상 화장실에서 나올 때까지 대기해야 한다.
  - 이 때 세마포어는 1개 이상의 열쇠라고 할 수 있다.

<br>

### (2) 뮤텍스(Mutex)

- 공유된 자원의 데이터를 여러 프로세스, 스레드가 접근하는 것을 막는 것
- 상호 배제라고도 하며 특정 프로세스가 공유 자원을 사용하고 있을 경우 다른 프로세스가 해당 공유 자원을 사용하지 못하게 제어하는 기법이다.
- 임계 구역을 가진 스레드들의 running time이 서로 겹치지 않게 각각 단독으로 실행되게 하는 기술
- 뮤텍스 객체를 두 스레드가 동시에 사용할 수 없다.
- Lock에 대한 소유권이 있으며 Lock을 가지고 있을 경우에만 공유 자원에 접근할 수 있고, Lock을 가진 사람만 반납할 수 있다.
- 화장실 예시
  - 뮤텍스는 무조건 1개의 열쇠만 가질 수 있다. 즉, 열쇠를 가진 사람만이 화장실에 갈 수 있고, 다음 사람이 화장실에 가기 위해서는 앞 사람이 화장실에서 나온 후 열쇠를 반납해야 한다.

<br>

## :exclamation: 세마포어 VS 뮤텍스 차이

- 동기화 대상 갯수
  - 세마포어: 동기화 대상이 하나 이상일 때 사용
  - 뮤텍스: 동기화 대상이 오직 하나뿐일 때 사용
- 세마포어는 뮤텍스가 될 수 있지만 뮤텍스는 세마포어가 될 수 없다.
  - 뮤텍스는 상태가 0 ,1 두 개 뿐인 binary semaphore이기 때문
- 세마포어는 소유할 수 없는 반면, 뮤텍스는 소유가 가능하며 소유주가 이에 대한 책임을 가진다.
  - 뮤텍스의 경우 상태가 두개 뿐인 lock 이므로 lock 을 가질 수 있다.

<br>

---

:book: <b>Reference</b>

- https://m.blog.naver.com/PostView.nhn?blogId=smuoon4680&logNo=50127179815&proxyReferer=https:%2F%2Fwww.google.co.kr%2F
- [https://github.com/wally-wally/Ready-For-Tech-Interview/blob/master/Operating%20System/%EB%8F%99%EA%B8%B0%ED%99%94%20%EB%AC%B8%EC%A0%9C.md](https://github.com/wally-wally/Ready-For-Tech-Interview/blob/master/Operating System/동기화 문제.md)
- https://worthpreading.tistory.com/90