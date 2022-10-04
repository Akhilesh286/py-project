import asyncio
import time
from pytube import YouTube 
'''
async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

asyncio.run(main())

import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")


#asyncio.run(main())
async def main():
    task1 = asyncio.create_task(
        say_after(3, 'hello'))

    task2 = asyncio.create_task(
        say_after(5, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")
asyncio.run(main())

async def function1 ():
  print ("hello")
  time.sleep(2)
  task2 = asyncio.create_task(function2())
  await task2
  #await asyncio.sleep(2)
  #YouTube ("https://youtu.be/98v7iA0LgzY").streams.get_by_itag(18).download()
  #time.sleep(3)
  print ("done..")
async def function2 ():
  print ("world")
  #time.sleep(5)
  #await asyncio.sleep(1)
  for i in range(10):
    print (i)
    await asyncio.sleep(.25)

async def main ():
  task1 = asyncio.create_task(function1())
  #task2 = asyncio.create_task(function2())
  await task1
  #await task2
  #await task1
  #await task2
asyncio.run(main())
'''
import asyncio
import time


async def sleep():
  time.sleep(1)


async def count():
    print("One")
    #await sleep()
    await asyncio.sleep(1)
    #time.sleep(1)
    print("Two")

async def count2():
    print("One")
    #await sleep()
    await asyncio.sleep(1)
    #time.sleep(1)
    print("Two")


async def main():
    #await asyncio.gather(count(), count(), count())
    await asyncio.create_task(count())
    asyncio.create_task(count2())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
'''
#!/usr/bin/env python3
# countsync.py

import time

def count():
    print("One")
    time.sleep(1)
    print("Two")

def main():
    for _ in range(3):
        count()

if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
'''