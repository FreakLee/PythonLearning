# Day10-网络编程、数据库编程、多线程及异步编程

## 网络编程
Python中的网络编程涵盖了多个领域，包括基本的套接字编程、网络通信、服务器端编程和客户端编程。这里简单介绍一下Python中的HTTP编程。以下是几个常用的进行 HTTP 请求的库：
* urllib：是 Python 标准库中的模块集合，提供了处理 URL 相关的功能，包括发送 HTTP 请求。
它包含了几个模块，如 urllib.request、urllib.parse 等，用于发送请求、解析 URL 等操作
* requests：这是一个第三方库，提供了更方便的HTTP请求方法，它基于urllib库但更加易于使用和功能丰富
* http.client：这是Python标准库中的低级HTTP客户端模块，允许你手动构建HTTP请求和处理响应
* urllib3：这是一个更高级的HTTP库，构建在urllib库之上，提供了连接池、请求重试等功能
* httpx：是一个现代化的、全功能的 HTTP 客户端库，提供了简洁的 API 和许多高级功能。它支持异步请求、连接池管理、文件上传、代理等功能，并且具有对 HTTP/2 和 HTTP/3 的支持

### requests使用
使用requests的前先安装：
```
pip install requests
```
* 发送普通GET请求
``` py
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Request failed with status code:", response.status_code)
```
* 发送带参数的GET请求
``` py
url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": "Shanghai,CN",
    "appid": "your_api_key"
}
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Request failed with status code:", response.status_code)
```
* 发送POST请求并传递数据
``` py
url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}
response = requests.post(url, json=data)

if response.status_code == 201:
    created_post = response.json()
    print("Created post:", created_post)
else:
    print("Request failed with status code:", response.status_code)
```
* 处理响应头和Cookies
``` py
url = "https://www.example.com"
response = requests.get(url)

if response.status_code == 200:
    print("Headers:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")

    cookies = response.cookies
    print("Cookies:", cookies)
else:
    print("Request failed with status code:", response.status_code)
```
* 处理异常和超时
``` py

url = "https://www.example.com"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()  # Raise an exception for HTTP errors
    print("Request successful:", response.text)
except requests.exceptions.RequestException as e:
    print("Request error:", e)
```

