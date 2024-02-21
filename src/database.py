from sqlalchemy import create_engine, text
from .config import setting

engine = create_engine(
    url = setting.database_url_psycopg,
    echo=True,
    #pool_size=5,
    #max_overflow=10
)

def test_db():
    with engine.connect() as conn:
        res = conn.execute(text("SELECT VERSION();"))
        print(f"{res.first()=}")
