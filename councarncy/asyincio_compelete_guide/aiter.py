
# a = -10
# print(abs(a))

import asyncio
# rows = [[col for col in range(5)] for row in range(10)]

# async def return_rows(rows):
#   for row in rows:
#     yield row
#     # return iter(row)

# async def main():
#   gen = return_rows(rows)
#   async for r in gen:
#       print(r)

# async for r in gen:
#   print(r)

# asyncio.run(main())


def change_size(current):
  return 2 * current


class Car(object):

  def __init__(self, wheels=4):
    self.wheels_sizes = iter([i for i in range(wheels)])

  async def __aiter__(self):

    for i in self.wheels_sizes:
      
      await asyncio.sleep(2)
      yield i


async def main():
  car = Car()
  print(change_size(3))
  car.wheels_sizes = map(change_size, car.wheels_sizes)
  # result = map(change_size())
  async for size in car:
    
    print(size)

  print(car.wheels_sizes)




asyncio.run(main())

