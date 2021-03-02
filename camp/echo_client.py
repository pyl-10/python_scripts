import socket

# 获取IP地址和端口号
HOST = 'localhost'
PORT = 10000

def echo_client():
    """
    echo server 的 client 端
    """
    # 创建socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 连接到服务器IP：prot上去
    s.connect((HOST, PORT))

    while True:
        # 接收用户输入数据并发送给服务端
        data = input('input > ')

        # 设定退出条件
        if data == 'exit':
            break

        # 发送数据到服务端
        s.sendall(data.encode())

        # 接收服务端数据
        data = s.recv(1024)
        if not data:
            break
        else:
            print(data.decode('utf-8'))
    # 关闭连接
    s.close()

if __name__ == '__main__':
    echo_client()
