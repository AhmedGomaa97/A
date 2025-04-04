def print_i_location(input_string):
  for index in range(len(input_string)):
    if input_string[index] == 'I' :
      print(f" 'I' found at index:{index} ")

input_string = "ALI"
print_i_location(input_string)