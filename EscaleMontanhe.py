import os
import time

# Limpa a tela

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

# CLASSE DOS NÓS DA HISTÓRIA
class No:
    def __init__(self, texto=None, opcoes=None, final=None):
        self.texto = texto
        self.opcoes = opcoes or {}
        self.final = final

    def eh_final(self):
        return self.final is not None

# VÁRIOS FINAIS (diversos desfechos para enriquecer a árvore)
final_topo = No(final="""
VOCÊ CHEGOU AO TOPO DA MONTANHA!

O vento sopra forte. O sol nasce.
Você ergue os braços em vitória!

PARABÉNS, AVENTUREIRO!
""")

final_sem_saida = No(final="""
CAMINHO SEM SAÍDA

Você chega a uma parede de pedra lisa.
Sem equipamentos... só resta voltar.

Derrota silenciosa...
""")

final_queda = No(final="""
VOCÊ CAIU!!!

Seus pés escorregam na pedra molhada.
Você tenta se agarrar... mas é tarde.

*Game Over*
""")

final_fog = No(final="""
PERDIDO NA NEBLINA

A névoa engole seus passos.
Você vaga sem rumo até cair exausto.

Fim trágico...
""")

final_sabedoria = No(final="""
SABEDORIA DO ANCIÃO

Um velho guia lhe ensina um caminho secreto.
Com conhecimento, você atravessa a montanha.

Vitória pacífica.
""")

final_caverna = No(final="""
CAVERNA ESCURA

Dentro da caverna você encontra um lago subterrâneo.
As paredes desabam silenciosamente.

Você não consegue sair.
""")

final_sucesso_parcial = No(final="""
MEIO TOPO

Você alcança uma plataforma elevada.
Não é o topo, mas é um lugar seguro para acampar.

Missão parcialmente cumprida.
""")

final_pedra_precaria = No(final="""
PONTA INSTÁVEL

Uma pedra onde você pisa se solta.
Você consegue escapar por pouco, machucado.

Volte mais preparado.
""")

final_resgate = No(final="""
RESGATE INESPERADO

Um helicóptero avista sua signal.
Você é resgatado para segurança.

Sobrevivência com honra.
""")

final_tesouro = No(final="""
TESOURO ESCONDIDO

Você encontra um pequeno tesouro deixado por antigos escaladores.
Não leva ao topo, mas muda seu destino.
""")

# NÓS BÁSICOS E RAMIFICAÇÕES
penhasco = No(
    texto="""
Você chega a um penhasco estreito e perigoso.
Abaixo, um abismo de 200 metros...

O que você faz?
1. Passa devagar e com cuidado
2. Corre para ganhar tempo
""",
    opcoes={
        "1": final_topo,
        "2": final_queda
    }
)

bifurcacao = No(
    texto="""
Você encontra uma bifurcação na trilha.

Caminho à esquerda: íngreme, mas curto
Caminho à direita: suave, mas muito longo

Qual você escolhe?
1. Caminho íngreme (curto)
2. Caminho suave (longo)
""",
    opcoes={
        "1": penhasco,
        "2": final_sem_saida
    }
)

rio = No(
    texto="""
Um rio gelado bloqueia seu caminho!

Você vê pedras escorregadias no meio da corrente...
Ou uma ponte velha de madeira a 500m dali.

O que faz?
1. Pula pelas pedras (rápido)
2. Vai até a ponte (seguro, mas demorado)
""",
    opcoes={
        "1": bifurcacao,
        "2": final_sem_saida
    }
)

floresta = No(
    texto="""
Você entra numa floresta densa e escura.

Ouve um riacho ao longe... e vê uma colina íngreme.

Para onde vai?
1. Segue o som do riacho
2. Sobe a colina
""",
    opcoes={
        "1": rio,
        "2": bifurcacao
    }
)
inicio = No( texto=""" 
A ESCALADA DA MONTANHA PERIGOSA Você está na base do Monte da Morte. 
Neva forte. O vento uiva. Só os mais corajosos chegam ao topo... 

Você verifica sua mochila. 
Pode levar apenas UM item: 
1. Um MAPA detalhado da montanha 
2. Uma BÚSSOLA confiável Qual você escolhe? (1 ou 2) """, 
opcoes={ "1": floresta, 
         "2":rio})

# Novos nós com alternativas
acampamento = No(
    texto="""
Você encontra um acampamento abandonado.
Há uma fogueira apagada e um mapa rasgado.

O que faz?
1. Revira o acampamento em busca de itens
2. Ignora e segue em frente
""",
    opcoes={
        "1": final_sabedoria,
        "2": floresta
    }
)

