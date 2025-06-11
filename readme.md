```
flask에서는  Post방식은
새로고침이나 페이지를 열면 success=True가 남아있다
단순히 랜더링한다고 생각 이전 정보를 그대로 사용
```
# PRG 패턴
```
Post -> Redirect -> Get
Post 요청 처리후 사용자를 리다이렉트 시켜서 GET 요청으로 바꿔줌
```