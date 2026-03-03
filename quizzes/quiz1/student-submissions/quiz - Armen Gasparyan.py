while True:
    try:
        x = input("Enter number")
        if str(x)  == 'exit':
            break
        if int(x) > 5000: 
            raise  ValueError ("High Value: Requires Approval")
        if int(x) <0:
            raise  ValueError("Invalid Amount")
    except ValueError:
        print ("Invalid Data Type")
    finally:
        print ("System: Monitoring active.")