ponte_arriscada = No(
    texto="""
A ponte range quando você pisa nela.
Do outro lado, há uma trilha com marcas antigas.

O que faz?
1. Atravessa com cuidado
2. Volta e busca outra rota
""",
    opcoes={
        "1": bifurcacao,
        "2": rio
    }
)

neblina = No(
    texto="""
Uma neblina espessa desce rápido.
Visibilidade quase zero.

O que faz?
1. Anda devagar, atento aos sons
2. Procura abrigo até a neblina passar
""",
    opcoes={
        "1": final_fog,
        "2": acampamento
    }
)

caverna_entrada = No(
    texto="""
Você encontra a entrada de uma caverna com inscrições.
Parece perigoso, mas pode ser um atalho.

O que faz?
1. Entra na caverna
2. Contorna pela trilha externa
""",
    opcoes={
        "1": final_caverna,
        "2": bifurcacao
    }
)

colina = No(
    texto="""
A colina é íngreme, coberta por pedras soltas.
No topo, você avista uma enorme cruz de pedra.

O que faz?
1. Sobe a colina para olhar ao redor
2. Desvia pela encosta para economizar energia
""",
    opcoes={
        "1": acampamento,
        "2": neblina
    }
)

ponte_velha = No(
    texto="""
A ponte velha está parcialmente quebrada.
Você pode pular uma parte ou consertar provisoriamente.

O que faz?
1. Pula a parte danificada
2. Usa corda improvisada para consertar
""",
    opcoes={
        "1": ponte_arriscada,
        "2": final_queda
    }
)

trilha_longe = No(
    texto="""
A trilha se estende por muitos quilômetros em ziguezague.
Você encontra uma placa indicando: "Santuário — 12 km".

O que faz?
1. Vai pelo atalho indicado pela placa
2. Segue a trilha principal
""",
    opcoes={
        "1": caverna_entrada,
        "2": penhasco
    }
)

# NÓS ADICIONAIS - muitos deles para criar profundidade e variedade
acampamento_antigo = No(
    texto="""
Você encontra um barracão em ruínas com símbolos antigos.

O que faz?
1. Investiga os símbolos
2. Evita o lugar e segue adiante
""",
    opcoes={
        "1": final_tesouro,
        "2": trilha_longe
    }
)

moinho = No(
    texto="""
Um velho moinho de vento aparece no topo de uma colina baixa.
Há uma velha corda pendurada.

O que faz?
1. Usa a corda para subir
2. Contorna o moinho
""",
    opcoes={
        "1": ponte_velha,
        "2": acampamento_antigo
    }
)

bosque_claro = No(
    texto="""
O bosque se abre em um clareira com flores estranhas.
O cheiro é reconfortante.

O que faz?
1. Descansa um pouco
2. Vai direto sem parar
""",
    opcoes={
        "1": final_sucesso_parcial,
        "2": moinho
    }
)

ruinas = No(
    texto="""
Você encontra ruínas de um antigo abrigo de escaladores.
Há ferramentas enferrujadas.

O que faz?
1. Pega ferramentas úteis
2. Continua, desconfiado
""",
    opcoes={
        "1": ponte_velha,
        "2": caverna_entrada
    }
)

rastro_animais = No(
    texto="""
Há rastros de animais na lama.
Eles seguem para uma formação rochosa.

O que faz?
1. Segue os rastros
2. Foge para evitar predadores
""",
    opcoes={
        "1": ruinas,
        "2": bosque_claro
    }
)

ladeira = No(
    texto="""
Uma ladeira íngreme bloqueia seu caminho.
As pedras cedem sob seus pés.

O que faz?
1. Desce com cuidado
2. Tenta escalar lateralmente
""",
    opcoes={
        "1": rastro_animais,
        "2": final_pedra_precaria
    }
)

barranco = No(
    texto="""
Você alcança um barranco com vista para um vale.
Há um heliponto abandonado.

O que faz?
1. Acende um sinal de fumaça
2. Grita pedindo ajuda
""",
    opcoes={
        "1": final_resgate,
        "2": ladeira
    }
)

ponte_suspensa = No(
    texto="""
Uma ponte suspensa liga duas falésias.
O vento a balança.

O que faz?
1. Avança firmemente
2. Retrocede com cautela
""",
    opcoes={
        "1": barranco,
        "2": ponte_arriscada
    }
)

mirante = No(
    texto="""
Um mirante natural oferece vista para várias trilhas.
Você pode estudar o mapa mentalmente.

O que faz?
1. Analisa as trilhas
2. Escolhe aleatoriamente uma trilha
""",
    opcoes={
        "1": trilha_longe,
        "2": neblina
    }
)

