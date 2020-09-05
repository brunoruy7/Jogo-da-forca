def forca():
    from random import randint
    p = [['amarelo', 'amiga', 'amor', 'ave', 'aviao', 'avo', 'balao', 'bebe', 'bolo', 'branco', 'cama', 'caneca',
          'celular', 'clube',
          'copo', 'doce', 'elefante', 'escola', 'estojo', 'faca', 'foto', 'garfo', 'geleia', 'girafa', 'janela',
          'limonada', 'mae',
          'meia', 'noite', 'oculos', 'onibus', 'ovo', 'pai', 'pao', 'parque', 'passarinho', 'peixe', 'pijama', 'rato',
          'umbigo'],
         ['afobado', 'amendoim', 'banheiro', 'caatinga', 'cachorro', 'campeonato', 'capricornio',
          'catapora', 'corrupcao', 'crepusculo', 'empenhado', 'esparadrapo', 'forca', 'galaxia', 'historia', 'magenta',
          'manjericao', 'menta',
          'moeda', 'oracao', 'pacoca', 'palavra', 'pedreiro', 'pneumonia', 'pulmao', 'rotatoria', 'serenata',
          'transeunte', 'trilogia', 'xicara'],
         ['acender', 'afilhado', 'ardiloso', 'aspero', 'assombracao', 'asterisco', 'basquete', 'caminho', 'champanhe',
          'chiclete', 'chuveiro',
          'coelho', 'contexto', 'convivencia', 'coracao', 'desalmado', 'eloquente', 'esfirra', 'esquerdo', 'excecao',
          'fugaz', 'gororoba',
          'heterossexual', 'horrorizado', 'impacto', 'independencia', 'modernidade', 'oftalmologista',
          'otorrinolaringologista', 'paralelepipedo',
          'pororoca', 'prognosticio', 'quarentena', 'quimera', 'refeicao', 'reportagem', 'sino', 'taciturno', 'tenue',
          'visceral']]
    print('-='*20)
    print('JOGO DA FORCA')
    print('-=' * 20)
    while True:
        print('[1] Fácil \n[2] Médio\n[3] Difícil')
        modo = int(input('Escolha o modo de jogo: '))
        if modo == 1 or modo == 2 or modo == 3:
            break

    pal = p[modo - 1][randint(0, len(p[modo - 1]))]
    usadas = ''
    guess = '_' * len(pal)
    if modo == 1:
        vidas = 7
    elif modo == 2:
        vidas = 5
    elif modo == 3:
        vidas = 3
    while True:
        print('Vidas : {}'.format(vidas))
        print('Letras usadas: {}.'.format(usadas))
        print(guess)
        t = input()
        x = 0
        for i in range(len(pal)):
            if t == pal[i]:
                t1 = guess[0:i]
                t2 = guess[i + 1:len(guess)]
                guess = t1 + t + t2
            else:
                x += 1
        usadas += ' ' + t
        if x == len(pal):
            vidas -= 1

        if vidas == 0 or guess == pal:
            print('-=' * 20)
            print(f'A palavra era {pal}!')
            break
    if vidas == 0:
        print('\033[033mGame Over!\033[m Tente novamente.')
    else:
        print('\033[035mParabens você venceu!!\033[m Tente um nível mais dificil!')

while True:
    forca()
    n = ' '
    while n not in 'nNsS':
        n = input('\nJogar novamente[S]/[N]? ').upper()[0]
    if n == 'N':
        break