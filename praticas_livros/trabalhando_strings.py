# A função len () retorna o tamanho de uma string
# Se a sting for vazia, por examplo "", o resultado será 0
# Lembrar de voltar e tratar as validações do código
# Por exemplo, no código abaixo, no idioma PT-BR não existe 
# Palavra com uma letra só.


n = input ('Digite uma palavra: \n\n')

print('VOCÊ DIGITOU: ', n)
print ('A palavra', n, 'tem', len(n), 'letras')

print ('A primeria letra é: ', n[0])
print ('A ultima letra é: ',  n[-1])

# Agora estou testando outro pedaço de código pra brincar com datas e separadores
# Tambem é preciso fazer validação dos campos de data

def validar_numero():
    while True:
        dia = input('Digite o DIA do seu nascimento: [2 digitos] ')
        mes = input('Digite o MÊS do seu nascimento: [2 digitos] ')
        ano = input('Digite o ANO do seu nascimento: [4 digitos] ')

        if not dia.isdigit():
            print("Oops!  O dia deve conter apenas números.  Tente novamente...")
            continue
        if not mes.isdigit():
            print("Oops!  O mês deve conter apenas números.  Tente novamente...")
            continue
        if not ano.isdigit():
            print("Oops!  O ano deve conter apenas números.  Tente novamente...")
            continue

        if len(dia) != 2:
            print("Oops!  O dia deve ter 2 dígitos.  Tente novamente...")
            continue
        if len(mes) != 2:
            print("Oops!  O mês deve ter 2 dígitos.  Tente novamente...")
            continue
        if len(ano) != 4:
            print("Oops!  O ano deve ter 4 dígitos.  Tente novamente...")
            continue

        break

    print("Você nasceu em: ", dia, mes, ano, sep="/")

validar_numero()

