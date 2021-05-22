import bibSenhaCarolRodolpho
tentativas = 8
quantCores = 4
cores = ['Vermelho','Azul','Roxo','Amarelo','Laranja','Verde']
#inicio = input('Você deseja iniciar o jogo?').lower()

##if inicio == 'não' or inicio == 'nao':
##    print('Você podia pelo menos tentar |_|')

senha_certa = bibSenhaCarolRodolpho.GerarSenha(cores,quantCores)
print(senha_certa)

senha_jogador = []
for n in range (quantCores):
    palpiteJogador = input(f'Qual a {n+1}° cor?\n').capitalize()
    while bibSenhaCarolRodolpho.ValidarPalpite(cores,palpiteJogador) == False:
        print('Senha Inválida.')
        palpiteJogador = input(f'Qual a {n+1}° cor?\n').capitalize()
    senha_jogador.append(palpiteJogador)

acertosTotais = bibSenhaCarolRodolpho.TestarAcertosTotais(senha_certa,senha_jogador)
print (f'Acertos Totais = {acertosTotais}')

testeVitoria = bibSenhaCarolRodolpho.TestarVitoria(senha_certa, senha_jogador)
if testeVitoria == True:
    print('Parabéns, você venceu!')
else:
    print('Infelizmente, você não conseguiu dessa vez... Tente numa próxima!')
    
