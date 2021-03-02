import sys
import os
import time

'''
手动编写一个daemon进程
'''

def daemonize(stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
    try:

        # 创建子进程
        pid = os.fork()

        if pid > 0:
            # 父进程先于子进程exit，会使子进程变为孤儿进程
            # 这样子进程成功被init这个用户级守护进程收养
            sys.exit(0)

    except OSError as err:
        sys.stderr.write('_Fork #1 failed: {0}\n'.format(err))
        sys.exit(1)

    # 从父进程环境脱离
    # decouple from parent environment
    # chdir 确认进程不占用任何目录， 否则不能umount
    os.chdir('/')
    # 调用umask（0）拥有写任何文件的权限，避免继承自父进程的umask被修改导致自身权限不足
    os.umask(0)
    # setsid调用成功后，进程成为新的会话组长和新的进程组长，并在原来的登录会话和进程组脱离
    os.setsid()

    # 第二次fork
    try:
        pid = os.fork()

def test():
    sys.stdout.write()
    while True:
        now = time.strftime()
        sys.stdout.write()
        sys.stdout.flush()
        time.sleep(1)


if __name__=='__main__':
    daemonize('/dev/null','/Users/edz/Downloads/demo/d1.log','/dev/null')
    test()