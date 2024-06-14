#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Versão do Python neste projeto
from platform import python_version as pv
print("Versão do Python usada neste Jupyter notebook: ", pv())


# > **Cauculadora Simples - Versão 2.0**

# In[20]:


print("\n----------CALCULADORA PYTHON 2.0----------\n")

# Criando funções para as operações
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def mutiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Imprimindo menu para usuário escolher a operação

print("\n Selecione o número da operação desejada: \n")
print("1 - Soma (+) ")
print("2 - Subtração (-) ")
print("3 - Multiplicação (*) ")
print("4 - Divisão (/) ")

choice = input("\nDigite sua opção (1/2/3/4): ")

num1 = int(input("\nDigite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

    
if choice == "1":
    print("\n")
    print(num1, "+", num2, "=", add(num1, num2))
    print("\n")

elif choice == "2":
    print("\n")
    print(num1, "-", num2, "=", subtract(num1, num2))
    print("\n")

elif choice == "3":
    print("\n")
    print(num1, "*", num2, "=", mutiply(num1, num2))
    print("\n")

elif choice == "4":
    print("\n")
    print(num1, "/", num2, "=", divide(num1, num2))
    print("\n")
    
else:
    print("\nOpção Inválida! ")


# In[ ]:





# In[ ]:




