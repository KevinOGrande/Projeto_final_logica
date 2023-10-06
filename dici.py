import teste_dici as t
while True:
    escolha= input("1)Adicionar documento\n2)Remover documento\n3)Pesquisar documento\n:")
    if escolha=="1":
        codigo=input("Digite o codigo do documento:")
        tipo=input("Digite o tipo do documento:")
        titular= input("Digite o titular do documento: ")
        data= input("Digite a data do documento:")
        t.adcionar(codigo,tipo,titular,data)
    elif escolha=="2":
        codigo=input("Digite o codigo:")
        t.remover(codigo)
    elif escolha=="3":
        codigo=input("Digite o condigo do documento:")
        t.pesquisa(codigo)
    elif escolha=="4":
        escolha=input("1)Codigo\n2)tipo de documento\n3)titular do documento\n4)data\n:")
        t.listar(escolha)