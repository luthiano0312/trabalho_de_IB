hora = int(input("informe a hora: "))

if 0<=hora<12:
    print("agora é manhã")
elif 11<hora<18:
    print("agora é tarde")
elif 17<hora<24:
    print("agora é noite")
else:
    print("essa hora não existe")