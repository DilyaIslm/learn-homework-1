line1 = str (12345)
line2 = str (1234567)

def main(line1,line2):
    print (f"line1":{line1}, f"line2":{line2})

    if type (line1) == str and isinstance (line2, str):
      return "0"
    if line1 == line2:
      return "1"
    if line1 != line2 and len(line1)> len(line2):
      return "2"
    if line1 != line2 and line2 == "learn":
      return "3"    
  
    if __name__ == "__main__":
      main('line1','line2')
