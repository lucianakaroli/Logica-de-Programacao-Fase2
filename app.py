#Projeto dados meterologicos Porto Alegre de 1960 a 2016.

#Parte 1:
#a) informar o usuário o periodo que deseja ver com mes e ano inicial e final.
#b) ver todos os dados.
#c) apenas os de precipitacao.
#d) apenas os de temperatura.
#e) apenas os de umidade e vento.

#Parte 2:
#a) informar o mes mais chuvoso.
#b) média da temperatura minima de um determinado mes (auge do inverno) de 2006 a 2016.
#c) gráfico de barras media temperatura minima de um determinado mes de 2006 a 2016.
#d) media geral da temperatura minima de um determinado mes de 2006 a 2016.


import matplotlib.pyplot as plt
import random
import datetime

# Leitura do arquivo

def cargaDados(nome ="anexo-arquivo.csv"):
  arquivo = open(nome, "r")
  dados = []
  for linha in arquivo:
    #print(linha)
    linha1 = linha[:-1] #retira \n
    dados.append(linha1)
  for coluna in arquivo:
    print(coluna)
    coluna = coluna[:-1] #retira \n
  arquivo.close()
  return dados


# Transformando e estruturando os dados em tuplas
def transformaDados(linha):
  itens = linha.split(",")
  itensTransformados = [itens[0]] #Data foi colocado na lista
  cont = 1
  while cont<len(itens):
    itensTransformados.append(float(itens[cont])) #Converte para float demais itens
    cont = cont + 1
  return itensTransformados


# Lista de lista com os dados

def tranformaLista(lista):
  listaDeItens = []
  cont = 1 #Pula o cabecalho

  cabecalho = lista[0]
  while cont<len(lista):
    listaDeItens.append(transformaDados(lista[cont]))
    cont = cont + 1
  return listaDeItens, cabecalho


# Quebra data

def quebraData(data):
    quebrado = data.split('/')
    mes = quebrado[1]
    ano = quebrado[2]
    return int(mes), int(ano)


# Imprime todos os dados
def imprimeTodosDados(lista, mesInicial, mesFinal, anoInicial, anoFinal):
  i = 0
  while i < len(lista):
    valorData = lista[i][0]
    data = quebraData(valorData)
    ano = data[1]
    mes = data[0]
    date_valor_lista = datetime.date(ano, mes, 1)
    date_inicio = datetime.date(anoInicial, mesInicial, 1)
    date_final = datetime.date(anoFinal, mesFinal, 1)

    if date_valor_lista >= date_inicio and date_valor_lista <= date_final:
      print(lista[i][0], lista[i][1], lista[i][2], lista[i][3], lista[i][4], lista[i][5], lista[i][6], lista[i][7])
    i += 1


# Imprime precipitacao
def imprimePrecipitacao(lista, mesInicial, mesFinal, anoInicial, anoFinal):
  i = 0
  while i < len(lista):
      valorData = lista[i][0]
      data = quebraData(valorData)
      ano = data[1]
      mes = data[0]
      date_valor_lista = datetime.date(ano, mes, 1)
      date_inicio = datetime.date(anoInicial, mesInicial, 1)
      date_final = datetime.date(anoFinal, mesFinal, 1)
      i+=1
    
  i = 0
  while i < len(lista):
    date_valor_lista = datetime.datetime.strptime(lista[i][0], '%d/%m/%Y').date()
    if date_valor_lista >= date_inicio and date_valor_lista <= date_final:
        print(lista[i][1])
    i += 1



# Imprime temperatura

def imprimeTemperatura(lista, mesInicial, mesFinal, anoInicial, anoFinal):
  i = 0
  while i < len(lista):
    valorData = lista[i][0]
    data = quebraData(valorData)
    ano = data[1]
    mes = data[0]
    date_valor_lista = datetime.date(ano, mes, 1)
    date_inicio = datetime.date(anoInicial, mesInicial, 1)
    date_final = datetime.date(anoFinal, mesFinal, 1)

    if date_valor_lista >= date_inicio and date_valor_lista <= date_final:
      print(lista[i][2], lista[i][3], lista[i][5])
    i += 1


# Imprime umidade e vento

def imprimeUmidadeVento(lista, mesInicial, mesFinal, anoInicial, anoFinal):
  i = 0
  while i < len(lista):
    valorData = lista[i][0]
    data = quebraData(valorData)
    ano = data[1]
    mes = data[0]
    date_valor_lista = datetime.date(ano, mes, 1)
    date_inicio = datetime.date(anoInicial, mesInicial, 1)
    date_final = datetime.date(anoFinal, mesFinal, 1)

    if date_valor_lista >= date_inicio and date_valor_lista <= date_final:
      print(lista[i][6], lista[i][7])
    i += 1


