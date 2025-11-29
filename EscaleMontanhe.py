import os
import time #biblioteca time para controlar o tempo entre os caminhos da história

# Limpa a tela para uma melhor visualização ao decorrer da história
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

# CLASSE DOS NÓS DA HISTÓRIA
class No:
    def __init__(self, id, texto=None, opcoes=None, final=None):
        self.id = id #nome interno do nó que está sendo criado
        self.texto = texto or '' #texto que aparece para contextualização do caminho 
        self.opcoes = opcoes or {} #Opções para o usuário escolher qual caminho seguir
        self.final = final #represnta o texto quando o usuário chega ao final

    def eh_final(self):
        return self.final is not None #verificação se é o nó final ou não

# Nós que representam os finais do jogo, os nós finais precisam apenas dos parâmetros de ID e do final 
final_topo = No('Arriscar tudo', final=""" 
VOCÊ CHEGOU AO TOPO DA MONTANHA!

O vento sopra forte. O sol nasce.
Você ergue os braços em vitória!

PARABÉNS, AVENTUREIRO!
""")

final_sem_saida = No('Parede_de_Pedra', final="""
CAMINHO SEM SAÍDA

Você chega a uma parede de pedra lisa.
Sem equipamentos... só resta voltar.

Derrota silenciosa...
""")

final_queda = No('Pular', final="""
VOCÊ CAIU!!!

Seus pés escorregam na pedra molhada.
Você tenta se agarrar... mas é tarde.

*Game Over*
""")

final_fog = No('Tentar_atravessar', final="""
PERDIDO NA NEBLINA

A névoa engole seus passos.
Você vaga sem rumo até cair exausto.

Fim trágico...
""")

final_sabedoria = No('Falar_com_ancião', final="""
SABEDORIA DO ANCIÃO

Um velho guia lhe ensina um caminho secreto.
Com conhecimento, você atravessa a montanha.

Vitória pacífica.
""")

final_caverna = No('Entrar_na_caverna', final="""
CAVERNA ESCURA

Dentro da caverna você encontra um lago subterrâneo.
As paredes desabam silenciosamente.

Você não consegue sair.
""")

final_sucesso_parcial = No('Subir_plataforma', final="""
MEIO TOPO

Você alcança uma plataforma elevada.
Não é o topo, mas é um lugar seguro para acampar.

Missão parcialmente cumprida.
""")

final_pedra_precaria = No('Passar_pelas_pedras', final="""
PONTA INSTÁVEL

Uma pedra onde você pisa se solta.
Você consegue escapar por pouco, machucado.

Volte mais preparado.
""")

final_resgate = No('Fazer_sinais_de_socorro', final="""
RESGATE INESPERADO

Um helicóptero avista sua signal.
Você é resgatado para segurança.

Sobrevivência com honra.
""")

final_tesouro = No('Pegar_tesouro', final="""
TESOURO ESCONDIDO

Você encontra um pequeno tesouro deixado por antigos escaladores.
Não leva ao topo, mas muda seu destino.
""")


# dicionário que representa o armazenamento de todos os nós criados para que seja possível uma validação e contagem dos nós alcançáveis pelo caminho 
nodes = {}

# função auxiliar pra criar nós e registrar
def N(id, texto=''):
    caminho = No(id, texto=texto) #cria o nó da história com o id e texto que representa o caminho
    nodes[id] = caminho #registra no dicionário
    return caminho

#A partir daqui são gerados os caminhos da história, representa o mapa do jogo
inicio = N('Início', """
A ESCALADA DA MONTANHA PERIGOSA
Você está na base do Monte da Morte.
Neva forte. O vento uiva.

Antes de partir, verifique sua mochila — você pode levar APENAS UM item:
1) MAPA detalhado da montanha
2) BÚSSOLA confiável

Escolha com sabedoria.
""")

floresta = N('Floresta', """
Você entra numa floresta densa e escura.
Ouve um riacho ao longe... e vê uma colina íngreme.
""")

rio = N('Rio', """
Um rio gelado bloqueia seu caminho!
Você vê pedras escorregadias no meio da corrente e uma ponte velha a alguma distância.
""")

bifurcacao = N('Bifurcacao', """
Você encontra uma bifurcação na trilha.
Caminho à esquerda: íngreme, mas curto
Caminho à direita: suave, mas muito longo
""")

penhasco = N('Penhasco', """
Você chega a um penhasco estreito e perigoso.
Abaixo, um abismo de 200 metros...
""")

acampamento = N('Acampamento', """
Você encontra um acampamento abandonado.
Há uma fogueira apagada e um mapa rasgado.
""")

ponte_arriscada = N('Ponte_arriscada', """
A ponte range quando você pisa nela.
Do outro lado, há uma trilha com marcas antigas.
""")

neblina = N('Neblina', """
Uma neblina espessa desce rápido.
Visibilidade quase zero.
""")

caverna_entrada = N('Entrada_da_Caverna', """
Você encontra a entrada de uma caverna com inscrições.
Parece perigoso, mas pode ser um atalho.
""")

