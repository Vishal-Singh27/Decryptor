def get_int(txt):
    while True:
        try:
            num = int(input(txt))
            return num
        except ValueError:
            continue