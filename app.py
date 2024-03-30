def convert_to_snake_case(pascal_string):
     snakecased_charlist = [
		'_' + char.lower() if char.isupper()
  else char
  for char in pascal_string
	]
     return ''.join(snakecased_charlist).strip('_')



def main():
     print(convert_to_snake_case('ThisIsMyComplexPascalStringBlaBlaYesYesHaHa'))
     
if __name__ == '__main__':
     main()