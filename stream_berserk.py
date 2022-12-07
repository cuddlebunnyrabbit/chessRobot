import berserk

session = berserk.TokenSession("lip_VQSKvH586ClP01n94FTr")
client = berserk.Client(session=session)

print(client.users.get_puzzle_activity)