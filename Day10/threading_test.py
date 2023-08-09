
import threading
import multiprocessing
import time

# 定义一个线程的执行函数
def thread_function(name):
    print("Thread {} started".format(name))
    time.sleep(2)  # 模拟线程执行的耗时操作
    print("Thread {} finished".format(name))

# 创建两个线程
thread1 = threading.Thread(target=thread_function, args=(1,))
thread2 = threading.Thread(target=thread_function, args=(2,))

# 启动线程
thread1.start()
thread2.start()

# 等待线程结束
thread1.join()
thread2.join()

print("All threads finished")


# 定义一个进程的执行函数
def process_function(name):
    print("Process {} started".format(name))
    time.sleep(2)  # 模拟进程执行的耗时操作
    print("Process {} finished".format(name))

if __name__ == "__main__":
    # 创建两个进程
    process1 = multiprocessing.Process(target=process_function, args=(1,))
    process2 = multiprocessing.Process(target=process_function, args=(2,))

    # 启动进程
    process1.start()
    process2.start()

    # 等待进程结束
    process1.join()
    process2.join()

    print("All processes finished")


def coroutine_example():
    while True:
        x = yield  # 接收发送的值，并将控制权返回给调用者
        print(f"Received: {x}")

# 创建协程对象
coroutine = coroutine_example()

# 启动协程
next(coroutine)

# 发送值给协程
coroutine.send(10)
coroutine.send("Hello")
    