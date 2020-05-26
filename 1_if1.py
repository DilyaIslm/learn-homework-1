age = (input('Сколько Вам лет?'))
p = age
def main():
  p = 25
  if p < 6:
   print ("Вам нужно ходить в детский сад!")
  elif 18 > p > 7:
   print ("Вам нужно ходить в школу")
  elif 18 < p < 22:
   print ("Вам нужно ходить в ВУЗ")
  else:
   print ("Вам пора работать!")  
    
pass

if __name__ == "__main__":
  main()
