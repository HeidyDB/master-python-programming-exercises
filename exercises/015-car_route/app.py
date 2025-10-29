# Complete the function to return the amount of days it will take to cover a route
import math 
def car_route(n,m):
  if  n==0:
    return 0

  if m<=0:
    return "la distancia por dia debe ser mayor a 0"
  return int(math.ceil(m/n))


# Invoke the function with two integers
print("reco<rrido en dias:" ,car_route(4, 8))
