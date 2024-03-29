def print_text(text, encoding_type):
    byte_data = text.encode(encoding_type)
    hex_data_as_str = ' '.join(f"{hex(c)}" for c in byte_data)
    int_data_as_str = ' '.join(f"{int(c)}" for c in byte_data)

    print('\'' + text + '\' 문자열 길이: {0}'.format(len(text)))
    print('\'' + text + '\' 전체 문자를 표현하는 데 사용한 바이트 수: {0} 바이트'.format(len(byte_data)))
    print('\'' + text + '\' 16진수 값: {0}'.format(hex_data_as_str))
    print('\'' + text + '\' 10진수 값: {0}'.format(int_data_as_str))


print_text("Hello Ine", "ascii")
print('==============')
print_text("Hello Ine", "euc-kr")
print_text("아이네넴 안녕하세요", "euc_kr")
print('==============')
print_text("Hello Ine", "utf-8")
print_text("아이네넴 안녕하세요", "utf-8")
