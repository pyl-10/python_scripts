import json

"""如果用户存储过用户名,就加载它"""
# 否则,就提示用户输入用户名并存储它

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        print(username)
        tf_username = input("y/n")
        if tf_username == 'y':
            return username
        else:
            return get_new_username()

def get_new_username():
    username = input('请输入你的名字: ')
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print('welcome back ,' + username)
    else:
        username = get_new_username()
        print(username)

greet_user()