from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL="sqlite:///./todosapp.db" 
password="Pace@321"
SQLALCHEMY_DATABASE_URL="mysql+pymysql://root:Pace%40321@localhost/TodoApplicationDB" 

# engine=create_engine(SQLALCHEMY_DATABASE_URL,connect_args={'check_same_thread':False})
engine=create_engine(SQLALCHEMY_DATABASE_URL)
sessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()




