try:
    a = int(input(" Please enter the desired number"))
    print(a+3)
# except:
#     print("Some error occured there,please enter only number")
except Exception as e:
    print("Some error occured", e)
