from sqlalchemy import func
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm.session import sessionmaker

# 打开数据库连接
Base = declarative_base()

# 初始化数据库连接，修改为你的数据库用户名和密码
engine = create_engine("mysql+mysqlconnector://root:@localhost:3306/heroDB")

# 定义Player对象:
class Player(Base):
    # 表的名字:
    __tablename__ = 'player'

    # 表的结构:
    player_id = Column(Integer, primary_key=True, autoincrement=True)
    team_id = Column(Integer)
    player_name = Column(String(255))
    height = Column(Float(3, 2))

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
# 创建session对象:
session = DBSession()

# 创建Player对象:
new_player = Player(team_id=1003, player_name="约翰-科斯", height=2.15)
# 添加到session:
session.add(new_player)
# 提交即保存到数据库:
session.commit()

rows = session.query(Player).filter(Player.height >= 2.08).all()
print([row.player_name for row in rows])

# 分组查询排序
rows = session.query(Player.team_id, func.count(Player.player_id)).group_by(Player.team_id).having(
    func.count(Player.player_id) > 5).order_by(func.count(Player.player_id).asc()).all()
print(rows)

# 删除 （先查到结果再删除）
row = session.query(Player).filter(Player.player_name=="约翰-科斯").first()
session.delete(row)
session.commit()

# 修改 （先查到结果再改）
row = session.query(Player).filter(Player.player_name=="约翰史密斯").first()
row.height = 2.19
session.commit()

# 关闭session:
session.close()
