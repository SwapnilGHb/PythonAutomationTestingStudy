print("-----Satrt of the Program")
try:
    a = int(input("Enter the Num1")) #ValueError: invalid literal for int() with base 10: ' pramod'
    b = int(input("Enter the Num2"))
    c = a / b # ZeroDivisionError: division by zero
    print("Result Div is ", c)
except Exception as e:
    print(e)
print("-----End of the Program")

# try and Except