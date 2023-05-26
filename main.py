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
    
def filtrar_por_entrevista(candidatos, entrevistaNota):    # Elimina candidatos com nota inferior em entrevista
    aprovados_entrevista = []
    for candidato in candidatos: 
        if int(cortarCandidato(candidato, 'e', '_')) >= entrevistaNota:   
            aprovados_entrevista.append(candidato)
    return aprovados_entrevista

def filtrar_por_teste_teorico(candidatos, teoricoNota):       # Elimina candidatos com nota inferior em teórico
    aprovados_teste_teorico = []
    for candidato in candidatos: 
        if int(cortarCandidato(candidato, 't', '_')) >= teoricoNota:    
            aprovados_teste_teorico.append(candidato)
    return aprovados_teste_teorico
        
def filtrar_por_teste_pratico(candidatos, praticoNota):       # Elimina candidatos com nota inferior em prático
    aprovados_teste_pratico = []
    for candidato in candidatos:
        if int(cortarCandidato(candidato, 'p', '_')) >= praticoNota:      
            aprovados_teste_pratico.append(candidato)
    return aprovados_teste_pratico

def filtrar_por_softskill(candidatos, softskillNota):          # Elimina candidatos com nota inferior em soft
    aprovados_soft_skills = []
    for candidato in candidatos:
        if int(cortarCandidato(candidato, 's')) >= softskillNota:
            aprovados_soft_skills.append(candidato)
    return aprovados_soft_skills

def selecao(entrevistaNota, teoricoNota, praticoNota, softskillNota, candidatos):# função principal = união de todas as seleções
    candidatos = filtrar_por_entrevista(candidatos, entrevistaNota)
    candidatos = filtrar_por_teste_teorico(candidatos, teoricoNota)
    candidatos = filtrar_por_teste_pratico(candidatos, praticoNota)
    candidatos = filtrar_por_softskill(candidatos, softskillNota)
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

    entrevistaNota = int(input('Qual a nota mínima de ENTREVISTA você procura?\nNota: '))
    teoricoNota = int(input('Qual a nota mínima no TESTE TEÓRICO você procura?\nNota: '))
    praticoNota = int(input('Qual a nota mínima no TESTE PRÁTICO você procura?\nNota: '))
    softskillNota = int(input('Qual a nota mínima de SOFT SKILLS você procura?\nNota: '))

    selecionados = selecao(entrevistaNota, teoricoNota, praticoNota, softskillNota, Candidatos)

    if len(selecionados) == 1:
        print(f'\nSomente o candidato com as notas || {selecionados[0]} || cumpre os requerimentos desejados.\n')
    elif len(selecionados) == 0:
        print('\nNenhum candidato atende os requerimentos desejados.\n')
    else:
        print('\nAs notas dos candidatos que passam nos requerimentos são: \n'
            f'{" || ".join(selecionados)}\n')
    
    sair()
