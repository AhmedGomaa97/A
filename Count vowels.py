
def count_vowels(input_string): 
  vowels = "uaeioUAEIO"
  vowel_count=0
  for char in input_string :
    if char in vowels :
       vowel_count += 1 
  return vowel_count

input_string = "Hello, World!"
result = count_vowels(input_string)
print("Number of vowels:", result)
















