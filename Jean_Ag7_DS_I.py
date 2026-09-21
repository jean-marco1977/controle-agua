# Declaração de variaveis para o projeto do Desconto de compras

Imovel = input("Qual imovel é o desejado (Escreva uma dessas opções: Apartamento, Casa, Comercial): ")
Imovel = Imovel.lower()  # Converte a entrada para minúsculas para facilitar a comparação

# Estrutura da funcionalidade do código e resposta do programa

if Imovel == "comercial":
    print("Tarifa comercial aplicada – consulte o plano corporativo.")
elif Imovel == "apartamento":
    Consumo_agua = float(input("Qual o consumo de água em m³: "))
    if Consumo_agua < 10:
        print("Consumo econômico – excelente controle de água!")
    elif Consumo_agua >= 10 and Consumo_agua <= 25:
        print("Consumo moderado – dentro do padrão residencial.")
    elif Consumo_agua > 25:
        print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")
elif Imovel == "casa":
    Consumo_agua = float(input("Qual o consumo de água em m³: "))
    if Consumo_agua < 15:
        print("Consumo econômico – excelente controle de água!")
    elif Consumo_agua >= 15 and Consumo_agua <= 30:
        print("Consumo moderado – dentro do padrão residencial.")
    elif Consumo_agua > 30:
        print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")
else:
    print("O imovel selecionado está errado")

"""if Imovel != "Comercial" and Imovel != "comercial" and Imovel != "COMERCIAL":
    print("O imovel selecionado está errado")
elif Imovel == "Comercial" or Imovel == "comercial" or Imovel == "COMERCIAL":
    print("Tarifa comercial aplicada – consulte o plano corporativo.")
elif Imovel != "Apartamento" and Imovel != "apartamento" and Imovel != "APARTAMENTO":
    print("O imovel selecionado está errado")
elif Imovel == "Apartamento" or Imovel == "apartamento" or Imovel == "APARTAMENTO":
    Consumo_agua = float(input("Qual o consumo de água em m³: "))
    if Consumo_agua < 10:
        print("Consumo econômico – excelente controle de água!")
    elif Consumo_agua >= 10 and Consumo_agua <= 25:
        print("Consumo moderado – dentro do padrão residencial.")
    elif Consumo_agua > 25:
        print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")
elif Imovel != "Casa" and Imovel != "casa" and Imovel != "CASA":
    print("O imovel selecionado está errado")
elif Imovel == "Casa" or Imovel == "casa" or Imovel == "CASA":
    Consumo_agua = float(input("Qual o consumo de água em m³: "))
    if Consumo_agua < 15:
        print("Consumo econômico – excelente controle de água!")
    elif Consumo_agua >= 15 and Consumo_agua <= 30:
        print("Consumo moderado – dentro do padrão residencial.")
    elif Consumo_agua > 30:
        print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")"""

        
"""if Imovel == "Apartamento" or Imovel == "apartamento" or Imovel == "APARTAMENTO":
    if Consumo_agua < 10:
        print("Consumo econômico – excelente controle de água!")
    elif Consumo_agua >= 10 and Consumo_agua <= 25:
        print("Consumo moderado – dentro do padrão residencial.")
    elif Consumo_agua > 25:
        print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")
    else:
        print("O imovel selecionado está errado")
if Imovel == "Casa" or Imovel == "casa" or Imovel == "CASA":
    if Consumo_agua < 10:
        print("Consumo econômico – excelente controle de água!")
    elif Consumo_agua >= 10 and Consumo_agua <= 25:
        print("Consumo moderado – dentro do padrão residencial.")
    elif Consumo_agua > 25:
        print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")
    else:
        print("O imovel selecionado está errado")"""