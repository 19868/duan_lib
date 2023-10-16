import time

def execute_time(function):
    start_time=time.time()
    function()
    end_time=time.time()
    execute_time=end_time - start_time
    return execute_time

def Print():
    for i in range(100000):
        pass
    print("测试函数")

print(f"{execute_time(Print):.6f}s")