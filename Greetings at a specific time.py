input_user = input("Que horas são? ")

if input_user.isdigit() and int:
    int_input_user = int(input_user)
    
    if int_input_user < 11:
        print("Bom dia!")
    elif 12 <= int_input_user <= 17:
        print("Boa tarde!")
    elif 18 <= int_input_user <= 23:
        print("Boa noite!")
else:
    print("Você não digitou um número válido.")