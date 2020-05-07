f_sequence= int(input("Enter the number of terms you want the sequence to run for: "))
s_num,e_num=0,1
count=0

while count < f_sequence:
  print(s_num)
  f_num = s_num + e_num
  s_num = e_num
  e_num = f_num
  count += 1
