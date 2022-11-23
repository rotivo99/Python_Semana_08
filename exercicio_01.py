#!/usr/bin/env python3

import re, os, time

start = time.process_time()

user_file = input('Insira o nome do arquivo: ') #Pedindo o nome do arquivo para o usuário.

if os.path.exists(user_file): #Se o arquivo existir...
    print('Arquivo encontrado. Prosseguindo...') #...avise que o arquivo existe e está sendo analisado.
    dictionary = {} #Criando um dicionário vazio.
    with open(user_file, 'r') as file_read: #Abrindo o arquivo inserido pelo usuário.
        joining_all = ''.join(file_read.read().splitlines()) #Como as sequências vêm quebradas em várias linhas, pensei em juntar tudo numa só. Então primeiro eu retiro o \n com o splitlines() e depois junto as linhas com o ''.join.
        splitting_greater_than = joining_all.split('>') #Quebro a linha única pelo '>', que indica que uma nova sequência está iniciando. Assim, cada sequência fica isolada e eu consigo mexer com cada uma separadamente.
        for line in splitting_greater_than: #Para cada linha em cada isolado...
            for match_1 in re.findall(r'\w+\d+_\w+\d+_\w+\d+', line): #...quero o identificador da sequência. Eu reparei que o número que acompanhava o c variava, então eu coloquei o + ao lado do d, mas eu também coloquei junto de todo o resto, porque eu não sabia se eles SEMPRE eram fixos.
                dictionary[match_1] = {} #Acrescentando o identificador como chave do dicionário.
            for match_2 in re.findall(r'\w+\d+_\w+\d+_\w+\d+.+\]([ATCG]+)', line): #Encontrando a sequência. Ela pode ter A, T, C e G inúmeras vezes e não preciso me preocupar com pegar parte da próxima sequência sem querer.
                A_count = match_2.upper().count('A') #Contando a quantidade de adeninas.
                dictionary[match_1]['A_count'] = A_count #Acrescentando ao dicionário.
                T_count = match_2.upper().count('T') #Contando a quantidade de timinas.
                dictionary[match_1]['T_count'] = T_count #Acrescentando ao dicionário.
                C_count = match_2.upper().count('C') #Contando a quantidade de citosinas.
                dictionary[match_1]['C_count'] = C_count #Acrescentando ao dicionário.
                G_count = match_2.upper().count('G') #Contando a quantidade de guaninas.
                dictionary[match_1]['G_count'] = G_count #Acrescentando ao dicionário.
else: #Caso o arquivo inserido pelo usuário não seja encontrado...
    print('Arquivo não encontrado. Insira um nome válido (Provavelmente: Python_08.fasta).') #Um aviso é entregue a ele pedindo um arquivo válido.
    exit() #O código para de rodar

#for key, value in dictionary.items(): #Outra forma de apresentar a sequência, com o dicionário.
#    print(key + ':', value)

print(f'Sequence\tA count\tT count\tC count\tG count') #Header da tabela apresentada ao usuário contabilizando o valor de cada nucleotídeo.
for key, value in dictionary.items(): #Para cada chave e valor em dicionário.
    print(key, '\t', value['A_count'], '\t', value['T_count'], '\t', value['C_count'], '\t', value['G_count'], sep = '') #Tabela.

end = time.process_time()
time = end - start
print('CPU Execution time:', time, 'seconds') #Como a saída de alguns arquivos estava demorando para aparecer na tela, eu me perguntei quanto tempo demorava para o computador processar esses dados, daí eu resolvi fazer isso.
