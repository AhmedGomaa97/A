def generate_multiplication_table(number):
  for i in range(1, number+1) :
    for j in range(1,i+1) :
       print(f"{i} x {j} = {i*j}") 
number=3
generate_multiplication_table(number)