import lexer
while True:
    text = input('Shell> ')
    if text == 'q' or text == 'Q': break
    result, error = lexer.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)