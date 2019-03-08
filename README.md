# PriorityThreadPoolExecutor
Little hack of **ThreadPoolExecutor** from **concurrent.futures.thread**: thread pool executor with priority queue (priorities must be different, lowest first). Priority can be any integer value except **sys.maxsize**


Example:
```
import time
from priority_thread_pool_executor import PriorityThreadPoolExecutor


def print_number(number, seconds=3):
    print('Start %s' % number)
    time.sleep(seconds)
    print('Stop %s' % number)


if __name__ == '__main__':
    pool = PriorityThreadPoolExecutor(max_workers=1)
    with pool:
        for x in range(10):
            pool.submit(print_number, x-1, 1, priority=9-x)

```
Result:
```
Start -1
Stop -1
Start 8
Stop 8
Start 7
Stop 7
Start 6
Stop 6
Start 5
Stop 5
Start 4
Stop 4
Start 3
Stop 3
Start 2
Stop 2
Start 1
Stop 1
Start 0
Stop 0
```
Threads run according to priority
