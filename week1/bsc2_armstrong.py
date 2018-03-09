def is_Armstrong(num):
  s_num = str(num)
  n_length = len(s_num)
  
  if (n_length!=3):
    raise ValueError("Exercise asks for 3 digit numbers")
  
  summed_cubes = 0
  
  for i in range (n_length):
    summed_cubes += (int(s_num[i])**n_length)

  if (summed_cubes == num):
    return True
  
  return False
    
