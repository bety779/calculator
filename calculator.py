
def mihret (): 
    print("standard calculator") 
    try: 
        while True: 
            op = input("Enter the operaters [/,*,-,+,**and exit]") 
            if op.lower().strip () == "exit":
                print("Existing calculator") 
            
                break  
            list_op = ['+','-','*','/','**'] 
            if op not in list_op: 
                print("please Enter the correct operator") 
                continue 

            numbers =[] 
            while True: 
                number = input("please Enter the number or = sign to calculator") 
                if number =="=": 
                    if len(numbers)<2: 
                        print("please Enter atleast 2 numbers") 
                    continue 
                break
                try :
                    num = float(number) 
                    numbers.append(num) 
                except ValueError: 
                        print("please enter the number only")   
                        continue  
                """performing different arthimetric oprations 
                    after performing arthimetric 
                    oprations we have to store the result on some variabel""" 
                if op =="+": 
                        result = numbers[0] 
                        for item in numbers[1:]: 
                            result =result + item 
                        print(" + ".join(map(str,numbers)) + f"={result}")    
                elif op =='*': 
                        result = numbers[0] 
                        for item in numbers[1:]: 
                            result = result * item 
                        print (" * ".join(map(str,numbers)) + f"={result}") 
                elif op == "/": 
                        result = number[0] 
                        for item in numbers[1:]: 
                            try: 
                                if item == 0:    
                                    raise ZeroDivisionError() 
                                result = result / item 
                            except ZeroDivisionError :
                               print("Denominator can not be zero")  
                            print("/".join(map(str,numbers)) + f"= {result}")   
                elif op == "-": 
                        result = numbers[0] 
                        for item in numbers [1:]: 
                            result = result - item 
                        print(" - ".join(map(str, numbers)) + f" = {result}") 
                elif op == "*": 
                        result = numbers[0] 
                        for item in numbers[1:]: 
                            result = reult ** item 
                        print(" ** ".join(map(str,numbers)) + f" = {result}")
    except Exception as e: 
        print(f"opration failed!{e}") 
    print("Developed By: aryam")
    calculator()
