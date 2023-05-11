def selecao(entrevistaCorte, teoricoCorte, praticoCorte, softCorte, lista):
    selecionados_e = []
    selecionados_t = []
    selecionados_p = []
    selecionados_final = []
    # e_nota, t_nota, p_nota e s_nota servem para reduzir o tamanho do código.
    for candidato in range(len(lista)): 
        # pega o item da lista, faz um slicing da string, isola a nota e converte em int
        e_nota = lista[candidato]
        if int(e_nota[e_nota.find('e') + 1:e_nota.find('_')]) >= entrevistaCorte:   # Corte da entrevista
            selecionados_e.append(e_nota) 
    for candidato in range(len(selecionados_e)): 
        t_nota = selecionados_e[candidato][selecionados_e[candidato].find('_') +1:]
        if int(t_nota[t_nota.find('t') + 1 : t_nota.find('_')]) >= teoricoCorte:    # Corte do teórico
            selecionados_t.append(selecionados_e[candidato])
    for candidato in range(len(selecionados_t)):
        p_nota = selecionados_t[candidato][selecionados_t[candidato].find('p'):]
        if int(p_nota[p_nota.find('p') + 1:p_nota.find('_')]) >= praticoCorte:      # Corte do prático
            selecionados_p.append(selecionados_t[candidato])
    for candidato in range(len(selecionados_p)):
        s_nota = selecionados_p[candidato][selecionados_p[candidato].find('s') + 1:]
        if int(s_nota) >= softCorte:                                                # Corte do Soft
            selecionados_final.append(selecionados_p[candidato])
    return selecionados_final

# lista de candidatos no formato string "eX_tX_pX_sX" 
# e = entrevista // t = teórico // p = prático // s = soft skill
CandidatosNota = ['e7_t9_p10_s8',
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

print(f'Temos {len(CandidatosNota)} candidatos que passaram por 4 etapas de seleção e receberam 4 notas\n'
      'A primeira etapa foi uma Entrevista\n'
      'A segunda etapa foi um teste teórico\n'
      'A terceira etapa foi um teste prático\n'
      'E por fim a quarta etapa foi uma avaliação das soft skills do candidato.\n'
      'As notas são de 0 a 10 e aqui você vai poder filtrar os resultados.\n')
entrevistaCorte = int(input('Qual a nota mínima de ENTREVISTA você procura?\nNota: '))
teoricoCorte = int(input('Qual a nota mínima no TESTE TEÓRICO você procura?\nNota: '))
praticoCorte = int(input('Qual a nota mínima no TESTE PRÁTICO você procura?\nNota: '))
softCorte = int(input('Qual a nota mínima de SOFT SKILLS você procura?\nNota: '))
selecionados = selecao(entrevistaCorte, teoricoCorte, praticoCorte, softCorte, CandidatosNota)
if len(selecionados) == 1:
    print(f'Somente o candidato com as notas {selecionados[0]} cumpre os requerimentos desejados.')
elif len(selecionados) == 0:
    print('Nenhum candidato atende os requerimentos desejados.')
else:
    print('As notas dos candidatos que passam nos requerimentos são: \n'
          f'{" || ".join(selecionados)}')
