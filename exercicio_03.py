#!/usr/bin/env python3

import re, os, time

start = time.process_time()

user_file = input('Insira o nome do arquivo: ') #Pedindo o nome do arquivo para o usuário.

if os.path.exists(user_file): #Se o arquivo existir...
    print('Arquivo encontrado. Prosseguindo...') #...avise que o arquivo existe e está sendo analisado...
    dictionary = {} #Criando um dicionário vazio.
    with open(user_file, 'r') as file_read, open('Python_08.codons-3frames.nt', 'w') as file_write: #Abrindo o arquivo inserido pelo usuário.
        joining_all = ''.join(file_read.read().splitlines()) #Como as sequências vêm quebradas em várias linhas, pensei em juntar tudo numa só. Então primeiro eu retiro o \n com o splitlines() e depois junto as linhas com o ''.join.
        splitting_greater_than = joining_all.split('>') #Quebro a linha única pelo '>', que indica que uma nova sequência está iniciando. Assim, cada sequência fica isolada e eu consigo mexer com cada uma separadamente.
        #PRIMEIRO OPEN READING FRAME:
        for line in splitting_greater_than: #Para cada linha contínua...
            for match in re.findall(r'\w+\d+_\w+\d+_\w+\d+', line): #...quero o identificador da sequência. Eu reparei que o número que acompanhava o c variava, então eu coloquei o + ao lado do d, mas eu também coloquei junto de todo o resto, porque eu não sabia se eles SEMPRE eram fixos.
                dictionary[match] = {} #Acrescentando o identificador como chave do dicionário.
            for codon in re.finditer(r'(([ATGC][ATGC][ATCG])+)', line, re.I): #Quero achar códons quantas vezes aparecerem... (Aqui tá tudo juntoe e tá separando eles de três em três)
                sequence = line[codon.start():codon.end()] #Separando os códons e atribuindo eles a uma variável.
                codon_list = [] #Criando uma lista vazia de códons.
                for nt in range(0, len(sequence), 3): #Para nucleotídeos nesse intervalo...
                    codon_list += [sequence[nt:nt+3]] #...adicionar eles na nossa lista de códons...
                    joining = ' '.join(codon_list) #Juntando os códons por espaços.
                for codon_search in re.finditer(r'([ATGC][ATGC][ATCG] )+([ATGC][ATGC][ATCG])', joining, re.I): #Procurando códons completos.
                    new_sequence = joining[codon_search.start():codon_search.end()] #Salvando a sequência aqui.
                    dictionary[match]['ORF1'] = new_sequence #...e no dicionário depois.
        #SEGUNDO OPEN READING FRAME:
        for line in splitting_greater_than:
            for match in re.findall(r'\w+\d+_\w+\d+_\w+\d+', line):
                for codon in re.finditer(r'(([ATGC][ATGC][ATCG])+)', line, re.I):
                    sequence = line[codon.start():codon.end()]
                    corrected_sequence = re.sub(r'\w', '', sequence, 1)
                    codon_list = []
                    for nt in range(0, len(corrected_sequence), 3):
                        codon_list += [corrected_sequence[nt:nt+3]]
                        joining = ' '.join(codon_list)
                    for codon_search in re.finditer(r'([ATGC][ATGC][ATCG] )+([ATGC][ATGC][ATCG])', joining, re.I):
                        new_sequence = joining[codon_search.start():codon_search.end()]
                        dictionary[match]['ORF2'] = new_sequence
        #TERCEIRO OPEN READING FRAME:
        for line in splitting_greater_than:
            for match in re.findall(r'\w+\d+_\w+\d+_\w+\d+', line):
                for codon in re.finditer(r'(([ATGC][ATGC][ATCG])+)', line, re.I):
                    sequence = line[codon.start():codon.end()]
                    corrected_sequence = re.sub(r'\w', '', sequence, 2)
                    codon_list = []
                    for nt in range(0, len(corrected_sequence), 3):
                        codon_list += [corrected_sequence[nt:nt+3]]
                        joining = ' '.join(codon_list)
                    for codon_search in re.finditer(r'([ATGC][ATGC][ATCG] )+([ATGC][ATGC][ATCG])', joining, re.I):
                        new_sequence = joining[codon_search.start():codon_search.end()]
                        dictionary[match]['ORF3'] = new_sequence
        for key, value in dictionary.items():
            try:
                file_write.write('>' + key + '-frame-1-codon\n')
                file_write.write(value['ORF1'] + '\n')
                file_write.write('>' + key + '-frame-2-codon\n')
                file_write.write(value['ORF2'] + '\n')
                file_write.write('>' + key + '-frame-3-codon\n')
                file_write.write(value['ORF3'] + '\n')
            except:
                KeyError
        print('Arquivo \'Python_08.codons-3frames.nt\' foi gerado.') #Aviso para o usuário do arquivo que acabou de ser gerado.
        end = time.process_time()
        time = end - start
        print('CPU Execution time:', time, 'seconds')
else: #Caso o arquivo inserido pelo usuário não seja encontrado...
    print('Arquivo não encontrado. Insira um nome válido (Provavelmente: Python_08.fasta).') #Um aviso é entregue a ele pedindo um arquivo válido.
    exit() #O código para de rodar.
