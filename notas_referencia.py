print("--------------------------------------------------------")
print("                         ESCOLA                         ")
print("--------------------------------------------------------")
print("          NOTAS  /  CLASSIFICAÇOES EM NÚMEROS           ")
print("           A             900 - 1000                     ")
print("           B             800 - 890                      ")
print("           C             700 - 790                      ")
print("           D             600 - 690                      ")
print("           E             500 - 590                      ")
print("           F             ABAIXO DE 500                  ")
print("--------------------------------------------------------")
print("                        STATUS                          ")
print("--------------------------------------------------------")
nota_1 = float(input("Primeira Nota: "))
nota_2 = float(input("Segunda Nota: "))
media = (nota_1 + nota_2)/ 2
print("--------------------------------------------------------")
print("Media: ", media)
if media >= 9 and media <= 10:
    print("Aproveitamento: A")
elif media >=8 and media <= 8.9:
    print("Aproveitamento: B")
elif media >=7 and media <= 7.9:
    print("Aproveitamento: C")
elif media >=6 and media <= 6.9:
    print("Aproveitamento: D")
elif media >=5 and media <= 5.9:
    print("Aproveitamento: E")
else:
    print("Aproveitamento: F")

