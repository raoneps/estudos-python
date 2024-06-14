#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Versão do Python neste projeto
from platform import python_version as pv
print("Versão do Python usada neste Jupyter notebook: ", pv())


# > **Cauculadora Simples - Versão 1.0**

# In[22]:


print("----------CALCULADORA PYTHON 1.0----------\n")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operator = input("Escolha a operação: + , - , * , / ")

if operator == '+':
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
else:
    print("Operador inválido")
   
print("Primeiro número: ", num1)
print("Segundo número: ", num2)
print("Operador ", operator)
print("Resultado: ", int(result))


# In[ ]:





# In[ ]:




