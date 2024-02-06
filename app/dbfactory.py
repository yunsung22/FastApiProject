from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.settings import config

engine = create_engine(config.db_conn, echo=True, connect_args={'check_same_thread':False})
Session = sessionmaker(autocommit=False, autoflush=False, bind=False)

