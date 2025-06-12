```
기능                매서드          엔드포인트           설명


회원가입폼      get                 /api/register

회원가입        post                /api/register       사용자 정보 DB 저장

로그인          post                /api/login          사용자 인증 및 세션관리

상품목록조회    get                 /api/products       전체 상품 조회

상품등록        post                /api/products       관리자용 상품등록

장바구니 담기   post                /api/cart           사용자별 장바구니 추가

장바구니 조회   get                 /api/cart?user_id=1 특정 사용자의 장바구니 조회

주문 요청       post                /api/order          장바구니 상품 주문 처리

주문 목록 조회  get                 /api/order?user_id=1    사용자 주문 내역


```
# VSCode 에서 확장탭을 열고
```
SQLite Viewer 설치한다
```

# 가상환경  생성
```
conda create -n api python
```

# FAST API 설치
```
pip install fastapi uvicorn sqlalchemy
```

# 실행
```
main.py파일이 있는 backend 폴더로 이동해서
uvicorn main:app --reload
이후 브라우져에서
http://127.0.0.1:8000/docs  실행한다.
루트에 /docs를 하면 uvicorn에서 제공하는 swegger ui 사용
```


# 통신 규칙
```
통신        json 포멧으로 한다

인증        쿠키.세션 대신 단순 로그인 응답으로 user_id 유지(js변수에 저장)

응답메세지      {success:true, date: ..} 형식

에러처리        {success:false, error: '메세지"} 통일
```

