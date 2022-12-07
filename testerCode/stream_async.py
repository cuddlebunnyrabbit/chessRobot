from lichess_client import APIClient
import asyncio 


tokenThing = "lip_VQSKvH586ClP01n94FTr"
client = APIClient(token=tokenThing)

async def get_email():  
    print("in email")
    response = await client.account.get_my_email_address()
    print("in here")
    return response.entity.content()

async def main():
    task1 = asyncio.create_task(get_email())
    print("in main")
    val1 = await task1
    print(val1)

asyncio.run(main())








