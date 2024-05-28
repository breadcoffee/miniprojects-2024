# 미니프로젝트 2024
IoT 개발자 과정 미니프로젝트

## 1일차
- IoT 프로젝트 개요

    ![IoT프로젝트](https://raw.githubusercontent.com/breadcoffee/miniprojects-2024/main/images/mp001.png)

    1. IoT기기 구성 - 아두이노, 라즈베리파이 등 IoT장비들과 연결
    2. 서버 구성 - IoT기기와 통신, DB구성, 데이터 수집 앱 개발
    3. 모니터링 구성 - 실시간 모니터링/제어 앱

- 조별 미니프로젝트
     - 5월 14일 ~ 28일 (40시간)
     - 구체적으로 어떤 디바이스 구성, 데이터 수집, 모니터링 계획
     - 8월말 데드라인으로 일정 계획
     - **요구사항 리스트, 기능명세, UI/UX(목업) 디자인, DB설계 등을 문서 하나**로 작성(A4 4-5장)
     - 5월 28일 오후에 조별로 10분 정도 발표

     - 요구사항 리스트(엑셀)
     - 기능명세 문서
     - DB설계 ERD 또는 SSMS 물리적 DB설계
     - UI/UX디자인(https://www.figma.com/), 목업(https://ovenapp.io/)
     - 발표자료(https://prezi.com/ko/), 미리캠퍼스(https://www.miricanvas.com)

## 2일차
- 미니 프로젝트
    - 프로젝트 문서
    - Notion 팀 프로젝트 템플릿 사용
    - UI/UX 디자인 툴 설명
        - https://ovenapp.io/ (카카오)
        - 피그마 단축키(https://www.figma.com/)
            1. V - 선택도구
            2. A - 직선도구
            3. T - 텍스트도구
            4. Space + Drag - 마우스 커서에 따라 원하는 영역으로 이동
            5. Ctrl + R - 레이어 이름 변경
            6. Ctrl + G - 객체 그룹화
            7. Ctrl + Shift + G - 객체 그룹 해제
            8. Ctrl + D - 선택한 객체 복사
            9. Ctrl + [ - 선택한 객체 뒤로 보내기
            10. Ctrl + ] - 선택한 객체 앞으로 보내기
    - 프레젠테이션
        - 미리캔버스 활용 추천
    - 라즈베리파이(RPi) 리셋팅, 네트워크 설정, VNC(OS UI작업)

- 스마트홈 연동 클래스 미니 프로젝트
    1. 요구사항 정의, 기능명세, 일정정리
    2. UI/UX 디자인
    3. DB설계
    4. RPi 셋팅
    5. RPi GPIO, IoT 디바이스 연결(카메라, 온습도센서, REB LED, ...)
    6. RPi 데이터 전송 파이썬 프로그래밍
    7. PC(Server) 데이터 수신 C# 프로그래밍
    8. 모니터링 앱 개발(수신 및 송신)

## 3일차
- 미니 프로젝트
    - 실무 프로젝트 문서(개발방법론.docx)
    - 팀프로젝트 템플릿(Jira 사용법)
    - 조별로 진행

- 라즈베리파이 셋팅
    1. RPi 기본 구성 : RPi + MicroSD + Power
    2. RPi 기본 셋팅
        - 최신 업그레이드
        - 한글화
        - 키보드 변경
        - 화면사이즈 변경(RealVNC)
        - Pi Apps 앱설치 도우미 앱
        - Github Desktop, VS Code
        - 네트워크 확인
        - RealVNC Server 자동실행 설정

- 스마트 홈 연동 클래스 미니 프로젝트
    - RPi 셋팅... 진행


## 4일차
- 라즈베리파이 IoT
    - [x] 라즈베리파이 카메라
    - [x] GPIO HAT
    - [x] 브레드보드와 연결
    - [x] DHT11 센서
    - [x] RGB LED 모듈
        - V : 5V 연결
        - R : GPIO 4번 연결
        - B : GPIO 5번 연결
        - G : GPIO 6번 연결
    - [-] 서브모터

## 5일차
- 라즈베리파이 IoT장비 설치
    - [x] DHT11 센서
        - GND : GND에 연결
        - VCC : 5V에 연결
        - S : GPIO 18번 연결

- 미니 프로젝트
    - 팀별 구매목록 작성
    - 프로젝트 결정사항 공유
    - 발표자료 준비

## 6일차
- 네트워크 세팅
    - [x] 개인공유기, PC, 라즈베리파이

## 7일차
- 스마트홈 연동 클래스 미니프로젝트
    - 온습도 센서, RGB LED
    - RPi <--> Windows 통신(MQTT)
    - WPF 모니터링 앱

- IoT 기기간 통신방법
    - Modbus : 시리얼통신으로 데이터 전송(완전 구식)
    - OPC UA : Modbus통신 불편한점 개선(아주 복잡)
    - **MQTT** : 가장 편리! AWS IoT, Azure IoT 클라우드 산업계표준으로 사용

- MQTT 통신
    - [x] Mosquitto Broker 설치
        - mosquitto.conf : listener 1883 0.0.0.0, allow_anonymous tre
        - 방화벽 인바운드 열기
    - [x] RPi : paho-mqtt 패키지 설치, 송신(publisher)
    - [ ] Win/C# : MQTT Nuget패키지 설치, 수신(subcriber)
        - M2Mqtt : 가볍게 쓸 수 있음. 업데이트가 안됨.
        - MQTTnet : MS에서 개발, 무겁다. 최신까지 업데이트 잘됨

## 9일차
- 스마트홈 연동 클래스 미니프로젝트
    - [x] WPF MQTT 데이터 DB로 저장
    - [x] MQTT 데이터 실시간 모니터링 - 온도
    - [ ] MQTT로 RPi 제어(LED제어)
    - [ ] WPF MQTT 데이터 히스토리 확인

## 10일차
- 스마트홈 연동 클래스 미니프로젝트
    - [x] WPF MQTT 데이터 DB로 저장
    - [x] MQTT 데이터 실시간 모니터링 - 습도
    - [x] MQTT로 RPi 제어(LED제어)
    - [x] WPF MQTT 데이터 히스토리 확인
        - LiveChart2는 차후에 다시, 현재는 OxyPlot 차트로 구현

    -실행결과
        ![스마트홈1](https://raw.githubusercontent.com/breadcoffee/miniprojects-2024/main/images/mp002.png)
        ![스마트홈2](https://raw.githubusercontent.com/breadcoffee/miniprojects-2024/main/images/mp003.png)
        ![스마트홈3](https://raw.githubusercontent.com/breadcoffee/miniprojects-2024/main/images/mp004.png)

- 조별 미니프로젝트 발표
    - 1~5조까지