# Mes mais chuvoso
def mesMaisChuvoso(lista, mesInicial, mesFinal, anoInicial, anoFinal):

  imprimeMesChuvoso = {
      "mes": 0,
      "ano": 0,
      "maior": 0
  }
  i = 0
  precipitacao = 0
  while i < len(lista):
    valorData = lista[i][0]
    data = quebraData(valorData)
    ano = data[1]
    mes = data[0]
    precipitacao = lista[i][1]
    if precipitacao > imprimeMesChuvoso["maior"]:
      imprimeMesChuvoso["maior"] = precipitacao
      imprimeMesChuvoso["mes"] = mes
      imprimeMesChuvoso["ano"] = ano
    i += 1
  print("Mes, ano, precipitacao: " , imprimeMesChuvoso["mes"], imprimeMesChuvoso["ano"], imprimeMesChuvoso["maior"])


#Media das temperaturas minimas (auge do inverno) de 2006 a 2016

def mediaDasTemperaturasMinimas(lista):
  dataMes, mes = escolheMesInverno()

  mediaTempMinima = salvaMediasMesesInverno(lista, dataMes)

  for anoFor in range(2006, 2017):
    chave = mes + str(anoFor)
    if chave in mediaTempMinima.keys():
      print("Media temperatura do mes: " , mes, anoFor, mediaTempMinima[chave])


#Grafico de barras media de temperaturas minimas

def escolheMesInverno():
  print("Escolha um numero para a opcao: ")
  print("1. Junho.")
  print("2. Julho.")
  print("3. Agosto")
  dataMes = int(input("Digite o numero do mes para saber a temperatura minima: "))
  while dataMes < 1 or dataMes > 3:
      dataMes = int(input("Número inválido, por favor, digite um valor entre 1 e 3: "))
  if dataMes == 1:
    print("Mes escolhido foi Junho.")
    return dataMes, "junho"
  if dataMes == 2:
    print("Mes escolhido foi Julho.")
    return dataMes, "julho"
  if dataMes == 3:
    print("Mes escolhido foi Agosto.")
    return dataMes, "agosto"


def salvaMediasMesesInverno(lista, dataMes):
  mediaTempMinima = {}

  i = 0
  while i < len(lista):
    valorData = lista[i][0]
    data = quebraData(valorData)
    ano = data[1]
    mes = data[0]
    tempMinima = lista[i][3]
    if ano >= 2006 and ano <= 2016:
      if dataMes == 3 and mes == 8:
        chaveSoma = "agosto" + str(ano) + "_soma"
        chaveCount = "agosto" + str(ano) + "_count"
        chaveMedia = "agosto" + str(ano)

        if chaveSoma in mediaTempMinima.keys():
          mediaTempMinima[chaveSoma] = mediaTempMinima[chaveSoma] + tempMinima
          mediaTempMinima[chaveCount] = mediaTempMinima[chaveCount] + 1
        else:
          mediaTempMinima[chaveSoma] = tempMinima
          mediaTempMinima[chaveCount] = 1

        mediaTempMinima[chaveMedia] = mediaTempMinima[chaveSoma] / mediaTempMinima[chaveCount]

      if dataMes == 2 and mes == 7:
        chaveSoma = "julho" + str(ano) + "_soma"
        chaveCount = "julho" + str(ano) + "_count"
        chaveMedia = "julho" + str(ano)

        if chaveSoma in mediaTempMinima.keys():
          mediaTempMinima[chaveSoma] = mediaTempMinima[chaveSoma] + tempMinima
          mediaTempMinima[chaveCount] = mediaTempMinima[chaveCount] + 1
        else:
          mediaTempMinima[chaveSoma] = tempMinima
          mediaTempMinima[chaveCount] = 1

        mediaTempMinima[chaveMedia] = mediaTempMinima[chaveSoma] / mediaTempMinima[chaveCount]

      if dataMes == 1 and mes == 6:
        chaveSoma = "junho" + str(ano) + "_soma"
        chaveCount = "junho" + str(ano) + "_count"
        chaveMedia = "junho" + str(ano)

        if chaveSoma in mediaTempMinima.keys():
          mediaTempMinima[chaveSoma] = mediaTempMinima[chaveSoma] + tempMinima
          mediaTempMinima[chaveCount] = mediaTempMinima[chaveCount] + 1
        else:
          mediaTempMinima[chaveSoma] = tempMinima
          mediaTempMinima[chaveCount] = 1
        
        mediaTempMinima[chaveMedia] = mediaTempMinima[chaveSoma] / mediaTempMinima[chaveCount]

    i+=1

  return mediaTempMinima

