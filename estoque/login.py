#Criar campos de entrada para receber login e senha.
#Conferir se credenciais já estão cadastradas para acesso.
#Permitir cadastro de novos usuários.
      
mail_login = input ('Digite seu email: ')
pass_login = input ('Digite sua senha: ')



if mail_login in cadastro_lista and pass_login in cadastro_lista:
    print('Login realizado com sucesso')
else:
    print('Login ou senha inválidos. Tente novamente')

    print (cadastro_lista)