passo_raso = No(
    texto="""
Um passo raso exige equilíbrio.

O que faz?
1. Segue devagar
2. Pula rápido
""",
    opcoes={
        "1": ponte_suspensa,
        "2": final_queda
    }
)

refugio = No(
    texto="""
Um pequeno refúgio de pedra oferece abrigo.
Há mantimentos secos.

O que faz?
1. Restaura energias
2. Usa mantimentos apenas parcialmente
""",
    opcoes={
        "1": mirante,
        "2": acampamento
    }
)

encosta_rochosa = No(
    texto="""
A encosta é rochosa e exige técnica.

O que faz?
1. Usa as mãos e sobe
2. Procura outra passagem
""",
    opcoes={
        "1": passo_raso,
        "2": rastro_animais
    }
)

ponte_de_pedra = No(
    texto="""
Uma ponte natural de pedra forma uma passagem estreita.

O que faz?
1. Atravesse concentrado
2. Retrocede e procura alternativa
""",
    opcoes={
        "1": refugio,
        "2": encosta_rochosa
    }
)

atalho_secreto = No(
    texto="""
Você descobre um atalho marcado por fitas coloridas.
Parece não ser usado há anos.

O que faz?
1. Segue o atalho
2. Fica na trilha principal
""",
    opcoes={
        "1": final_tesouro,
        "2": trilha_longe
    }
)

# NÓS DE TRANSIÇÃO ADICIONAIS
n1 = No(texto="""
Você encontra uma pedra com inscrições.

O que faz?
1. Lê as inscrições
2. Ignora e segue
""", opcoes={"1": acampamento_antigo, "2": ponte_de_pedra})

n2 = No(texto="""
Um pequeno riacho corta a trilha.
Água limpa, parece potável.

O que faz?
1. Beber água
2. Encher a cantina e seguir
""", opcoes={"1": refugio, "2": rastro_animais})

n3 = No(texto="""
Ventos fortes sopram pedras soltas.

O que faz?
1. Abriga-se atrás de uma rocha
2. Corre até um abrigo próximo
""", opcoes={"1": passo_raso, "2": ponte_suspensa})

n4 = No(texto="""
Uma árvore caída forma uma ponte sobre um córrego.

O que faz?
1. Usa a árvore para cruzar
2. Procura caminho alternativo
""", opcoes={"1": n2, "2": neblina})

n5 = No(texto="""
Pegadas frescas seguem por uma trilha estreita.

O que faz?
1. Segue as pegadas
2. Volta para a trilha principal
""", opcoes={"1": n1, "2": mirante})

n6 = No(texto="""
Uma trilha antiga com corrimões de madeira.

O que faz?
1. Segue a trilha segura
2. Ignora e escala pelas pedras
""", opcoes={"1": ponte_suspensa, "2": encosta_rochosa})

n7 = No(texto="""
O céu escurece rapidamente.
Tempestade se aproxima.

O que faz?
1. Procura abrigo imediato
2. Continua correndo
""", opcoes={"1": refugio, "2": final_queda})


n8 = No(texto="""
Um som metálico ecoa por entre as rochas.

O que faz?
1. Vai investigar
2. Mantém distância
""", opcoes={"1": ruinas, "2": bosque_claro})

n9 = No(texto="""
Uma corrente de ar frio sopra por uma fenda.

O que faz?
1. Explora a fenda
2. Evita a fenda
""", opcoes={"1": caverna_entrada, "2": passo_raso})

# FUNÇÃO PRINCIPAL DO JOGO

def jogar():
    limpar()
    print("Bem-vindo à".center(70))
    print("ESCALADA DA MORTE".center(70, "█"))
    time.sleep(1.2)

    atual = inicio

    while not atual.eh_final():
        limpar()
        print(atual.texto)

        escolha = input(" → Sua escolha: ").strip()

        if escolha not in atual.opcoes:
            print("\nOpção inválida! Tente novamente.")
            time.sleep(1.2)
            continue

        print(f"\nVocê escolheu: {escolha}")
        time.sleep(0.9)

        atual = atual.opcoes[escolha]

    limpar()
    print(atual.final)
    time.sleep(2.5)

# EXECUÇÃO
if __name__ == '__main__':
    while True:
        jogar()
        limpar()
        novamente = input("\nDeseja tentar novamente? (s/n): ").strip().lower()
        if novamente != 's':
            limpar()
            print("Obrigado por jogar! Até a próxima escalada... se sobreviver.")
            time.sleep(2)
            break

