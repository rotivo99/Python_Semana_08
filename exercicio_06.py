#!/usr/bin/env python3

import os, re, time

start = time.process_time()

user_file = input('Insira o nome do arquivo: ') #Pedindo o nome do arquivo para o usuário.

if os.path.exists(user_file): #Se o arquivo existir...
    print('Arquivo encontrado. Prosseguindo...') #...avise que o arquivo existe e está sendo analisado...
    dictionary = {} #Criando um dicionário vazio.  
    with open(user_file, 'r') as file_read, open('Python_08.translated-longest.aa', 'w') as file_write: #Abrindo o arquivo inserido pelo usuário
        for sequence in file_read: #Para cada sequência no arquivo...
            if sequence[0] == '>': #... se ela começar com >
                split = sequence.split('>') #Tira esse > (para ficar bonitinho no dicionário)
                split_2 = split[1].rsplit('-', 1) #e tira o codon do final, o que sobrar...
                dictionary[split_2[0]] = {} #... vai ser a chave no dicionário
            else: #Se não começar com >
                try: #Tente
                    cds_regex = re.search(r'M.+\*', sequence) #Achando sequência que comece com M e termine com *
                    cds = sequence[cds_regex.start():cds_regex.end()] #Separando a sequência numa variável
                    dictionary[split_2[0]]['Protein CDS'] = cds #E acrescenta ela como valor no dicionário
                except: #Exceto
                    AttributeError #Se der esse erro
        for key, value in dictionary.items(): #Para cada chave e valor nos itens do dicionário...
            if bool(dictionary.get(key)) == True: #Se for verdadeiro que a chave tem um valor
                file_write.write('>' + key + '-protein\n') #Escrever o nome da sequência...
                file_write.write(value['Protein CDS'] + '\n') #e a sequência num novo arquivo.
        print('Arquivo \'Python_08.translated-longest.aa\' foi gerado.') #Aviso para o usuário do arquivo que acabou de ser gerado.
        end = time.process_time()
        time = end - start
        print('CPU Execution time:', time, 'seconds')
else: #Caso o arquivo inserido pelo usuário não seja encontrado...
    print('Arquivo não encontrado. Insira um nome válido (Provavelmente: Python_08.translated.aa).') #Um aviso é entregue a ele pedindo um arquivo válido.
    exit() #O código para de rodar.
