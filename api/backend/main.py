# FAST API의 메인 서버
from fastapi import FastAPI,HTTPException,Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from model import Base, User
from database import SessionLocal,engin
# Fast api 생성
app = FastAPI()
# 앱을 실행하면 DB에 정의된 모든 테이블을 생성
Base.metadata.create_all(bind=engin)

def get_db():
    db = SessionLocal()  # 새션 객체  생성
    try:
        yield db # 종속된 함수에 세션 주입
    finally:
        db.close()  # 요청이 끝나면 자동으로 세션 종료
# 회원가입용 데이터타입  pydantic 
class RegisterRequest(BaseModel):
    username: str
    email: str
    passowrd: str

# 라우터(요청에 응답하는)
@app.post('/api/register')
def register_user(user: RegisterRequest, db:Session=Depends(get_db)):
    # 같은 사용자가 있는지 조회
    existing_user =  db.query(User).filter(User.username == user.username).first()
    # 같은 사용자가 있으면  400에러로 응답
    if existing_user:
        raise HTTPException(status_code=400, detail="이미 존재하는 사용자입니다.")
    # 새 유저에대한 객체(인스턴스) 생성성
    new_user =  User(
        username = user.username,
        email = user.email,
        password = user.passowrd
    )
    # db commit하는 과정과 동일
    db.add(new_user)
    db.commit()
    db.refresh(new_user)  # DB에서 자동 생성된 id를 유저인스턴스에 할당
    return {"success":True,'message':'회원가입 성공', 'user_id':new_user.id}
