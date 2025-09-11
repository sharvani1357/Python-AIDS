numerator=int(input("enter numerator"))
denominator=int(input("enter denominator"))
try:
    div=numerator/denominator
    print("result:",div)
except Exception:
    print("error:Division by zero is not allowed")
else:
    print(div)
finally:
    print("Execution done!")