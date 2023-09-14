from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI

####################################################################
SQLALCHEMY_DATABASE_URL = 'sqlite:///sql_app.db'
# SQLALCHEMY_DATABASE_URL = 'postgresql:///user:password@postgresserver/db'
engine = create_engine(SQLALCHEMY_DATABASE_URL, 
                       connect_args={"check_same_thread": False})


Base = declarative_base()


class Person(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)

# Base.metadata.create_all(engine)
####################################################################

SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()

# Tom = Person(name='Tom', age=46)
# Tom2 = Person(name='Tom', age=56)
# db.add_all([Tom, Tom2])
# db.commit()
# db.refresh(Tom)

# peoples = db.query(Person).filter(Person.age > 30).first()
# db.delete(peoples)
# db.commit()
# print(f'{peoples.id}')
# for people in peoples:
#     # if people.age > 30:
#     print(f'{people.id}. {people.name} ({people.age})')

####################################################################

app = FastAPI()


@app.get('/user/{user_id}')
def get_user(user_id: int):
    user = db.query(Person).filter(Person.id == user_id).first()
    return {"id": user.id,
            "name": user.name,
            "age": user.age
            }


@app.post('/user')
def add_user(name: str, age: int):
    try:
        user = Person(name=name, age=age)
        db.add(user)
        db.commit()
        db.refresh(user)
        return {"id": user.id,
                "name": user.name,
                "age": user.age
                }
    except:
        db.rollback()
        return {"Response": "Error!"}
