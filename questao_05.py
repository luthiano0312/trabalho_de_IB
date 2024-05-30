hora = int(input("informe a hora: "))

if 5<hora<13:
    print("agora é manhã")
elif 12<hora<19:
    print("agora é tarde")
elif 18<hora<24 or -1<hora<6:
    print("agora é noite")
else:
    print("essa hora não existe")