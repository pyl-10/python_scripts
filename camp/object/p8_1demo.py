# ORM (flask.ext.sqlalchemy)
# 一个表记录一个节点的心跳更新
# 通过一个属性来获取节点是否可用，而不用写复杂的查询语句

class Node(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    updated_at = db.Column(db.DateTime) # 节点最后心跳时间
    state = db.Column(db.Integer, nullable=False) # 节点是否禁用

    @property
    def is_active(self):
        if(datetime.datetime.now() - self.updated_at).secondes > 60 and self.vm_state == 0:
            return False
        return True

# 限制传入的类型和范围 （整数，且满足 18-65）
class Age(object):
    def __init__(self, default_age = 18) -> None:
        self.age_range = range(18, 66)
        self.default_age = default_age
        self.data = {}

    def __get__(self, instance, owner):
        return self.data.get(instance, self.default_age)

    def __set__(self, isinstance, value):
        if value not in self.age_range:
            raise ValueError('must be in (18-65)')

        self.data[isinstance] = value

class Student(object):
    age = Age()

if __name__ == "__main__":
    s1 = Student()
    s1.age = 30
    s1.age = 100