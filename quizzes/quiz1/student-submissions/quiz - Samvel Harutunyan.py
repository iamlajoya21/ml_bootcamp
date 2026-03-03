

print("="*50)
print(" " *20 + "Problem 1")
print("="*50)
d = {}
k = 0

with open("inventory.txt","r") as f, open("audit_errors.log", "w") as e:
    for line in f:
        line = line.strip()
        try:
            parts = line.split(":")

            if type(int(parts[1]))  != int:
                raise TypeError
            name = parts[0].upper()
            if name not in d:
                d[name] = 0
            d[name] += int(parts[1])

        except TypeError:
            k+=1
            e.write(line + "\n")

print(d,k)




print("="*50)
print(" " *20 + "Problem 2")
print("="*50)


all_logins = [
    "192.168.1.1", "10.0.0.5", "192.168.1.1", "172.16.0.1",
    "10.0.0.5", "192.168.1.10", "172.16.0.1", "8.8.8.8",
    "192.168.1.1", "10.0.0.9", "192.168.1.10", "10.0.0.5"
]
blacklisted_ips = {"172.16.0.1", "8.8.8.8", "200.50.10.1"}

s= set()

with open("authorized_logins.txt", "w") as e:
    for i in all_logins:
        if i in blacklisted_ips:
            all_logins.remove(i)
        s.add(i)

    t = tuple(s)

    for item in t:
        e.write(item + "\n")






print("="*50)
print(" " *20 + "Problem 3")
print("="*50)



b = True

while b:

    c = input("Enter an amount: ")
    if c == "exit":
        b = False
    try:

        if type(int(c)) != int:
            print("Invalid Data Type")
            raise ValueError

        num = int(c)
        if num > 5000:
            print("High Value: Requires Approval")
            raise ValueError
        if num <=0:
            print("Invalid Amount")
            raise ValueError


    except ValueError:
        print(" ")


    finally:
        print("System: Monitoring active.")


print("="*50)
print(" " *20 + "Problem 4")
print("="*50)

