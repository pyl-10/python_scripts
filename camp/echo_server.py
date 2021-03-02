import socket

HOST = 'localhost'
PORT = 10000

def echo_server():
    """
    echo server 的 server 端
    """
    # 创建新的socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 将对象 s 绑定到指定的主机和端口上
    s.bind((HOST, PORT))
    # 允许socket接收连接，且只接受一个连接
    s.listen(1)
    while True:
        # accept 表示等待接受用户端的连接
        conn, addr = s.accept()
        # 输出客户端的地址
        print(f'Connected by {addr}')
        while True:
            # 读取客户端发送的内容
            data = conn.recv(1024)
            if not data:
                break
            # 回送消息响应
            conn.sendall(data)
        conn.close()
    # 关闭连接
    s.close()

if __name__ == '__main__':
    echo_server()