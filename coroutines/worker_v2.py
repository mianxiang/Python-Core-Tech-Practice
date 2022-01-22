import asyncio
import time

async def worker_1():
    print('worker_1 start')
    await asyncio.sleep(1)
    print('worker_1 done')

async def worker_2():
    print('worker_2 start')
    await asyncio.sleep(2)
    print('worker_2 done')

async def main():
    print('before start')
    worker1_task = asyncio.create_task(worker_1())
    worker2_task = asyncio.create_task(worker_2())
    await worker1_task
    print('awaited worker1')
    await worker2_task
    print('awaited worker2')

if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())
    end = time.perf_counter()
    print('Execution overall time:{}'.format(end - start))