以上这些示例演示了 requests 库的一些常见用法，包括发送GET和POST请求、处理响应、处理异常等。requests 的其他功能，例如文件上传、会话管理、认证等查阅[官方文档](https://docs.python-requests.org/en/latest/)进行进一步学习

## 数据库编程
Python的数据库编程涉及到使用Python与数据库进行交互，从而实现数据的存储、检索、更新和删除等操作。Python提供了多种方式来进行数据库编程，最常用的方式包括使用标准库中的sqlite3模块、MySQL Connector/Python以及第三方库如SQLAlchemy、Django ORM和psycopg2等。

### SQLite3
sqlite3 是 Python 标准库中的模块，提供了对 SQLite 数据库的支持。它使用简单，无需额外安装，适用于小型项目或原型开发。
``` py
import sqlite3

# 连接到数据库（如果不存在则创建）
conn = sqlite3.connect('test.db')

# 创建游标对象
cursor = conn.cursor()

# 执行 SQL 查询
cursor.execute('SELECT * FROM users')

# 提取查询结果
results = cursor.fetchall()

# 处理查询结果
print(results)

# 关闭游标和连接
cursor.close()
conn.close()
```
### MySQL Connector/Python
* mysql-connector-python 是 MySQL 官方提供的 Python 驱动程序，用于连接和操作 MySQL 数据库。
* 它支持 Python 3.x，并提供了丰富的功能和灵活的 API。
* 示例：
``` py
import mysql.connector

# 连接到数据库
conn = mysql.connector.connect(
    host='localhost',
    user='username',
    password='password',
    database='database_name'
)

# 创建游标对象
cursor = conn.cursor()

# 执行 SQL 查询
cursor.execute('SELECT * FROM users')

# 提取查询结果
results = cursor.fetchall()

# 处理查询结果

# 关闭游标和连接
cursor.close()
conn.close()
```
### psycopg2：
* psycopg2 是用于连接和操作 PostgreSQL 数据库的第三方库。
* 它提供了高性能和稳定的 PostgreSQL 数据库访问功能。
* 示例：
``` py
import psycopg2

# 连接到数据库
conn = psycopg2.connect(
    host='localhost',
    user='username',
    password='password',
    database='database_name'
)

# 创建游标对象
cursor = conn.cursor()

# 执行 SQL 查询
cursor.execute('SELECT * FROM users')

# 提取查询结果
results = cursor.fetchall()

# 处理查询结果

# 关闭游标和连接
cursor.close()
conn.close()
```

## 多线程编程
多线程编程是指在一个程序中同时运行多个线程（轻量级的执行单元），以便实现并发执行任务的目标。在Python中，多线程编程可以通过内置的 threading 模块来实现。然而，需要注意的是，Python的多线程编程在某些情况下可能受到全局解释器锁（GIL）的限制，导致在某些多核处理器上并不能实现真正的并行执行。这意味着在某些CPU密集型任务中，多线程可能不如预期效果。下面是一个简单的多线程编程示例：
``` py
import threading
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
```
在上述示例中，通过打印线程开始和结束的消息来模拟线程的执行过程。

然后，创建了两个线程 thread1 和 thread2，分别指定它们的执行函数为 thread_function，并传递不同的参数。使用 start() 方法启动线程，并使用 join() 方法等待线程结束。最后，打印所有线程结束的消息。

需要注意的是，Python 的多线程编程默认情况下并不能充分利用多核处理器的并行性，因为有一个全局解释器锁（Global Interpreter Lock，GIL）的限制。如果需要利用多核处理器进行并行计算，可以考虑使用 multiprocessing 模块来创建多个进程，每个进程拥有独立的 GIL，从而实现并行执行。

### 线程同步
多个线程可能会同时访问共享的数据，因此需要进行线程同步以避免竞争条件和数据损坏。可以使用 threading.Lock 来实现简单的线程同步。
``` py
import threading

count = 0
lock = threading.Lock()

def increment():
    global count
    with lock:
        count += 1

threads = []

for _ in range(10):
    thread = threading.Thread(target=increment)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Count:", count)
```

### 线程间通信：
线程之间可以通过共享的数据结构（如队列、列表等）来进行通信。queue 模块提供了线程安全的队列。
``` py
import threading
import queue

def producer(q):
    for i in range(5):
        q.put(i)
        print("Produced:", i)

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print("Consumed:", item)
        q.task_done()

q = queue.Queue()
producer_thread = threading.Thread(target=producer, args=(q,))
consumer_thread = threading.Thread(target=consumer, args=(q,))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
q.put(None)
consumer_thread.join()
```
### 线程池：
concurrent.futures 模块提供了 ThreadPoolExecutor 和 ProcessPoolExecutor 类，用于创建线程池和进程池，以便更方便地管理并发任务。
``` py
import concurrent.futures

def worker(value):
    return value * 2

values = [1, 2, 3, 4, 5]

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    results = list(executor.map(worker, values))

print("Results:", results)
```
以上是 Python 中多线程编程的简要示例。在实际开发中，还需要处理异常、线程的生命周期管理、线程之间的通信等更复杂的情况。同时，记住在使用多线程时需要注意线程安全问题，以及GIL可能带来的性能影响。如果需要更强大的并发支持，可以考虑使用多进程编程或异步编程技术（如asyncio）来实现。

## 多进程编程
多进程编程是指在一个程序中同时运行多个独立的进程，以实现并行执行任务的目标。与多线程编程不同，多进程编程可以在多核处理器上实现真正的并行执行，因为每个进程有自己独立的Python解释器和内存空间。在Python中，可以使用内置的 multiprocessing 模块来实现多进程编程，可以让利用多核处理器的并行性。下面是一个简单的多进程编程示例：
``` py
import multiprocessing
import time

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
```
在上述示例中，通过打印进程开始和结束的消息来模拟进程的执行过程。

然后，创建了两个进程 process1 和 process2，分别指定它们的执行函数为 process_function，并传递不同的参数。我们使用 start() 方法启动进程，并使用 join() 方法等待进程结束。最后，打印所有进程结束的消息。

需要注意的是，为了避免创建子进程时发生递归调用问题，将主程序的代码放在 if \__name__ == "\__main__" 的条件语句中。这是因为在 Windows 系统中，multiprocessing 模块会通过创建子进程来执行代码，而子进程也会导入主程序的模块。通过将主程序的代码放在 if \__name__ == "\__main__" 条件下，可以确保只有在直接运行主程序时才会执行这部分代码，而在子进程中不会执行。

运行以上代码，会看到两个进程同时启动并执行，然后打印出所有进程结束的消息。

使用 multiprocessing 模块还可以进行更复杂的多进程编程，如进程间通信、进程池等。可以参考官方文档或其他教程来了解更多关于 multiprocessing 模块的功能和用法。

### 进程间通信
在 multiprocessing 模块中，可以使用多种方式进行进程间通信，包括队列（Queue）、管道（Pipe）和共享内存（Shared Memory）。

* 队列（Queue）：是用于在进程之间安全地传递数据的一种常用方式。多个进程可以通过将数据放入队列的方式进行通信。
``` py
from multiprocessing import Process, Queue

def producer(queue):
    for i in range(5):
        item = 'Item {}'.format(i)
        queue.put(item)
        print('Produced:', item)

def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        print('Consumed:', item)

if __name__ == '__main__':
    queue = Queue()
    process1 = Process(target=producer, args=(queue,))
    process2 = Process(target=consumer, args=(queue,))
    process1.start()
    process2.start()
    process1.join()
    process2.join()
```
在上述示例中，创建了一个队列 queue，然后在生产者进程中使用 put() 方法将数据放入队列，消费者进程使用 get() 方法从队列中获取数据。通过队列实现的进程间通信是线程安全的。

* 管道（Pipe）：是一种双向通信机制，可以在两个进程之间传递数据。每个管道都有两个端点，分别用于读取和写入数据。
``` py
from multiprocessing import Process, Pipe

def sender(conn):
    messages = ['Message 1', 'Message 2', 'Message 3']
    for msg in messages:
        conn.send(msg)
        print('Sent:', msg)
    conn.close()

def receiver(conn):
    while True:
        msg = conn.recv()
        if msg is None:
            break
        print('Received:', msg)

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    process1 = Process(target=sender, args=(parent_conn,))
    process2 = Process(target=receiver, args=(child_conn,))
    process1.start()
    process2.start()
    process1.join()
    process2.join()
```
在上述示例中，创建了一个管道，使用 Pipe() 函数返回两个连接对象 parent_conn 和 child_conn，分别用于父进程和子进程之间的通信。在发送者进程中，使用 send() 方法将消息发送到管道，而接收者进程使用 recv() 方法从管道中接收消息。

* 共享内存（Shared Memory）：允许多个进程共享一块内存区域，从而实现数据的共享。multiprocessing 模块提供了 Value 和 Array 两个类来创建共享内存对象。
``` py
from multiprocessing import Process, Value, Array

def writer(val, arr):
    val.value = 10
    for i in range(len(arr)):
        arr[i] = arr[i] * 2

def reader(val, arr):
    print('Value:', val.value)
    print('Array:', arr[:])

if __name__ == '__main__':
    val = Value('i', 0)
    arr = Array('d', [1.0, 2.0, 3.0, 4.0, 5.0])
    process1 = Process(target=writer, args=(val, arr))
    process2 = Process(target=reader, args=(val, arr))
    process1.start()
    process2.start()
    process1.join()
    process2.join()
```
在上述示例中，创建了一个整型共享内存对象 val 和一个双精度浮点型共享内存数组 arr，它们可以在多个进程之间共享。在写入者进程中，我们修改了共享内存对象的值和数组中的元素，而读取者进程则读取并打印了共享内存对象和数组的值。

以上是使用 multiprocessing 模块进行进程间通信的几种常见方式。可以根据具体需求选择适合的方式进行进程间数据通信。需要注意的是，进程间通信可能涉及到数据的同步和互斥访问，因此在使用这些方式进行通信时，应当谨慎处理数据的读写操作，以避免潜在的竞争条件和数据一致性问题。

### 进程同步
多个进程可能会同时访问共享的数据，因此需要进行进程同步以避免竞争条件和数据损坏。与多线程不同，多进程使用 multiprocessing.Lock 进行进程同步。
``` py
import multiprocessing

count = multiprocessing.Value('i', 0)
lock = multiprocessing.Lock()

def increment():
    global count
    with lock:
        count.value += 1

processes = []

for _ in range(10):
    process = multiprocessing.Process(target=increment)
    processes.append(process)
    process.start()

for process in processes:
    process.join()

print("Count:", count.value)
```

### 进程池
multiprocessing.Pool 类提供了进程池的功能，可以方便地管理并发任务。
``` py
import multiprocessing

def worker(value):
    return value * 2

values = [1, 2, 3, 4, 5]

with multiprocessing.Pool(processes=2) as pool:
    results = pool.map(worker, values)

print("Results:", results)
```

以上是多进程编程的简要示例。在实际开发中，还需要处理异常、进程的生命周期管理、进程之间的通信等更复杂的情况。多进程编程可以在CPU密集型任务中实现更好的性能，但也需要注意进程间通信的开销。如果需要更轻量级的并发支持，可以考虑使用多线程编程或异步编程技术（如asyncio）来实现。

## 异步编程
在Python中，异步编程通常使用asyncio库来实现。下面是对Python中异步编程的简单介绍：

* 协程（Coroutines）：协程是异步编程的基本单位。它是一种特殊的函数，可以在执行过程中暂停并恢复。在Python中，通过使用async关键字定义协程函数。

``` py
async def my_coroutine():
    # 协程函数的代码
    ...
```

* 事件循环（Event Loop）：事件循环是异步编程的核心机制。它负责调度协程的执行，并处理事件的触发和分发。在Python中，可以使用asyncio库创建和管理事件循环。

``` py
import asyncio

async def main():
    # 创建事件循环
    loop = asyncio.get_event_loop()

    # 执行协程
    await my_coroutine()

    # 关闭事件循环
    loop.close()

# 运行主函数
asyncio.run(main())
```

* 异步函数（Async Functions）：异步函数是一种特殊的函数，它可以在内部包含await关键字来等待其他协程的完成。异步函数可以被协程或其他异步函数调用。

``` py
async def async_function():
    # 等待其他协程的完成
    await other_coroutine()
    ...
```

* await关键字：await关键字用于等待一个协程的完成。当遇到await时，当前协程会被挂起，事件循环可以执行其他任务。一旦等待的协程完成，挂起的协程会被恢复。

``` py
async def my_coroutine():
    await asyncio.sleep(1)  # 等待1秒钟
    ...
```

* 异步IO操作：异步编程通常用于处理IO密集型任务，例如网络请求或文件操作。在Python中，asyncio库提供了异步IO操作的支持，包括协程化的套接字、文件和其他IO资源。

``` py
async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()
```

* 并发执行：异步编程能够实现高效的并发执行。通过将多个协程一起调度，可以同时执行多个任务而不会阻塞主线程。

``` py
async def main():
    coroutines = [my_coroutine() for _ in range(10)]
    await asyncio.gather(*coroutines)
```

以上是Python中异步编程的基本概念和组件。通过使用异步编程，可以提高程序的性能和响应性，特别是在处理IO密集型任务时。


当涉及到网络请求或IO操作时，异步编程可以提供显著的性能改进。下面是一个使用异步编程进行并发网络请求的实际例子：
``` py
import asyncio
import aiohttp

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data

async def main():
    urls = [
        "https://api.example.com/data/1",
        "https://api.example.com/data/2",
        "https://api.example.com/data/3"
    ]

    tasks = [fetch_data(url) for url in urls]
    results = await asyncio.gather(*tasks)

    for result in results:
        print(result)

asyncio.run(main())
```
在这个例子中，使用aiohttp库来进行异步网络请求。fetch_data函数使用async with语法创建了一个异步的HTTP会话，并发起GET请求。然后，用await关键字来等待响应的完成，并将响应转换为JSON格式的数据。

在main函数中，定义了要请求的URL列表。然后，创建了一个包含所有异步任务的列表tasks，每个任务都是调用fetch_data函数。接下来，使用asyncio.gather函数将所有任务一起调度，并使用await关键字等待它们的完成。最后，打印每个请求的结果。

通过使用异步编程，可以并发地发起多个网络请求，并在它们完成后处理结果，而不需要等待每个请求的响应。这样可以大大提高程序的性能和效率。

### 协程
协程（Coroutines）是一种用于异步编程的概念，它允许在单个线程内实现并发执行任务，从而实现非阻塞的异步操作。在Python中，协程通过使用 async 和 await 关键字来定义和管理，主要用于处理I/O密集型任务，如网络请求、文件读写等。一个常见的例子是使用协程来实现生成器的高级用法。在这种情况下，协程可以在生成器的迭代过程中实现双向通信。下面是一个简单的例子：

``` py
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
```
在这个例子中，coroutine_example函数是一个协程函数。在函数内部，yield语句用于接收从调用者发送的值，并将控制权返回给调用者。每次调用coroutine.send(value)时，值会被发送给协程，并在yield语句处恢复协程的执行。

在主程序中，首先创建了一个协程对象coroutine，然后使用next(coroutine)启动协程。接下来，使用coroutine.send(value)向协程发送值。第一个发送的值是10，然后是字符串"Hello"。每次发送值后，协程会打印接收到的值。

通过使用协程，可以实现双向通信，将值传递给协程并从中获取结果。这种能力使得协程在处理大量数据流、事件处理和并发编程等场景中非常有用。

* 协程调用和执行：
协程函数的调用并不立即执行，而是返回一个协程对象。要执行协程，可以使用 await 关键字，也可以将协程对象传递给 asyncio.run() 函数。

``` py
import asyncio

async def main():
    print("Main coroutine is starting")
    await asyncio.sleep(1)
    print("Main coroutine is done")

asyncio.run(main())
```

* 并发执行多个协程：
使用 asyncio.gather() 函数可以并发执行多个协程，从而实现并行执行多个异步任务。
``` py
import asyncio

async def coroutine_a():
    await asyncio.sleep(1)
    print("Coroutine A is done")

async def coroutine_b():
    await asyncio.sleep(2)
    print("Coroutine B is done")

async def main():
    await asyncio.gather(coroutine_a(), coroutine_b())

asyncio.run(main())
```

* 协程间通信：
协程之间可以通过 asyncio.Queue 实现通信，类似于线程间的队列。协程可以通过 put() 将数据放入队列，另一个协程可以通过 get() 从队列中获取数据。

``` py
import asyncio

async def producer(queue):
    for i in range(5):
        await asyncio.sleep(1)
        await queue.put(i)
        print(f"Produced: {i}")

async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"Consumed: {item}")

async def main():
    queue = asyncio.Queue()
    producer_coroutine = producer(queue)
    consumer_coroutine = consumer(queue)

    await asyncio.gather(producer_coroutine, consumer_coroutine)

asyncio.run(main())
```

协程和线程是两种不同的并发编程概念，它们具有不同的优势和特点：

* 并发性：线程是操作系统级别的并发模型，多个线程可以同时执行，每个线程都有自己的执行上下文和调度。而协程是程序级别的并发模型，在单个线程内通过协作式调度实现并发。多个协程可以在一个线程中交替执行，通过在合适的时机主动让出控制权来实现并发。

* 资源消耗：线程在创建时会分配较大的内存空间，每个线程都需要独立的堆栈和执行上下文，因此创建大量线程可能导致内存消耗过大。相比之下，协程是轻量级的，它们共享同一个线程的资源，不需要额外的内存分配。

* 切换开销：线程之间的切换需要由操作系统负责，涉及上下文切换和内核态与用户态之间的切换，开销较大。而协程之间的切换是由程序显式控制的，切换开销较小，不涉及内核态的切换。

* 编程模型：线程使用共享状态和锁来实现并发控制，这可能导致复杂的并发问题，如死锁和竞态条件。协程通过避免共享状态和显式的消息传递来简化并发编程，使得代码更容易理解和调试。

* 异常处理：线程中的异常通常会导致整个线程终止，需要额外的机制来处理异常。协程可以通过try/except块捕获异常，并在协程内部进行处理。

总体而言，协程适用于高效处理大量IO密集型任务，例如网络请求和文件操作，可以实现高并发和高吞吐量。线程适用于需要利用多核处理器或执行计算密集型任务的场景。在选择使用协程还是线程时，需要根据具体的需求和应用场景进行权衡。