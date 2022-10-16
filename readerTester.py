'''
file_obj = open("tasks.txt")

for line in file_obj:
    print(line)

file_obj.close()
'''

with open("tasksTester.txt") as file_obj:
    for line in file_obj:
        print(line)
        #print("hello")