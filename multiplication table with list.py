
def generate_multiplication_tables(number):
 
  big_list = []
  for i in range(1, number + 1):
    small_list = []
    for j in range(1, i + 1):
      small_list.append(f"{i * j}")
    big_list.append(small_list)
  return big_list
tables = generate_multiplication_tables(5)
print(tables)