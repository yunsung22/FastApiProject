from pydantic import BaseSettings

class Settings(BaseSettings):
    userid: str = 'abc123'
    passwd: str = 'abc123'
    dbname: str = 'abc123'
    dburl: str = 'abc123'
    dbconn: str = f'sqlite:///app/{dbname}'

config = Settings()