# Media geral da temperatura minima de um determinado mes

def mediaGeralTemperaturaMinima(lista):
  dataMes, mes = escolheMesInverno()
  mediaTempMinima = salvaMediasMesesInverno(lista, dataMes)
  mediaTotal = 0
  count = 0
  for anoFor in range(2006, 2017):
    chave = mes + str(anoFor)
    if chave in mediaTempMinima.keys():
      mediaTotal += mediaTempMinima[chave]
      count +=1

  print("Média total do mes de ", mes, " é: ", (mediaTotal/count))

def geraGrafico(lista):
  dataMes, mes = escolheMesInverno()
  mediaTempMinima = salvaMediasMesesInverno(lista, dataMes)
  
  chaves = []
  valores = []
  for anoFor in range(2006, 2017):
    chave = mes + str(anoFor)
    if chave in mediaTempMinima.keys():
      chaves.append(anoFor)
      valores.append(mediaTempMinima[chave])

  plt.bar(chaves, valores, color="blue")
  plt.title("Media das temperaturas minimas em um determinado mes " , color="blue")
  plt.xlabel("Ano", color="blue")
  plt.ylabel("Media", color="blue")
  plt.show()


#MenuDatas

meses = {}


def dadosMenu(lista, cabecalho):
  mesInicial = int(input("Informe o mes inicial (1 a 12): "))
  while mesInicial < 1 or mesInicial > 12:
    print("Mes invalido.")
    mesInicial = int(input("Digite novamente o mes inicial: "))

  mesFinal = int(input("Informe o mes final (1 a 12): "))
  while mesFinal <1 or mesFinal > 12:
    print("Mes invalido.")
    mesFinal = int(input("Digite novamente o mes final: "))

  anoInicial = int(input("Informe o ano inicial (1960 a 2016): "))
  while anoInicial < 1960 or anoInicial > 2016:
    print("Ano invalido")
    anoInicial = int(input("Digite novamente o ano inicial: "))

  anoFinal = int(input("Informe o ano final(1960 a 2016): "))
  while anoFinal < 1960 or anoFinal > 2016 or anoInicial > anoFinal:
    print("Ano invalido, o ano deve ser >= 1960 e <= 2016 e maior que o ano inicial")
    anoFinal = int(input("Digite novamente o ano final: "))


# Menu opcoes

  print("Escolha uma opcao: ")
  print("1. Ver todos os dados. ")
  print("2. Apenas os de precipitacao.")
  print("3. Apenas os de temperatura (máxima, mínima e media.) ")
  print("4. Apenas os de umidade e vento.")
  print("Ou você ainda pode escolher: ")
  print("5. Mes mais chuvoso.")
  print("6. Média da temperatura mínima de um determinado mês (auge do inverno).")
  print("7. Gráfico de barras com as médias de temperatura mínima de um determinado mês.")
  print("8. Média geral da temperatura mínima de um determinado mês.")
  opcao = int(input(" Digite o numero para opcao: "))
  while opcao < 1 or opcao > 8:
    opcao = int(input("Opcao invalida, Digite o numero de 1 a 8 para opcao: "))
  if opcao == 1:
    print("Ver todos os dados: ")
    print(cabecalho)
    imprimeTodosDados(lista, mesInicial, mesFinal, anoInicial, anoFinal)
  if opcao == 2:
    print("Apenas os de precipitacao: ")
    imprimePrecipitacao(lista, mesInicial, mesFinal, anoInicial, anoFinal)
  if opcao == 3:
    print("Apenas os de temperatura (máxima, mínima e média): ")
    imprimeTemperatura(lista, mesInicial, mesFinal, anoInicial, anoFinal)
  if opcao == 4:
    print("Apenas os de umidade e vento: ")
    imprimeUmidadeVento(lista, mesInicial, mesFinal, anoInicial, anoFinal)
  if opcao == 5:
    print("Mes mais chuvoso de todos os tempos: ")
    mesMaisChuvoso(lista, mesInicial, mesFinal, anoInicial, anoFinal)
  if opcao == 6:
    print("Média da temperatura mínima: ")
    mediaDasTemperaturasMinimas(lista)
  if opcao == 7:
    print("Grafico de barras da temperatura mínima: ")
    geraGrafico(lista)
  if opcao == 8:
    mediaGeralTemperaturaMinima(lista)


lista = cargaDados("anexo-arquivo.csv")
transformada, cabecalho = tranformaLista(lista)
dadosMenu(transformada, cabecalho)

