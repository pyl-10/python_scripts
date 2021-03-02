from sqlalchemy import DateTime
from datetime import datetime
import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

# 打开数据库连接
Base =declarative_base()

class Book_table(Base):
    __tablename__ = "bookorm"
    book_id = Column(Integer(), primary_key=True)
    book_name = Column(String(50), index=True)

# 定义一个更多的列属性的类
class Author_table(Base):
    __tablename__ = 'authororm'
    user_id = Column(Integer(), primary_key=True)
    username = Column(String(15), nullable=False, unique=True)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)


# 实现一个引擎
dburl = "mysql+pymysql://root:@localhost/testdb"
engine = create_engine(dburl, echo=True, encoding="utf-8")
Base.metadata.create_all(engine)