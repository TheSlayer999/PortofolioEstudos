dia=int(input("Introduz o dia da semana: "))

""" match dia:
    case 1:print("Dia da semana")
    case 2:print("Dia da semana")
    case 3:print("Dia da semana")
    case 4:print("Dia da semana")
    case 5:print("Dia da semana")
    case 6:print("Fim de semana")
    case 7:print("Fim de semana")
    case _:print("Dia inválido")
 """

match dia:
    case 1|2|3|4|5: print("Dia de semana")
    case 6|7: print("Fim de semana")
    case _:print("Dia inválido")