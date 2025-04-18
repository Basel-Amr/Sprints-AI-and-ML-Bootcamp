print("Try programiz.pro")
i=0
list = []
while(1):
    try:
        while(1):
            list.append(i)
            list.append(i)
            list.append(i)
            list.append(i)
            list.append(i)
            list.append(i)
            list.append(i)
        a = int(input("Enter a number1: "))
        b = int(input("Enter a number2: "))
        Result = a/b
    except ValueError:
        print("Enter a valid number")
    except ZeroDivisionError:
        print("cannot divide on 0")
    except:
        print("Typed a signal")
        break