class Restaurante:
    nome= ''
    categoria=''
    ativo=False


# 2 criação de objetos
restaurante_praca=Restaurante()
restaurante_praca.nome='praça'
# restaurante_praca.categoria='Gourmet'


restaurante_pizza=Restaurante()

restaurantes=[restaurante_praca,restaurante_pizza]

print(dir(restaurante_praca))
print('')
print(vars(restaurante_praca))




#tarefa 1 =======================================================================================================
restaurante_praca=Restaurante()
restaurante_praca.categoria='Italiana'
print(vars(restaurante_praca))

#tarefa 1 =======================================================================================================




#tarefa 2 =======================================================================================================
nome_restaurante=restaurante_praca.nome
print(nome_restaurante)

#tarefa 2 =======================================================================================================



#tarefa 3 =======================================================================================================
if restaurante_praca.ativo:
    print('o retaurante está ativo')
else:
    print('o restaurante está inativo')
    print('')
#tarefa 3=======================================================================================================



#tarefa 4 =======================================================================================================
categoria=Restaurante.categoria
print(categoria)
#tarefa 4=======================================================================================================



#tarefa 5 =======================================================================================================
restaurante_praca=Restaurante()
restaurante_praca.nome='Bistrô'

#tarefa 5 =======================================================================================================


#tarefa 6=======================================================================================================
restaurante_pizza=Restaurante()
restaurante_pizza.nome='Pizza Place'
restaurante_praca.categoria='Fast Food'
#tarefa 6 =======================================================================================================


#tarefa 7=======================================================================================================
verifica_categoria=restaurante_pizza.categoria
print(verifica_categoria)
#tarefa 7 =======================================================================================================



#tarefa 8=======================================================================================================
restaurante_pizza.ativo=True
print(restaurante_pizza.ativo)

#tarefa 8=======================================================================================================



#tarefa 9=======================================================================================================
restaurante_praca=Restaurante()
restaurante_praca.nome='praça'
restaurante_praca.categoria='Italiana'
print(vars(restaurante_praca))
#tarefa 9 =======================================================================================================
