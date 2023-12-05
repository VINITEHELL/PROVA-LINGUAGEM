Contagem = 0
Cont1 = 0 #facebook
Cont2 = 0 #instagram
Cont3 = 0 #twitter
IdadeMaior1 = 0 #Idade da pessoa mais velha que prefere facebook
IdadeMaior2 = 0 #Idade da pessoa mais velha que prefere instagram
IdadeMaior3 = 0 #Idade da pessoa mais velha que prefere twitter
IdadeMenor1 = 1000 #Idade da pessoa mais nova que prefere facebook
IdadeMenor2 = 1000 #Idade da pessoa mais nova que prefere instagram
IdadeMenor3 = 1000 #Idade da pessoa mais nova que prefere twitter
ContM1 = 0
ContM2 = 0
ContM3 = 0
ContF1 = 0
ContF2 = 0
ContF3 = 0


while True:
    Contagem = Contagem + 1
    Animal = int(input("Qual sua rede social favorita?(1-Facebook,2-instagram,3-Twitter)"))
    Idade = int(input("Qual sua idade?"))
    Sexo = (input("Qual seu Sexo?(M-Masculino, F-Feminino)"))
    Parar = input("Deseja parar o formulário? (S , N)")
    

    if Animal == 1:
        Cont1 = Cont1 + 1
    elif Animal == 2:
        Cont2 = Cont2 + 1
    elif Animal == 3:
        Cont3 = Cont3 + 1

    if Animal == 1 and Idade > IdadeMaior1:
        IdadeMaior1 = Idade
    if Animal == 2 and Idade > IdadeMaior2:
        IdadeMaior2 = Idade
    if Animal == 3 and Idade > IdadeMaior1:
        IdadeMaior3 = Idade

    if Animal == 1 and Idade < IdadeMenor1:
        IdadeMenor1 = Idade
    if Animal == 2 and Idade < IdadeMenor2:
        IdadeMenor2 = Idade
    if Animal == 3 and Idade < IdadeMenor3:
        IdadeMenor3 = Idade

    if Sexo == "M" and Animal == 1:
        ContM1 = ContM1 + 1
    if Sexo == "M" and Animal == 2:
        ContM2 = ContM2 + 1
    if Sexo == "M" and Animal == 3:
        ContM3 = ContM3 + 1

    if Sexo == "F" and Animal == 1:
        ContF1 = ContF1 + 1
    if Sexo == "F" and Animal == 2:
        ContF2 = ContF2 + 1
    if Sexo == "F" and Animal == 3:
        ContF3 = ContF3 + 1
    if Parar == "S":



 # 1-Pergunta
        print("Total de respondentes foi de:",Contagem)
# 2-Pergunta
        Pergunta2 = (Cont1/Contagem) * 100
        print(Pergunta2,"% das pessoas preferem facebook")
# 3-Pergunta
        Pergunta3 = (Cont2/Contagem) * 100
        print(Pergunta3, "% das pessoas preferem instagram")
# 4-Pergunta
        Pergunta4 = (Cont3/Contagem) * 100
        print(Pergunta4,"% das pessoas preferem facebook")
# 5-Pergunta
        print("Idade da pessoa mais velha que preferiu facebook foi de:",IdadeMaior1," Anos")
# 6-Pergunta
        print("Idade da pessoa mais velha que preferiu instagram foi de:",IdadeMaior2," Anos")
# 7-Pergunta
        print("Idade da pessoa mais velha que preferiu twitter foi de:",IdadeMaior3," Anos")
# 8-Pergunta
        print("Idade da pessoa mais nova que prefiriu facebook foi de:" ,IdadeMenor1 ," Anos")
# 9-Pergunta    
        print("Idade da pessoa mais nova que prefiriu instagram foi de:" ,IdadeMenor2 ," Anos")
# 10-Pergunta
        print("Idade da pessoa mais nova que prefiriu twitter foi de:" ,IdadeMenor3 ," Anos")
# 11,13,15-Pergunta
        print("Quantidade de homens que escolheram facebook:",ContM1," ,instagram:",ContM2," e twitter:",ContM3)
# 12,14,16-Pergunta
        print("Quantidade de mulheres que escolheram facebook:",ContF1," ,instagram:",ContF2," e twitter:",ContF3)  

        if IdadeMenor1 == 1000:
            IdadeMenor1 = 0
        if IdadeMenor2 == 1000:
            IdadeMenor2 = 0
        if IdadeMenor3 == 1000:
            IdadeMenor3 = 0
            