#Problem 1
file_path1 = '/Users/lilit/Downloads/inventory.txt'
res = {}

with open(file_path1, 'r') as file1, open("audit_errors.log", "w") as error_file:
     for line in file1:
         try:
            new_line = line.strip()
            up = new_line.upper()
            split_line = up.split(":")
            print(split_line) #check
            for item in split_line:
                if item not in res:
                    res[item] = item
                else:
                    res[item] += 1
        except ValueError:
     error_file.write(new_line + "\n")                   

print(res)



#Problem 2
all_logins = [
    "192.168.1.1", "10.0.0.5", "192.168.1.1", "172.16.0.1", 
    "10.0.0.5", "192.168.1.10", "172.16.0.1", "8.8.8.8", 
    "192.168.1.1", "10.0.0.9", "192.168.1.10", "10.0.0.5"
]
blacklisted_ips = {"172.16.0.1", "8.8.8.8", "200.50.10.1"}

store = []
for ip in all_logins:
    if ip not in blacklisted_ips:
        store.append(ip)
unique = set(store)
safe_uniqu = tuple(unique)

with open("authorized_login.txt", "w") as err_file:
    for ip in safe_uniqu:
        file.write(ip + "\n")
print(safe_uniqu)



#Problem 3
while True:
    try:
        amount = (input("Enter amount or type 'exit to stop"))
        if amount == 'exit':
            break 
        if amount > 5000:
            raise ValueError("High Value Reuires approval")
        if amount <= 0:
            raise ValueError("Invalid")
    except:
        print()
    finally:
        print()


#Problem 4