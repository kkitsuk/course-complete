def password_selection(number: int, result: str):
    # Выводим результат
    for i in range(1, number):
        for j in range(i + 1, number):
            # print(i, j)
            if i >= j:
                continue
            if number % (i + j) == 0 or (i + j) == number:
                result += f"{i}{j}"

    print(f"{number} - {result}")
    return result


checked = {
    "3": "12",
    "4": "13",
    "5": "1423",
    "6": "121524",
    "7": "162534",
    "8": "13172635",
    "9": "1218273645",
    "10": "141923283746",
    "11": "11029384756",
    "12": "12131511124210394857",
    "13": "112211310495867",
    "14": "1611325212343114105968",
    "15": "1214114232133124115106978",
    "16": "1317115262143531341251161079",
    "17": "11621531441351261171089",
    "18": "12151811724272163631545414513612711810",
    "19": "118217316415514613712811910",
    "20": "13141911923282183731746416515614713812911",
}

# Проверочный модуль - перебор от 3 до 20
for number in range(1, 21):
    if number < 3 or number > 20:
        print("Допустимый диапазон от 3 до 20 (включительно)")
        continue
    result = ""
    result = password_selection(number, result)
    is_check = checked[f"{number}"] == result
    if is_check:
        print("Проход открыт")
    else:
        print(f"{is_check}\nr = {result}\nc = {checked[f"{number}"]}")


# При number = 9
# При диапазоне j от 1 до 20 - 152 активации цикла с j
# При диапазоне j от i + 1 до 20 - 116 активации цикла с j
# При диапазоне j от 1 до number - 64 активации цикла с j
# При диапазоне j от i + 1 до number - 28 активации цикла с j
