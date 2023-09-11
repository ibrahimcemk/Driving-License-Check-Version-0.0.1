name = input ("Please Enter Your Name.")
age = int(input ("Please Enter Your Age. "))

if (age < 16):
    print (f"{name}, If you are under 16 years old, you cannot get a driver's license.")
else:
  education = input ('Please Enter Your Education Status: "Primary school", "Middle school", "High School", "Undergraduate", "Master Degree","Ph. D." ,"Associate Degree"')
  if (education == "Primary school" or education == "Middle school"):
    print (f"{name}, You did not receive it because your education is not sufficient.")
  else:
    print (f"{name}, You Can Get a Driver's License")

    input("break")   
      
