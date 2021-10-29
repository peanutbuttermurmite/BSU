import time,sys
def out(message,color="white",speed=7,underline=False,bold=False,italic=False,loadTime=20):
  if color=="white":
    sys.stdout.write("\033[0m")
    sys.stdout.flush()
  elif color=="gray":
    sys.stdout.write("\033[37m")
    sys.stdout.flush()
  elif color=="red":
    sys.stdout.write("\033[31m")
    sys.stdout.flush()
  elif color=="green":
    sys.stdout.write("\033[32m")
    sys.stdout.flush()
  elif color=="yellow":
    sys.stdout.write("\033[33m")
    sys.stdout.flush()
  elif color=="blue":
    sys.stdout.write("\033[34m")
    sys.stdout.flush()
  elif color=="purple":
    sys.stdout.write("\033[35m")
    sys.stdout.flush()
  else:
    sys.stdout.write("\033[31mHey! That's not a supported color!\033[0m")
  if underline:
    sys.stdout.write("\033[4m")
    sys.stdout.flush()
  if bold:
    sys.stdout.write("\033[1m")
    sys.stdout.flush()
  if italic:
    sys.stdout.write("\033[3m")
    sys.stdout.flush()
  remove=False
  removeChar=0
  for l in str(message):
    if (l=="*"):
      remove=not(remove)
      if (not(remove)):
        for x in range(0,removeChar):
          sys.stdout.write("\b")
          sys.stdout.flush()
          time.sleep(speed/50)
        time.sleep(speed/50)
    elif (l=="~"):
      sys.stdout.write("|")
      sys.stdout.flush()
      time.sleep(speed/100)
      for x in range(0,loadTime):
        sys.stdout.write("\b/")
        sys.stdout.flush()
        time.sleep(speed/100)
        sys.stdout.write("\b-")
        sys.stdout.flush()
        time.sleep(speed/100)
        sys.stdout.write("\b\\")
        sys.stdout.flush()
        time.sleep(speed/100)
        sys.stdout.write("\b|")
        sys.stdout.flush()
        time.sleep(speed/100)
      sys.stdout.write("\b")
      sys.stdout.flush()
    else:
      sys.stdout.write(l)
      sys.stdout.flush()
      time.sleep(speed/100)
      if (remove):
        removeChar+=1
      if (l==","):
        time.sleep(speed/50)
      elif (l=="."):
        time.sleep(speed/25)
      elif (l==";"):
        time.sleep(speed/25)
  sys.stdout.write("\033[0m")
  sys.stdout.flush()

def s(color):
  if color=="reset":
    return ("\033[0m")
  elif color=="gray":
    return ("\033[37m")
  elif color=="red":
    return ("\033[31m")
  elif color=="green":
    return ("\033[32m")
  elif color=="yellow":
    return ("\033[93m")
  elif color=="blue":
    return ("\033[34m")
  elif color=="purple":
    return ("\033[35m")
  elif color=="bold":
    return ("\033[1m")
  elif color=="italic":
    return ("\033[3m")
  elif color=="select":
    return ("\033[7m")
  elif color=="uline":
    return ("\033[4m")