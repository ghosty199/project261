import requests
equation=input("enter the equation=")
result='https://newton.now.sh/api/v2//simplify/'+equation
print(result)
data=requests.get(result).json()
print("operations for the given equation"+data["operation"])
print("result for the given equation"+data["result"])
