# username ="tamim"
# print("username is:", username)
# variable = 10
# print("variable is:", variable)


# username = "tamim"
# print(type(username))

cpu_range = 3.4
print(type(cpu_range))


#list

ports=[80, 443, 8080]
print(type(ports))
print(ports[0])
print(ports)

#dictionary

user = {"name": "tamim", "class": "python", "roll": 10}
print(type(user))
print(user["name"])

#user input 

uses= input("enter the name:")
print(uses)

username = input("enter the number:")
print(username)

number = int(input("enter the number:"))
print(number)


ips=["192.168.1.1", "192.168.1.2", "192.168.1.3"]

feild_attamp=[2,7,1,10]
for i in range(len(ips)):
     print("IP:", ips[i], "Feild Attamp:", feild_attamp[i])

if feild_attamp[i] > 5:
        print("IP:", ips[i], "is blocked due to high feild attamp:", feild_attamp[i])

