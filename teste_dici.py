import pickle
def adcionar(codigo,tipo,titular,data):
    with open("Banco de dados.pkl","rb") as arquivo:
        recuperar= pickle.load(arquivo)
    recuperar.append({'codigo': codigo, 'tipo': tipo, 'titular':titular, 'data': data})
    with open("Banco de dados.pkl", "wb") as arquivo:
        pickle.dump(recuperar,arquivo)
def remover(codigo):
    with open("Banco de dados.pkl","rb") as arquivo:
        recuperar= pickle.load(arquivo)
    for i in recuperar:
        if codigo in i['codigo']:
            recuperar.remove(i)
    with open("Banco de dados.pkl", "wb") as arquivo:
        pickle.dump(recuperar,arquivo)
def pesquisa(codigo):
    with open("Banco de dados.pkl","rb") as arquivo:
        recuperar= pickle.load(arquivo)
    for i in recuperar:
        if codigo in i['codigo']:
            print(i)
def listar(escolha):
    with open("Banco de dados.pkl","rb") as arquivo:
        recuperar= pickle.load(arquivo)
    if escolha=="1":
        mostrar=sorted(recuperar, key=lambda x: x['codigo'])
        for i in mostrar:
            print(i['codigo'],"\t",i['tipo'],"\t",i['titular'],"\t",i['data'])
    elif escolha=="2":
        mostrar=sorted(recuperar, key=lambda x: x['tipo'])
        for i in mostrar:
            print(i['codigo'],"\t",i['tipo'],"\t",i['titular'],"\t",i['data'])
    elif escolha=="3":
        mostrar=sorted(recuperar, key=lambda x: x['titular'])
        for i in mostrar:
            print(i['codigo'],"\t",i['tipo'],"\t",i['titular'],"\t",i['data'])
    elif escolha=="4":
        mostrar=sorted(recuperar, key=lambda x: x['data'])
        for i in mostrar:
            print(i['codigo'],"\t",i['tipo'],"\t",i['titular'],"\t",i['data'])