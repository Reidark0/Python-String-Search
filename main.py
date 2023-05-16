def sair():     # Função para sair do código após a consulta.
    decisaoSair = int(input('Você deseja fazer outra selação usando requisitos diferentes nos mesmo candidatos?\n'
                            '1 - Sim\n'
                            '0 - Não\n'))
    if decisaoSair == 0:
        print('Tudo bem, volte se precisar fazer outra consulta ou atualize a lista de candidatos.')
        exit()
    elif decisaoSair == 1:
        print('Digite as notas:\n')

def cortarCandidato(candidato, inicio, fim=None):   # Essa função faz slicing na 'eX_tX_pX_sX' usando dos paramêtros (inicio) e (fim), começa diminuindo
    candidato = candidato[candidato.find(inicio):]  # pelo (inicio) para o (fim) '_' funcionar corretamente e depois adiciona +1 no slicing para não incluir
    if fim is not None:                             # o (incio) e isolar a nota e assim números de mais digitos são reconhecidos.
        corte = candidato[candidato.find(inicio) + 1:candidato.find(fim)]
        return corte
    else: 
        corte = candidato[candidato.find(inicio) + 1:]  # (inicio) com 's' não há caracter no final, o número já está isolado
        return corte
    
def selecionados_e(candidatos, entrevistaCorte):    # Elimina candidatos com nota inferior em entrevista
    aprovados_e = []
    for candidato in candidatos: 
        if int(cortarCandidato(candidato, 'e', '_')) >= entrevistaCorte:   
            aprovados_e.append(candidato)
    return aprovados_e

def selecionados_t(candidatos, teoricoCorte):       # Elimina candidatos com nota inferior em teórico
    aprovados_t = []
    for candidato in candidatos: 
        if int(cortarCandidato(candidato, 't', '_')) >= teoricoCorte:    
            aprovados_t.append(candidato)
    return aprovados_t
        
def selecionados_p(candidatos, praticoCorte):       # Elimina candidatos com nota inferior em prático
    aprovados_p = []
    for candidato in candidatos:
        if int(cortarCandidato(candidato, 'p', '_')) >= praticoCorte:      
            aprovados_p.append(candidato)
    return aprovados_p

def selecionados_s(candidatos, softCorte):          # Elimina candidatos com nota inferior em soft
    aprovados_s = []
    for candidato in candidatos:
        if int(cortarCandidato(candidato, 's')) >= softCorte:
            aprovados_s.append(candidato)
    return aprovados_s

def selecao(entrevistaCorte, teoricoCorte, praticoCorte, softCorte, candidatos):# função principal = união de todas as seleções
    candidatos = selecionados_e(candidatos, entrevistaCorte)
    candidatos = selecionados_t(candidatos, teoricoCorte)
    candidatos = selecionados_p(candidatos, praticoCorte)
    candidatos = selecionados_s(candidatos, softCorte)
    return candidatos


Candidatos = [      # Lista de candidatos pré-selecionados
            'e7_t9_p10_s8',   
            'e4_t4_p8_s8',
            'e8_t10_p7_s7',
            'e4_t1_p3_s2',
            'e4_t10_p3_s10',
            'e9_t3_p5_s1',
            'e7_t9_p5_s6',
            'e1_t2_p8_s3',
            'e8_t10_p8_s6',
            'e9_t8_p3_s3',
            'e7_t8_p8_s6',
            'e1_t4_p3_s1',
            'e3_t2_p6_s5',
            'e3_t8_p3_s9',
            'e4_t10_p8_s3',
            'e9_t10_p8_s9',
            'e1_t6_p3_s6',
            'e5_t2_p4_s9',
            'e1_t5_p5_s2',
            'e5_t8_p1_s5']

print(f'Temos {len(Candidatos)} candidatos que passaram por 4 etapas de seleção e receberam 4 notas\n'
      'A primeira etapa foi uma Entrevista\n'
      'A segunda etapa foi um teste teórico\n'
      'A terceira etapa foi um teste prático\n'
      'E por fim a quarta etapa foi uma avaliação das soft skills do candidato.\n'
      'As notas são de 0 a 10 e aqui você vai poder filtrar os resultados.\n')

ficar = 0
while ficar == 0:   # Loop para pesquisar de novo sem encerrar o programa.

    entrevistaCorte = int(input('Qual a nota mínima de ENTREVISTA você procura?\nNota: '))
    teoricoCorte = int(input('Qual a nota mínima no TESTE TEÓRICO você procura?\nNota: '))
    praticoCorte = int(input('Qual a nota mínima no TESTE PRÁTICO você procura?\nNota: '))
    softCorte = int(input('Qual a nota mínima de SOFT SKILLS você procura?\nNota: '))

    selecionados = selecao(entrevistaCorte, teoricoCorte, praticoCorte, softCorte, Candidatos)

    if len(selecionados) == 1:
        print(f'\nSomente o candidato com as notas || {selecionados[0]} || cumpre os requerimentos desejados.\n')
    elif len(selecionados) == 0:
        print('\nNenhum candidato atende os requerimentos desejados.\n')
    else:
        print('\nAs notas dos candidatos que passam nos requerimentos são: \n'
            f'{" || ".join(selecionados)}\n')
    
    sair()
