#problem 1

Fixed_dict = {}

try:
    with open('inventory.txt', 'r') as f, open('audit_errors.log', 'w') as errors:
        for line in f:
            try:
                items = line.split(':')
                
                item_name = items[0].strip()
                item_price = int(items[1].strip())
            except IndexError:
                print("there is missing data")
                continue
            except ValueError:
                print("wronge data_type given")
                errors.write(line)
                continue

            item_name = item_name.upper()

            if item_name in Fixed_dict:
                Fixed_dict[item_name.upper()] += item_price
            else:
                Fixed_dict[item_name.upper()] = item_price

        
except FileNotFoundError:
    print('file does not exist')


print(Fixed_dict)

#===========================================================================
#problem 2

all_logins = [
    "192.168.1.1", "10.0.0.5", "192.168.1.1", "172.16.0.1", 
    "10.0.0.5", "192.168.1.10", "172.16.0.1", "8.8.8.8", 
    "192.168.1.1", "10.0.0.9", "192.168.1.10", "10.0.0.5"
]
blacklisted_ips = {"172.16.0.1", "8.8.8.8", "200.50.10.1"}

safe_logins = set()

for login in all_logins:
    if not login in blacklisted_ips:
        safe_logins.add(login)
        

safe_logins_tuple = tuple(safe_logins)

print(safe_logins_tuple)

with open('authorized_logins.txt', 'w') as f:
    for login in safe_logins_tuple:
        f.write(login + '\n')



#===========================================================================
#problem 3

while True:
    
    
    try:
        number = input("Give me a number")

        if number == 'exit':
            break
        number = int(number)
        
        try:
            if number > 5000:
                raise ValueError
        except ValueError:
            print("High Value: Requires Approval")
        
        try:
            if number <= 0:
                raise ValueError
        except ValueError:
            print("invalid Amount")


    except ValueError:
        print("Invalid Data Type")
    finally:
        print("System: Monitoring active")


#===========================================================================
#problem 4

final_grades = {}

def merger(info):
    for name, grades in info.items():

        if name in final_grades:
            final_grades[name].extend(grades)
        else:
            final_grades[name] = grades




semester_1 = {
    "Alice": [85, 90], "Bob": [70, 65], "Charlie": [100], 
    "David": [88], "Eve": [92, 91]
}
semester_2 = {
    "Alice": [95, 88], "Frank": [78, 80], "Bob": [72], 
    "Grace": [99], "Charlie": [90, 85], "Heidi": [75]
}


merger(semester_1)
merger(semester_2)

print(final_grades)

