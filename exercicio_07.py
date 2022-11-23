#!/usr/bin/env python3

import os, time

start = time.process_time()

user_file = input('Insira o nome do arquivo: ') #Pedindo o nome do arquivo para o usuário.

if os.path.exists(user_file): #Se o arquivo existir...
    print('Arquivo encontrado. Prosseguindo...') #...avise que o arquivo existe e está sendo analisado...
    dictionary = {} #Criando um dicionário vazio
    dictionary['Protein'] = {} #Criando um dicionário vazio.
    with open(user_file, 'r') as file_read, open('Python_08.orf-longest.nt', 'w') as file_write: #Abrindo o arquivo inserido pelo usuário
        for sequence in file_read: #Para cada sequência no arquivo...
            if sequence[0] == '>': #... se ela começar com >
                split = sequence.split('>') #Tira esse > (para ficar bonitinho no dicionário)
                split_2 = split[1].split('-') #Nesse, eu deixo só o nome principal da sequência, tiro as informações da ORF e de ser proteína.
                split_3 = split[1].rsplit('-', 1)  #Nesse, eu tiro o 'protein' do nome da sequência (para ficar bonitinho no dicionário)
                if split_2[0] not in dictionary['Protein']: #Se o nome principal da sequência não tiver no dicionário...
                    dictionary['Protein'][split_2[0]] = {} #... acrescenta lá
                else: #Caso contrário...
                    continue #Seguindo em frente.
            else: #Se não começar com >
                dictionary['Protein'][split_2[0]][split_3[0]] = sequence.rstrip() #Vai acrescentar a sequência como valor para o nome ORF - tem que tirar a linha extra também, porque senão vai contar um aminoácido a mais..
        for key, value in dictionary['Protein'].items(): #Para chave e valor no dicionário...
            amino_max_len = max(value.values(), key=len) #Calculando a proteína de maior tamanho.
            key_amino_max_len = max(value, key=value.get) #Achando a chave dessa proteína de maior tamanho (o nome que revela as ORFS).
            file_write.write(f'>{key_amino_max_len}-protein [Protein length: {len(amino_max_len)} codons]\n') #Escreve isso no arquivo.
            file_write.write(amino_max_len + '\n') #E a maior sequência também.
        print('Arquivo \'Python_08.orf-longest.nt\' foi gerado.') #Aviso para o usuário do arquivo que acabou de ser gerado.
        end = time.process_time()
        time = end - start
        print('CPU Execution time:', time, 'seconds')
else: #Caso o arquivo inserido pelo usuário não seja encontrado...
    print('Arquivo não encontrado. Insira um nome válido (Provavelmente: Python_08.translated-longest.aa).') #Um aviso é entregue a ele pedindo um arquivo válido.
    exit() #O código para de rodar
