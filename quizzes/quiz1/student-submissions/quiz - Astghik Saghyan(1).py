import pprint

items = {}

with (open('inventory.txt', 'r') as inventory, open('audit_errors.log', 'w') as logs):
    for line in inventory:
        data = line.strip().split(':')
        if len(data) != 2:
            logs.write(line)
            continue

        item, price = data

        try:
            price = int(price)
        except ValueError:
            logs.write(line)
        else:
            item = item.upper()
            if item not in items:
                items[item] = price
            else:
                items[item] += price

pprint.pprint(items)


all_logins = [
    "192.168.1.1", "10.0.0.5", "192.168.1.1", "172.16.0.1", 
    "10.0.0.5", "192.168.1.10", "172.16.0.1", "8.8.8.8", 
    "192.168.1.1", "10.0.0.9", "192.168.1.10", "10.0.0.5"
]
blacklisted_ips = {"172.16.0.1", "8.8.8.8", "200.50.10.1"}

safe_ips = set()

for ip in all_logins:
    if ip not in blacklisted_ips:
        safe_ips.add(ip)

safe_ips = tuple(safe_ips)

with open('authorized_logins.txt', 'w') as logins:
    
    for ip in safe_ips:
        logins.write(ip + '\n')

print(safe_ips)


while True:
    number = input("Enter a number: ")

    if number == "Exit":
        break

    try:
        number = int(number)
    except ValueError:
        print("Invalid Data Type")
    else:
        try:
            if number > 5000:
                raise ValueError("High Value: Requires Approval")
            if number <= 0:
                raise ValueError("System: Monitoring active.")
        finally:
            print("System: Monitoring active.")