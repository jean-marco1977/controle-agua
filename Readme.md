# 💰 Desconto de Produtos sem registro

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![GitHub](https://img.shields.io/badge/github-8da0cb?style=for-the-badge&labelColor=555555&logo=github)

## 📝 Sobre o Projeto
Este é um script simples em **Python** desenvolvido para calcular o consumo de água de um imóvel e lhe dizer se o consumo está dentro dos padrões. 

---

## 🧮 Fórmula Utilizada
A fórmula deste é bem simples, não tem muitas complicações:

1. **Aplicação do tipo de Imóvel**
   \[\text{Imóvel} = {\text{Comercial} | \text{Apartamento} | \text{Casa}}\]

2. **Definição de consumo de água**
   \[\text{10/m³} = {\text{Moderado}}\]

---

## 📂 Estrutura do Código
O programa foi construído com a seguinte lógica em Python (`Jean_Ag7_DS_I.py`):

```python
# Declaração de variaveis para o projeto do Desconto de compras

Imovel = input("Qual imovel é o desejado (Apartamento, Casa, Comercial): ")
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
```

---

## 🚀 Como Executar o Programa

### Pré-requisitos
Antes de começar, você vai precisar ter o **Python 3.x** instalado em sua máquina.

### Passo a Passo

1. **Clone o repositório** (ou baixe o arquivo `Jean_Ag7_DS_I.py`):
   ```bash
   git clone https://github.com/jean-marco1977/Desconto/blob/main/Jean_Ag6_DS_I.py
   ```

2. **Navegue até a pasta** do projeto:
   ```bash
   cd nome-do-repositorio
   ```

3. **Execute o script** pelo terminal ou prompt de comando:
   ```bash
   python Jean_Ag7_DS_I.py
   ```

4. **Interaja com o terminal** inserindo o valor do que foi gasto.
