from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# SQL_ALCHEMY_DATABASE_URL = 'mysql+pymysql://root:Root-1234567890@localhost/fast_api'
SQL_ALCHEMY_DATABASE_URL = f'mysql+pymysql://{settings.database_username}:{settings.database_password}' \
                           f'@{settings.database_hostname}/{settings.database_name}'

engine = create_engine(SQL_ALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

# connection_fast_api_db = pymysql.connect(host='localhost',
#                                            user='root',
#                                            password='Root-1234567890',
#                                            database='fast_api',
#                                            cursorclass=pymysql.cursors.DictCursor)
# class ModelName(str, Enum):
#     alexnet = "alexnetttt"
#     resnet = "resnetttt"
#     lenet = "lenetttt"

#
# my_posts = [{"title":"title of post1", "content": "content of post 1", "id": 1}, { "title":"favorite foods",
#                                                                                    "content":"I like pizza",
#                                                                                    "id":2}]
# @app.get("/sqlalchemy")
# def test_posts(db:Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     return {"data":posts}


# @app.get("/items/{item_id}")
# async def items(item_id:int):
#     return {"message": item_id}
#
# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}
#
#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}
#
#     return {"model_name": model_name, "message": "Have some residuals"}