try:
    number1=float(input("Please enter number1: "))
    number2=float(input("Please enter number2: "))
    operator=input("Please enter a operator (+,-,*,/,%,**)")

    if operator == "+":
      result=(number1+number2)
    elif operator == "-":
     result=(number1-number2)
    elif operator == "*":
     result=(number1*number2)
    elif operator == "/":
     if number2 != 0:
      result=(number1/number2)
     else :
       result="cannot divide by zero"
    elif operator == "%":
       if number2 != 0:
        result=(number1%number2)
       else :
         result="cannot divide by zero"
    elif operator == "**":
      result=(number1**number2)
    else:
       result=("invalid operator")
    print(number1 , operator,number2, "= ", result)
except ValueError:
 print("Please enter a valid number")

