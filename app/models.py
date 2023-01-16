from sqlalchemy.orm import relationship

from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, BINARY, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
class Post(Base):
    __tablename__="posts"
    id = Column(Integer, primary_key = True, nullable=False)
    title = Column(String(50),nullable=False)
    content = Column(String(50),nullable=False)
    published = Column(Boolean, default=True,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    rating = Column(Integer,nullable=True)
    owner_id=Column(Integer,ForeignKey("users.id",ondelete="NO ACTION"),nullable=False)
    owner = relationship("User")

class User(Base):
    __tablename__ = "users"
    id=Column(Integer,primary_key = True, nullable = False)
    email = Column(String(50),nullable=False,unique = True)
    password= Column(String(60),nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    phone_number = Column(String[15])

class Vote(Base):
    __tablename__ = "votes"
    user_id= Column(Integer,ForeignKey("users.id", ondelete="NO ACTION"),primary_key = True)
    post_id= Column(Integer,ForeignKey("posts.id", ondelete="NO ACTION"),primary_key = True)
