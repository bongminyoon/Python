while True:
    try:
        value = float(input("변환하고자 하는 값을 입력하세요:  "))
        unit = input("변환하고자 하는 단위를 입력하세요:  ")

        if unit == "C":
            print("{0:.2f}℉".format(fahrenheit))
        elif unit == "℉":
            celsius = (value - 32) * 5/9
            print("{0:.2f}℃".format(celsius))
        elif unit == "m":
            feet = value * 3.281
            print("{0:.2f}ft".format(feet))
        elif unit == "ft":
            meter = value / 3.281
            print("{0:.2f}m".format(meter))
        else:
            print("잘못된 입력입니다. 다시 시도해주세요.")
        
        answer = input("다시 변환하시겠습니까? (Y/N)").upper()
        if answer == "N":
            break
    except ValueError:
        print("잘못된 입력입니다. 다시 시도해주세요.")