colina = N('Colina', """
A colina é íngreme, coberta por pedras soltas.
No topo, você avista uma enorme cruz de pedra.
""")

ponte_velha = N('Ponte_velha', """
A ponte velha está parcialmente quebrada.
Você pode pular uma parte ou consertar provisoriamente.
""")

trilha_longe = N('Trilha_longe', """
A trilha se estende por muitos quilômetros em ziguezague.
Você encontra uma placa indicando: "Santuário — 12 km".
""")

acampamento_antigo = N('Acampamento_antigo', """
Você encontra um barracão em ruínas com símbolos antigos.
""")

moinho = N('Moinho', """
Um velho moinho de vento aparece no topo de uma colina baixa.
Há uma velha corda pendurada.
""")

bosque_claro = N('Bosque_claro', """
O bosque se abre em uma clareira com flores estranhas.
O cheiro é reconfortante.
""")

ruinas = N('Ruinas', """
Você encontra ruínas de um antigo abrigo de escaladores.
Há ferramentas enferrujadas.
""")

rastro_animais = N('Rastro_de_animais', """
Há rastros de animais na lama.
Eles seguem para uma formação rochosa.
""")

ladeira = N('Ladeira', """
Uma ladeira íngreme bloqueia seu caminho.
As pedras cedem sob seus pés.
""")

barranco = N('Barranco', """
Você alcança um barranco com vista para um vale.
Há um heliponto abandonado.
""")

ponte_suspensa = N('Ponte_suspensa', """
Uma ponte suspensa liga duas falésias.
O vento a balança.
""")

mirante = N('Mirante', """
Um mirante natural oferece vista para várias trilhas.
Você pode estudar o mapa mentalmente.
""")

passo_raso = N('Passo_raso', """
Um passo raso exige equilíbrio.
""")

refugio = N('Refugio', """
Um pequeno refúgio de pedra oferece abrigo.
Há mantimentos secos.
""")

encosta_rochosa = N('Encosta_rochosa', """
A encosta é rochosa e exige técnica.
""")

ponte_de_pedra = N('Ponte_de_pedra', """
Uma ponte natural de pedra forma uma passagem estreita.
""")

atalho_secreto = N('Atalho_secreto', """
Você descobre um atalho marcado por fitas coloridas.
Parece não ser usado há anos.
""")
pedra_escrita = N('Pedra_escrita', 
                  'Você encontra uma pedra com inscrições.')
riacho = N('Riacho', 
           'Um pequeno riacho corta a trilha. Água limpa, parece potável.')
vento_forte = N('Vento_forte', 
                'Ventos fortes sopram pedras soltas.')
arvore_caida = N('Arvore_caida', 
                 'Uma árvore caída forma uma ponte sobre um córrego.')
pegada = N('Pegada', 
           'Pegadas frescas seguem por uma trilha estreita.')
trilha_antiga = N('Trilha_antiga', 
                  'Uma trilha antiga com corrimões de madeira.')
tempestade = N('tempestade', 
               'O céu escurece rapidamente. Tempestade se aproxima.')
som_metalico = N('Som_metalico', 
                 'Um som metálico ecoa por entre as rochas.')
corrente_ar = N('Corrente_de_ar', 
                'Uma corrente de ar frio sopra por uma fenda.')

#Conexões - opções de caminhos a partir do nó, tudo isso é adicionado ao dicionario com os nó 
# inicio como ponto inicial
inicio.opcoes = {
    '1': floresta,
    '2': rio,
    '3': colina
}

floresta.opcoes = {
    '1': rio,
    '2': colina,
    '3': acampamento,
    '4': arvore_caida
}

rio.opcoes = {
    '1': ponte_velha,
    '2': bifurcacao,
    '3': arvore_caida
}

bifurcacao.opcoes = {
    '1': penhasco,
    '2': trilha_longe,
    '3': pegada
}

penhasco.opcoes = {
    '1': final_topo,
    '2': final_sem_saida,
    '3': ponte_de_pedra
}

acampamento.opcoes = {
    '1': acampamento_antigo,
    '2': refugio,
    '3': final_sabedoria
}

ponte_arriscada.opcoes = {
    '1': ponte_suspensa,
    '2': ponte_de_pedra,
    '3': bifurcacao
}

neblina.opcoes = {
    '1': acampamento,
    '2': riacho,
    '3': final_fog
}

caverna_entrada.opcoes = {
    '1': final_caverna,
    '2': ruinas,
    '3': corrente_ar
}

colina.opcoes = {
    '1': acampamento,
    '2': mirante,
    '3': moinho
}

ponte_velha.opcoes = {
    '1': ponte_arriscada,
    '2': ponte_suspensa,
    '3': final_queda
}

trilha_longe.opcoes = {
    '1': caverna_entrada,
    '2': atalho_secreto,
    '3': penhasco
}

acampamento_antigo.opcoes = {
    '1': final_tesouro,
    '2': trilha_longe,
    '3': moinho
}

