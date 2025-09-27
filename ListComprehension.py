def convert_to_snake_case(pascal_or_camel_cased_string):
    return ''.join(
        '_' + char.lower() if char.isupper() else char
        for char in pascal_or_camel_cased_string
    ).strip('_')

def main():
    print(convert_to_snake_case('aLongAndComplexString'))

main()