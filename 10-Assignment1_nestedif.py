sec=int(input("enter security code"))
if sec==5566:
  dept=str(input("enter department"))
  if dept.lower()=="finance":
    level=int(input("enter access level"))
    if level>=5:
      print("Access granted: welcom to meeeting room")
    else:
      print("insufficient access level")  
  else:
    print("access denied: dept not allowed")
else:
  print("invalid security code")        