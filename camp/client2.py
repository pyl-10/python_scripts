import socket

# AF_INET IPv4 地址， SOCK_STREAM TCP协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# debug
print(f"s1: {s}")

s.connect(('www.httpbin.org', 80))

# debug
print(f"s2: {s}")

# 发送http头部信息
s.send(b'GET / HTTP/1.1\r\nHOST:time.geekbang.org\r\nConnection: close\n\r\n')

buffer = []

while True:
    data = s.recv(1024) # recv()方法 接收服务器返回的内容，参数是每次接收多少字符的内容
    if data:
        buffer.append(data)
    else:
        break

s.close()

response = b''.join(buffer)

header, html = response.split(b'\r\n\r\n', 1)

print(header.decode('utf-8'))

with open('index.html','wb') as f:
    f.write(html)
