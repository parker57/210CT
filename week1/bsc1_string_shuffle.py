def string_shuffle(str1,str2):
  len1 = len(str1)
  len2 = len(str2)

  comb_str = ''
  short_str = min(len1,len2)
  long_str = max(len1,len2)

  for i in range(short_str):
    comb_str += str1[i]
    comb_str += str2[i]

  comb_str+=max(str1,str2, key=len)[short_str:long_str]
  return comb_str

  
