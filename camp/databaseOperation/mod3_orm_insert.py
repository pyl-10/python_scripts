from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy.orm.session import Session

# 打开数据库连接
Base = declarative_base()

class Book_table(Base):
    __tablename__ = "bookorm"
    book_id = Column(Integer(), primary_key=True)
    book_name = Column(String(50), index=True)

    def __repr__(self) -> str:
        return "Book_table(book_id='{self.book_id}', book_name={self.book_name}".format(self=self)

class Author_table(Base):
    __tablename__ = "authororm"
    user_id = Column(Integer(), primary_key=True)
    username = Column(String(15), nullable=False, unique=True)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

# 实例一个引擎
dburl = "mysql+pymysql://root:@localhost/testdb"
engine = create_engine(dburl, echo=True, encoding="utf-8")

# 创建session
SessionClass = sessionmaker(bind=engine)
session = SessionClass()

# 增加数据
book_demo = Book_table(book_name="肖申克的救赎")
author_demo = Author_table()
print(book_demo)
print(author_demo)
session.add(book_demo)
session.commit()
res = session.query(Book_table).all()
print(res)
session.commit()

# 业务逻辑层  业务类，实例化的对象
# 持久层
# 数据库层
