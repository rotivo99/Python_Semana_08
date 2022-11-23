#!/usr/bin/env python3

#Tive que rodar esses comandos para conseguir instalar o biopython
#sudo apt-get update
#sudo apt install python3-pip
#pip install biopython

import os, time
from Bio.Seq import Seq

start = time.process_time()

user_file = input('Insira o nome do arquivo: ') #Pedindo o nome do arquivo para o usuário.

if os.path.exists(user_file): #Se o arquivo existir...
    print('Arquivo encontrado. Prosseguindo...') #...avise que o arquivo existe e está sendo analisado...
    dictionary = {} #Criando um dicionário vazio.
    with open(user_file, 'r') as file_read, open('Python_08.translated.aa', 'w') as file_write: #Abrindo o arquivo inserido pelo usuário
        for sequence in file_read: #Para cada sequência no arquivo...
            if sequence[0] == '>': #... se ela começar com >
                split = sequence.split('>') #Tira esse > (para ficar bonitinho no dicionário)
                split_2 = split[1].rsplit('-', 1) #e tira o codon do final, o que sobrar...
                dictionary[split_2[0]] = {} #... vai ser a chave no dicionário
            else: #Se não começar com >
                new_sequence = sequence.replace(' ', '').rstrip() #Vamos tirar o espaço entre os códons...
                if len(new_sequence) % 3 == 0: #Conferindo se o número de nucleotídeos na sequência é múltiplo de três, porque testei com um arquivo que não tinha passado pelos exercícios anteriores e deu erro bem nisso.
                    coding_DNA = Seq(new_sequence) #Tem que colocar esse Seq para o biopython funcionar (aparecia assim na documentação)
                    protein = coding_DNA.translate() #Traduzindo os códons em aminoácidos
                    amino_list = [] #A lista vazia fica aqui para zerar a sequência que tá entrando toda vez de maneira que uma proteína não se some à outra...
                    for aminoacid in protein: #Para cada aminoácido na proteína
                        amino_list += aminoacid #Acrescentar ele a essa lista
                        joined = ''.join(amino_list) #Junta eles (para não ficar uma lista de aminoácidos, mas uma sequência direta
                        dictionary[split_2[0]]['Protein'] = joined #E acrescenta como valor no dicionário (eu tive que fazer isso, porque não tava dando certo acrescentar no dicionário direto no else)
                else:
                    print('Não foi possível realizar a separação dos códons. Verifique se o número de nucleotídeos na(s) sequência(s) inserida(s) é múltiplo de três e tente novamente.')
                    exit()
        for key, value in dictionary.items(): #Para cada chave e valor nos itens do dicionário...
            try: #Tente
                file_write.write('>' + key + '-protein\n') #Escrever o nome da sequência...
                file_write.write(value['Protein'] + '\n') #e a sequência num novo arquivo.
            except: #Exceto
                KeyError #Se der Keyerror
        print('Arquivo \'Python_08.translated.aa\' foi gerado.') #Aviso para o usuário do arquivo que acabou de ser gerado.
        end = time.process_time()
        time = end - start
        print('CPU Execution time:', time, 'seconds')
else: #Caso o arquivo inserido pelo usuário não seja encontrado...
    print('Arquivo não encontrado. Insira um nome válido (Provavelmente: Python_08.codons-6frames.nt).') #Um aviso é entregue a ele pedindo um arquivo válido.
    exit() #O código para de rodar.
