import pymysql
from sqlalchemy import create_engine, Table, Integer, String, MetaData, ForeignKey
from sqlalchemy.sql.schema import Column

# 打开数据库连接
engine = create_engine('mysql+pymysql://root:@localhost/testdb', echo=True)

# 创建元连接
metadata = MetaData(engine)

book_table = Table('book', metadata,
            Column('id', Integer, primary_key=True),
            Column('name', String(20)),
)

author_table = Table('author', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('book_id', ForeignKey('book.id')),
                    Column('author_name', String(128), nullable=False),
                    )

try:
    metadata.create_all()
except Exception as e:
    print(f'create error {e}')
