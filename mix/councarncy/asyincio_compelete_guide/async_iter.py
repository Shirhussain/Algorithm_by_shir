# https://docs.python.org/3/library/functions.html

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

# import time

# def change_size():
#   print('change_size')

# async def get_data():
#   await asyncio.sleep(3)
#   return [1,2,3,4]

# async def change_data(data):
#   await asyncio.sleep(1)
#   return (await data) * 2

# Future
# Corotine

# async def main():
#   # await asyncio.to_thread(change_size)
#   # a = await get_data()
#   b = asyncio.create_task(change_data(get_data()))
#   c = await b
#   print(c)
#   # await asyncio.to_thread(change_size)

users = []


async def send_email(email, context):
  await asyncio.sleep(3)
  print(f"email has been sent to {email}")


class User(object):

  def __init__(self, email, password):
    self.id = id
    self.email = email    
    self.password = password

  async def save(self):
    await asyncio.sleep(1)

    self.id = len(users) + 1
    users.append(self)
    print('user saved')


async def signup(email, password):
  user = User(email, password)
  user_c = asyncio.create_task(user.save())
  email_c = asyncio.create_task(send_email(email, {}))
  print('Email Send')
  await user_c
  await email_c


async def main():
  await signup('test@test.com', "1233445")


asyncio.run(main())

