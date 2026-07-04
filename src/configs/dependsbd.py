from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import db




def session():
    try:
        s= sessionmaker(bind=db)
        Session= s()
        yield Session

    except:
        Session.rollback()
        
    finally:
        Session.close()