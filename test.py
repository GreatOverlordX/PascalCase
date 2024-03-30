# Same as app.py but with for loop instead of List Comprehension

def convert_to_snake_case(pascal_string):
     snakecased_charlist = []
     for char in pascal_string:
          if char.isupper():
               converted_character = '_' + char.lower()
               snakecased_charlist.append(converted_character)
          else:
               snakecased_charlist.append(char)
     snakecased_string = ''.join(snakecased_charlist)
     clean_snakecased_string = snakecased_string.strip('_')
     return clean_snakecased_string

def main():
     print(convert_to_snake_case('BlaBlaComplexPascalStringHahaHaha'))
     
if __name__ == '__main__':
	main()