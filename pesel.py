pesel = input("Wpisz PESEL: ")

if len(pesel) == 11:
    sum = (int(pesel[0]) * 1) + (int(pesel[1]) * 3) + (int(pesel[2]) * 7) + (int(pesel[3]) * 9) + (int(pesel[4]) * 1) + \
          (int(pesel[5]) * 3) + (int(pesel[6]) * 7) + (int(pesel[7]) * 9) + (int(pesel[8]) * 1) + (int(pesel[9]) * 3) + \
          (int(pesel[10])* 1)

    str_sum = str(sum)

    if sum > 0:
        if str_sum[len(str_sum)-1] == "0":
            print("D")
        else:
            print("N")
else:
    print("N")