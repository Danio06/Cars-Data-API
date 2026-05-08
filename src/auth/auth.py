from fastapi import APIRouter, HTTPException, status
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from src.auth.schemas import UserCreate, UserLogin, Token

router = APIRouter(prefix="/auth", tags=["auth"])

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_user_by_email(email: str):
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("""
            SELECT id, email, hashed_password, is_active
            FROM users WHERE email = %s
            """, (email.lower(),))
            return cur.fetchone()
    finally:
        conn.close()

def create_user(email: str, hashed_password: str):
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO users (email, hashed_password, is_active)
                VALUES (%s, %s, TRUE)
                RETURNING id
            """, (email.lower(), hashed_password))
            user_id = cur.fetchone()[0]
            conn.commit()
            return user_id
    finally:
        conn.close()

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user: UserCreate):
    if get_user_by_email(user.email):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="This mail is taken"
        )

    hashed = hash_password(user.password)
    create_user(user.email, hashed)

    return {"message": "Account successfully created"}

@router.post("/login", response_model=Token)
def login(user: UserLogin):
    db_user = get_user_by_email(user.email)

    if not db_user or not verify_password(user.password, db_user[2]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email or password incorrect",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not db_user[3]:
        raise HTTPException(status_code=400, detail="Account is not active")

    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}