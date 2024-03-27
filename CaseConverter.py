print('\n---------- Case Converter ----------')
initial = input('From PascalCase or camelCase: ')

def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]
    return ''.join(snake_cased_char_list).strip('_')

def main():
    print('To snake_case: ',convert_to_snake_case(initial))


if __name__ == '__main__':
    main()

print ('-'*40+'\n')
