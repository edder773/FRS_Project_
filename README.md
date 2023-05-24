# FRS_Project(금융 추천 서비스)

> 금융 API를 사용하여 사용자에게 맞춤형 예금, 적금을 추천해주는 사이트
>
> 금융 API와 사용자에게 받은 데이터를 토대로, 사용자와 비슷한 데이터를 가진 다른 사람들이 자주 가입하는 상품을 추천하거나
> 간단한 미니게임을 통해 사용자에게 상품을 추천해주는 알고리즘 구현

## 개발 기간
> 2023.05.17 ~ 23.05.25

## 📌 시작 전 확인 사항
### ✔️ Front-end
> Front를 실행하기 위해 필요한 패키지들의 설치
```
$ cd Front/frs-Front/
$ npm install
$ npm install bootstrap-vue
$ npm install axios
```

### ✔️ Back-end
> Back을 실행하기 위해 필요한 패키지들의 설치
```
$ cd Back/frs_back/
$ python -m vevn venv
$ source venv/Script/activcate
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
```

## 1. 📂 개요

### 1-1 팀원 설명
김보석 : Front-end & Back-end
- Vue 클라이언트 구현
- Django 서버 구현
- Vue - django 연동
- css 모델링

박승희 : Front-end
- Vue 클라이언트 구현
- Css 모델링
- Web Design

### 1-2 주요 기능
> 시작 페이지
```
1. 메인 화면생성
2. 로그인 여부에 따른 NavBar 표시 변경
```
<br>

> 로그인 & 회원가입
```
1. 회원 가입 시 사전 정보 선택적 입력
2. 로그인 여부 토큰을 통해 확인
```
<br>

> 예금 & 적금 조회 서비스
```
1. 시중 은행의 예금 & 적금 상품 리스트 조회
2. 가입 기간에 따른 금리 정보 제공
3. 예금 & 적금 추천 알고리즘 페이지 제공
4. 상품 클릭 시 해당 은행 위치 서비스 제공 (카카오 API)
5. 즐겨찾기 버튼을 통해 상품능저장 가능
```
<br>

> 예금 & 적금 추천 알고리즘
```
1. 2가지의 추천 서비스 제공
2. 다른 사용자들의 정보와 사용자의 사전 입력 정보를 통한 추천 서비스
3. 미니게임을 통한 사용자 맞춤 서비스 제공
```
<br>

> 커뮤니티
```
1. 자유롭게 토론할 수 있는 자유 게시판 기능 제공
2. 게시판 별 댓글 기능 제공
3. 자주 묻는 질문 게시판 제공
4. 1:1 문의 게시판 제공
```
<br>

> 환율 계산기
```
1. 현재 환율에 따른 원하는 나라의 환율 금액 계산
2. 환율 서비스 제공을 위해 환율 API 사용
```
<br>

> 은행 지도
```
1. 원하는 지역의 은행 위치 검색 서비스 제공
2. 선택 박스를 통해 위치 선택 가능
```
<br>

> 개인 프로필 페이지
```
1. 사용자의 정보 조회
2. 선택적 정보에 대한 정보 수정 기능 제공
3. 사용자가 즐겨찾기로 선택한 상품 확인 가능
```
<br>

### 1-3 컴포넌트 구조

### 1-4 ERD model

# 2. 추천 알고리즘
![recommend](https://github.com/edder773/FRS_Project_/assets/58801719/b4ad6c9f-8b61-4580-9d57-a0d363209cc2)

> 예금 정보 비교 탭에서 알고리즘 추천 버튼을 통해 2개의 추천 서비스 이용 가능 구현
> 2개의 추천 서비스 모두 사용자의 제공 정보 기반 추천 알고리즘

### 2-1 나와 비슷한 조건을 가진 다른 사람들이 선택한 상품 추천 알고리즘
![recommend2](https://github.com/edder773/FRS_Project_/assets/58801719/ff534200-6011-478a-b9de-46f86bec5a22)

> - 사용자가 사전에 입력한 나이, 연봉, 자산을 근거로 나와 가까운 범위를 가진 사람의 데이터를 추출
> - django에서 기본으로 제공하는 Q 사용
> - 사용자의 사전 데이터를 기반으로 분류하므로, 나이, 연봉, 자산 등의 

```
similar_users = User.objects.filter(
        Q(age__range=(age_min, age_max)) &
        Q(annual_income__range=(income_min, income_max)) &
        Q(assets__range=(assets_min, assets_max)) &
        ~Q(id=current_user.id)
```


### 2-2 사용자의 선택을 기반으로 한 상품 추천 알고리즘

