def check_num(n):
  try:
    int(n)
  except ValueError:
    return False
  return True
#Exercise_01
def F1_score ( tp =1 , fp =1 , fn =1):
    print("EXERCISE_1")
    if (check_num(tp)==False):
      print("tp must be int")
      return
    elif (check_num(fp)==False):
      print("fp must be int")
      return
    elif (check_num(fn)==False):
      print("fn must be int")
      return
    tp = int(tp)
    fn = int(fn)
    fp = int(fp)
    if (tp < 0 or fp < 0 or fn < 0) :
      print("tp and fp and fn must be greater than zero")
      return
    precision = tp/(tp + fp)
    recall = tp/(tp + fn)
    F1_score = 2*(precision * recall)/(precision + recall)
    print("precision is ", precision)
    print("recall is ", recall)
    print("f1_score is ", F1_score)

#Exercise_02
import math
def activate_func():
    x = (input("Input x = "))
    if(check_num(x)==False):
      print("x must be a number")
      return
    actFunc = (input("Input activation Function (sigmoid|relu|elu): "))
    if(actFunc != "sigmoid" and actFunc!= "relu" and actFunc!= "elu"):
      print(actFunc, " is not supported")
      return
    x = float(x)
    if(actFunc == "sigmoid"):
      sigmoid = 1/(1 + pow(math.e, -x))
      print(f"Sigmoid: f({x}) =  {sigmoid}")
    elif(actFunc == "relu"):
      if(x<=0):
        relu = 0
        print(f"Relu: f({x}) =  {relu}")
      elif(x>0):
        relu = x
        print(f"Relu: f({x}) =  {relu}")
    elif(actFunc == "elu"):
      alpha = 0.01
      if(x<=0):
        elu = alpha*(pow(math.e, x) - 1)
        print(f"Elu: f({x}) =  {elu}")
      elif(x>0):
        elu = x
        print(f"Elu: f({x}) =  {elu}")

#Exercise_03
import random
def loss_func(n, loss_name):
  if(check_num(n) == False):
    print("number of space must be integer")
    return
  n = int(n)
  if (loss_name == "MAE"):
    MAE = 0
    for i in range(0, n):
      y = random.uniform(0, 10)
      _y = random.uniform(0, 10)
      MAE += abs(y - _y)
      print(f"loss name: {loss_name}, sample: {i}, pred: {y}, target: {_y}, loss: {MAE}")
    MAE /= n
    print(f"final MAE: {MAE}")
    return
  elif (loss_name == "MSE"):
    MSE = 0
    for i in range (0, n):
      y = random.uniform(0, 10)
      _y = random.uniform(0, 10)
      MSE += pow(y - _y, 2)
      print(f"loss name: {loss_name}, sample: {i}, pred: {y}, target: {_y}, loss: {MSE}")
    MSE /= n
    print(f"final MS5E: {MSE}")
    return
  elif (loss_name == "RMSE"):
    RMSE = 0
    for i in range (0, n):
      y = random.uniform(0, 10)
      _y = random.uniform(0, 10)
      RMSE += pow(y - _y, 2)
      print(f"loss name: {loss_name}, sample: {i}, pred: {y}, target: {_y}, loss: {RMSE}")
    RMSE /= n
    RMSE = math.sqrt(RMSE)
    print(f"final RMSE: {RMSE}")
    return

#Exercise 4
def appox_sin(x = 3.14, n = 10):
  sinx = 0
  x = int(x)
  n = int(n)
  for i in range(n + 1):
    sinx += pow(-1, i)*(pow(x, 2*i + 1)/(math.factorial(2*i + 1)))
  print(sinx)
  return

def appox_cos(x = 3.14, n = 10):
  cosx = 0
  x = int(x)
  n = int(n)
  for i in range(n + 1):
    cosx += pow(-1, i)*(pow(x, 2*i)/(math.factorial(2*i)))
  print(cosx)
  return 

def appox_sinh(x = 3.14, n = 10):
  sinhx = 0
  x = int(x)
  n = int(n)
  for i in range(n + 1):
    sinhx += (pow(x, 2*i + 1)/(math.factorial(2*i + 1)))
  print(sinhx)
  return

def appox_cosh(x = 3.14, n = 10):
  coshx = 0
  x = int(x)
  n = int(n)
  for i in range(n + 1):
    coshx += (pow(x, 2*i)/(math.factorial(2*i)))
  print(coshx)
  return

#Exercise 5
def mean_diff_func(y, _y, n, p):
  y = int(y)
  _y = int(y)
  n = int(n)
  p = int(p)
  MDF = pow(y, 1/n) - pow(_y, 1/n)
  MDF = pow(MDF, p)
  print(MDF)

      
#main_function
if __name__ == "__main__":
  print("------------------------------------EXERCISE_01----------------------------------------")
  tp = input("Enter tp: ")
  fn = input("Enter fn: ")
  fp = input("Enter fp: ")
  F1_score(tp, fp, fn)
  print()
  print("------------------------------------EXERCISE_02----------------------------------------")
  activate_func()
  print()
  print("------------------------------------EXERCISE_03----------------------------------------")
  n = input("Enter n: ")
  loss_name = input("Enter loss_func_name: ")
  loss_func(n, loss_name)
  print()
  print("------------------------------------EXERCISE_04----------------------------------------")
  x = input("Enter x: ")
  n = input("Enter n: ")
  appox_sin(x, n)
  appox_cos(x, n)
  appox_sinh(x, n)
  appox_cosh(x, n)
  print()
  print("------------------------------------EXERCISE_05----------------------------------------")
  y = input("Eneter target: ")
  _y = input("Enter predict: ")
  n = input("Enter n: ")
  p = input("Enter p: ")
  mean_diff_func(y, _y, n, p)
  
  



