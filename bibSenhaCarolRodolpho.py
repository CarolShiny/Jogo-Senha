import random
def GerarSenha(cores,quantCores):
    senha_certa = []
    for n in range (quantCores):
        corAleatoria = random.choice(cores)
        while corAleatoria in senha_certa:
            corAleatoria = random.choice(cores)
        senha_certa.append(corAleatoria)
    return senha_certa

def ValidarPalpite (cores,palpiteJogador):
    if palpiteJogador not in cores:
        return False
    else:
        return True

def TestarVitoria(senha,palpite):
    if senha == palpite:
        return True
    else:
        return False

def TestarAcertosTotais (senha,palpite):
    AcertosTotais = 0
    for n in range (len(senha)):
        if senha[n] == palpite[n]:
            AcertosTotais += 1
    return AcertosTotais
    