moinho.opcoes = {
    '1': ponte_velha,
    '2': acampamento_antigo,
    '3': trilha_antiga
}

bosque_claro.opcoes = {
    '1': final_sucesso_parcial,
    '2': moinho,
    '3': som_metalico
}

ruinas.opcoes = {
    '1': ponte_velha,
    '2': acampamento_antigo,
    '3': pedra_escrita
}

rastro_animais.opcoes = {
    '1': ruinas,
    '2': bosque_claro,
    '3': ladeira
}

ladeira.opcoes = {
    '1': rastro_animais,
    '2': final_pedra_precaria
}

barranco.opcoes = {
    '1': final_resgate,
    '2': ladeira
}

ponte_suspensa.opcoes = {
    '1': barranco,
    '2': ponte_arriscada,
    '3': vento_forte
}

mirante.opcoes = {
    '1': trilha_longe,
    '2': neblina,
    '3': pegada
}

passo_raso.opcoes = {
    '1': ponte_suspensa,
    '2': final_queda
}

refugio.opcoes = {
    '1': mirante,
    '2': acampamento
}

encosta_rochosa.opcoes = {
    '1': passo_raso,
    '2': rastro_animais
}

ponte_de_pedra.opcoes = {
    '1': refugio,
    '2': encosta_rochosa
}

atalho_secreto.opcoes = {
    '1': final_tesouro,
    '2': trilha_longe
}

pedra_escrita.opcoes = {
    '1': acampamento_antigo, 
    '2': ponte_de_pedra
}
riacho.opcoes = {
    '1': refugio, 
    '2': rastro_animais
}
vento_forte.opcoes = {
    '1': passo_raso, 
    '2': ponte_suspensa
}
arvore_caida.opcoes = {
    '1': riacho, 
    '2': neblina
}
pegada.opcoes = {
    '1': pedra_escrita, 
    '2': mirante
}
trilha_antiga.opcoes = {'1': ponte_suspensa, '2': encosta_rochosa}
tempestade.opcoes = {'1': refugio, '2': final_queda}
som_metalico.opcoes = {'1': ruinas, '2': bosque_claro}
corrente_ar.opcoes = {'1': caverna_entrada, '2': passo_raso}

# Algumas ligações adicionais para garantir que TODOS os nós sejam alcançáveis
# (ligações bidirecionais parciais para navegação mais livre)
# ruinas.opcoes.setdefault('4', puente := None)
# (o operator acima é só para manter consistência; não é usado)

# FUNÇÕES AUXILIARES

def listar_opcoes(caminho):
    # Retorna lista de (label, descrição curta, destino_id)
    items = []
    for i, (label, destino) in enumerate(caminho.opcoes.items(), start=1):
        #criar uma decrição com o texto do destino
        descricao = getattr(destino, 'texto', '')
        # use primeira linha como descrição curta
        descricao_short = descricao.strip().splitlines()[0] if descricao else destino.id
        #item = número da opção, descricao, id do detino e texto original
        items.append((str(i), descricao_short, destino.id, label))
    return items

# função principal do jogo
def jogar():
    limpar()
    print("Bem-vindo à".center(70))
    print("ESCALADA: Chegue ao topo ou não".center(70, "█"))
    time.sleep(1)

    atual = inicio

    # ciclo do jogo
    while True:
        limpar()
        # mostra texto do nó atual
        print(f"Local: {atual.id}\n")
        print(atual.texto)

        #verifica se é o ponto final, se for, o jogo acaba
        if atual.eh_final():
            print(atual.final)
            break

        # lista opções de caminhos a partir do ponto atual para o usuário
        lista_opcoes = listar_opcoes(atual)
        if not lista_opcoes:
            print("Não há caminhos daqui — fim prematuro.")
            break

        print('\nO que você faz?')
        for numero_opcao, descricao, id_destino, rotulo_original in lista_opcoes:
            print(f"{numero_opcao}. Ir para: {id_destino}")
        print("0. Sair do jogo")

        escolha = input("Sua escolha: ").strip()
        if escolha == '0':
            print("Você decidiu abandonar a escalada. Fim de jogo.")
            break

        # tenta transformar a escolha em um número
        try:
            n = int(escolha)
            if 1 <= n <= len(lista_opcoes): #verifica se a escolha corresponde a alguma opção
                _, _, id_destino, rotulo_original = lista_opcoes[n - 1]
                destino = atual.opcoes[rotulo_original] # seleciona o destino a partir do valor do rótulo original
                print(f"\nIndo para {destino.id}...")
                time.sleep(0.8)
                atual = destino #muda o atual para o destino
                continue
            else:
                raise ValueError  #númro inválido
        except Exception:
            print("Escolha inválida — tente novamente.")
            time.sleep(1)
            continue


if __name__ == '__main__':
    while True:
        jogar()
        again = input("\nDeseja jogar novamente? (s/n): ").strip().lower()
        if again != 's':
            limpar()
            print("Obrigado por jogar! Até a próxima escalada.")
            time.sleep(1.5)
            break
