import os
import time
import graphviz
from IPython.display import Image, display
# Limpa a tela
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

# Classe dos Nós
class No:
    def __init__(self, id, texto=None, opcoes=None, final=None):
        self.id = id
        self.texto = texto or ''
        self.opcoes = opcoes or {}
        self.final = final

    def eh_final(self):
        return self.final is not None

# Nós finais
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
Seus pés escorregam na quando salta.
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
MEIO TOPO - parcialmente vitorioso
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
RESGATE INESPERADO - Vitória
Um helicóptero avista sua signal.
Você é resgatado para segurança.
Sobrevivência com honra.
""")
final_tesouro = No('Pegar_tesouro', final="""
TESOURO ESCONDIDO - parcialmente vitorioso
Você encontra um pequeno tesouro deixado por antigos escaladores.
Não leva ao topo, mas muda seu destino.
""")
passagem_desmoronada = No("Passagem_arriscada", final = """
A trilha pela lateral do penhasco termina abruptamente. Rochas soltas cedem sob o peso, e a passagem desaba, levando tudo consigo para o abismo abaixo.""" )
colapso_final = No("Arriscar_verificar_sala",final="""
Um estalo seco ecoa pelo ambiente. As engrenagens cedem, puxando vigas e correntes junto. Em segundos, a estrutura inteira começa a desmoronar, soterrando tudo sob metal e pedra.""")
final_queda_eixo = No("Verificar_eixo",final="""
Ao se aproximar do eixo central, o chão cede sem aviso. A queda é rápida e descontrolada, terminando em um impacto seco no fundo da estrutura. A escuridão toma conta, e o moinho finalmente silencia.""")
correnteza_fatal = No("Mergulhar",final="""
Ao mergulhar a mão na água fria, você consegue agarrar o objeto brilhante: um artefato antigo, coberto por símbolos desgastados. No entanto, o esforço desequilibra seu corpo, e a corrente começa a puxar com mais força.""")
emboscada = No("Verificar_sinais",final="""
Ao seguir os sinais, o silêncio se torna pesado demais. De repente, sombras surgem entre as árvores. Não há tempo para reagir. O caminho era uma armadilha desde o início.""")

# Dicionário de nós
nodes = {}

# Função para criar nós
def N(id, texto=''):
    caminho = No(id, texto=texto)
    nodes[id] = caminho
    return caminho

# Criação dos nós intermediários
inicio = N('Início', """
A ESCALADA DA MONTANHA PERIGOSA
Você está na base do Monte da Morte.
Neva forte. O vento uiva.
Você tem três caminhos, escolha com sabedoria.
""")
floresta = N('Floresta', """
Você entra numa floresta densa e escura.
Ouve um riacho ao longe... e vê uma colina íngreme um pouco distante.
Ao olhar para os lados você também vê um caminho com uma placa indicando 50mts de um acampamento e do outro lado vê uma árvore no chão.
""")
rio = N('Rio', """
Um rio gelado bloqueia seu caminho!
Você vê uma ponte velha a alguma distância. Há uma árvore caida ao lado esquerdo do rio e uma bifurcação à direita do rio, mas não parece muito confiável...
""")
bifurcacao = N('Bifurcacao', """
Você encontra uma bifurcação na trilha.
Caminho à esquerda: curto, mas leva a um penhasco
Caminho à direita: suave, mas muito longo

Olhando com calma, você vê algumas pegadas que estão um pouco apagadas e vão por um caminho alternativo...
""")
penhasco = N('Penhasco', """
Você chega a um penhasco estreito e perigoso.
Abaixo, um abismo de 200 metros...

Você tem uma corda que pode lançar e tentar atingir o ponto mais alto arriscando tudo, mas há um caminho que aparentemente te leva para uma parede que você pode tentar escalar.

Ao verificar esses caminhos você também vê uma ponte de pedra que pode seguir.
""")
acampamento = N('Acampamento', """
Você encontra um acampamento abandonado.
Há uma fogueira apagada e um mapa rasgado.
Você vê um ancião estranho, pode ignorar ele e explorar o acampamento antigo
""")
ponte_arriscada = N('Ponte_arriscada', """
A ponte é formada por tábuas velhas presas por cordas gastas. O abismo abaixo é profundo o suficiente para não se ver o fundo. A cada passo, a estrutura range e balança, deixando claro que pode ceder a qualquer momento
""")
atravessar_com_cuidado = N("Atravessar_Com_Cuidado","""
Segurando firmemente nas cordas laterais, o avanço é lento e tenso. Algumas tábuas cedem sob o peso, mas ainda se mantêm presas. O vento balança a ponte, exigindo concentração total para não perder o equilíbrio.
""")
descer_pelo_abismo = N("Descer_pelo_Abismo", """
Um caminho estreito segue pela lateral do penhasco. A descida é íngreme e escorregadia, mas parece mais estável do que a ponte. Qualquer erro pode resultar em uma queda grave.
""")
neblina = N('Neblina', """
Uma neblina espessa desce rápido.
Visibilidade quase zero.

Você viu um acampamento antes de chegar na neblina, pode ir até ele...
Mas está escutando um barulho de água vindo de alguma direção, ou então você se arrisca para atravessar essa neblina...
""")
caverna_entrada = N('Entrada_da_Caverna', """
Você encontra a entrada de uma caverna com inscrições.
Parece perigoso, mas pode ser um atalho.
Parece muito tentador entrar nessa caverna para tentar conseguir algo...

Ao olhar as proximidades você vê algumas ruinas que também pode explorar, mas sente uma corrente de ar que parece te chamar...
""")
colina = N('Colina', """
A colina é íngreme, coberta por pedras soltas.
No topo, você avista uma enorme cruz de pedra.

Lá do alto você consegue ver três áreas: um acampamento, um mirante e um moinho
""")
ponte_velha = N('Ponte_velha', """
A ponte velha está parcialmente quebrada.
Você pode pular uma parte ou tentar caminhos alternativos já que você consegue ver outras duas pontes um pouco mais distante.
""")
trilha_longe = N('Trilha_longe', """
A trilha se estende por muitos quilômetros em ziguezague.
Você encontra uma placa indicando: "Caverna do urso - 5km".
E ao lado um caminho entre árvores que parece tentador
""")
acampamento_antigo = N('Acampamento_antigo', """
Você encontra um barracão em ruínas com símbolos antigos.
Você pode  tentar decifrar esses símbolos que parece dar em um tesouro escondido alí, seguir uma trilha para tentar chegar ao topo e conseguir ajuda ou ir até o moinho do acampamento
""")
moinho = N('Moinho', """
As pás quebradas do moinho giram lentamente, mesmo sem vento aparente. A madeira estala, e o som grave do mecanismo ecoa ao redor. O lugar parece fora do tempo, como se ainda tentasse cumprir sua função, apesar de abandonado há anos.
""")
bosque_claro = N('Bosque_claro', """
O bosque se abre em uma clareira com flores estranhas.
O cheiro é reconfortante.
Há uma meia parede que você pode tentar escalar e vê no que dá...
Você também vê um moinho há uma distância e está ouvindo um barulho de metais vindo de muito perto...
""")
ruinas = N('Ruinas', """
Você encontra ruínas de um antigo abrigo de escaladores.
Há ferramentas enferrujadas e um mapa rasgado.

As ferramentas não estão servindo, mas o mapa marca uma ponte, pode seguir até ela.
Você vê também que os escaladores escreveram algo em algumas pedras, você pode seguir o que eles escreveram e investigar
""")
rastro_animais = N('Rastro_de_animais', """
Há rastros de animais na lama.
Eles seguem para uma trilha que mostra passagem de pessoas, mas está se apagando.
Ao lado do rastro há um bosque que você pode verificar""")
ladeira = N('Ladeira', """
Uma ladeira íngreme bloqueia seu caminho.
As pedras cedem sob seus pés.
Você pode continuar ou seguir o rastro que vê próximo
""")
barranco = N('Barranco', """
Você alcança um barranco com vista para um vale.
Há um heliponto abandonado e uma ladeira.
""")
ponte_suspensa = N('Ponte_suspensa', """
Uma ponte suspensa liga duas falésias.
O vento a balança, mas você consegue atravessar...
De longe você vê um barranco, mas até ele tem que sair passando por caminhos dificeis, há mais próximo uma ponte mais arriscada que há anterior.
Ou você segue enfrentando o vento forte que está nessa altitude...
""")
mirante = N('Mirante', """
Um mirante natural oferece vista para várias trilhas.
Você pode estudar o mapa mentalmente.

Logo abaixo há uma neblina forte e logo ao seu lado tem marcas de pegadas que estão sumindo
""")
passo_raso = N('Passo_raso', """
A água parece calma à primeira vista, cobrindo apenas parte dos tornozelos. No entanto, a corrente empurra com força, e as pedras sob a superfície estão cobertas por limo escorregadio. O barulho constante da água abafa outros sons, tornando difícil perceber qualquer perigo se aproximando.
""")
refugio = N('Refugio', """
Restos de uma fogueira ainda soltam fumaça fina, indicando que alguém esteve ali recentemente. Latas vazias, pedaços de tecido e marcas no chão sugerem pressa na partida. O local oferece abrigo, mas também levanta dúvidas sobre quem passou por ali.
""")
explorar_acampamento = N('Explorar_Acampamento', """
Entre mochilas rasgadas e caixas reviradas, há mapas antigos e anotações incompletas. Algumas rotas estão marcadas com pressa, como se alguém tivesse descoberto algo importante e precisasse sair rápido.
""")
trilha_dos_sinais = N("Trilha_dos_Sinais","""
Pedras empilhadas, galhos quebrados e marcas no chão indicam um caminho improvisado. Alguém claramente queria deixar um rastro, mas não se sabe se era para ajudar… ou atrair.
""""")
encosta_rochosa = N('Encosta_rochosa', """
A encosta é rochosa e exige técnica.
Pode seguir em passos rasos tomando cuidado ou tentar subir...
""")
ponte_de_pedra = N('Ponte_de_pedra', """
Uma ponte natural de pedra forma uma passagem estreita.
Você encontra um refúgio e uma encosta rochosa...
""")
atalho_secreto = N('Atalho_secreto', """
Você descobre um atalho marcado por fitas coloridas.
Parece não ser usado há anos.
Há umas marcas que parecem indicar um tesouro ou uma armadilha...
Há também uma trilha que leva até uma caverna
""")
pedra_escrita = N('Pedra_escrita',
                  """Você encontra uma pedra com inscrições.
                  Nela consta direções para um acampamento e para uma ponte
                  """)
riacho = N('Riacho',
            """Um pequeno riacho corta a trilha. Água limpa, parece potável.
            Ao seguir o rio você pode chegar em um acampamento...
            Se preferir arriscar, pode ir seguindo um rastro que viu antes de chegar ao riacho""")
vento_forte = N('Vento_forte',
                'Ventos fortes sopram pedras soltas. você fica com medo. Você pode ir em passos rasos ou para ir rapidamente até uma ladeira que avistou...')
arvore_caida = N('Arvore_caida',
                  'Uma árvore caída forma uma ponte sobre um córrego. você atravessa, mas mais a frente há um riacho que dá para atravessar andando ou pode ir até um caminho meio nebuloso')
pegada = N('Pegada',
           """Pegadas frescas seguem por uma trilha estreita.
           Ao chegar em um ponto você vê uma pedra com escritas e uma entrada de caverna.
           Você percebe que não pode ir em ambos devido a noite que está chegado, então deve escolher...""")
trilha_antiga = N('Trilha_antiga',
                  'Uma trilha antiga com corrimões de madeira fez você chegar em um ponto que deve passar por uma encosta de rochas, não há escolhas')
tempestade = N('tempestade',
               'O céu escurece rapidamente. Tempestade se aproxima. Você pode correr até o refúgio que passou anteriormente ou corre em frente por uma ponte de madeira que parece')
som_metalico = N('Som_metalico',
                  'Um ruído metálico ecoa entre as pedras, irregular e insistente, como ferro sendo arrastado contra rocha. O som se propaga pelo vale e se mistura ao vento, dificultando saber de onde vem exatamente. Às vezes parece distante, outras vezes próximo demais, fazendo a sensação de estar sendo observado crescer a cada passo.')
estrutura_abandonada = N("Estrutura_ambandonada",
                         "Entre a vegetação densa e pedras cobertas de musgo, surge uma antiga estrutura de metal, tomada pela ferrugem. Vigas tortas e correntes soltas balançam lentamente, produzindo o som que ecoa pela região. Tudo indica que aquilo foi construído há muito tempo, mas abandonado às pressas.")
sala_das_engrenagens = N('Sala_das_Engrenagens',
                         "O interior revela um emaranhado de engrenagens enormes, presas às paredes de pedra. Algumas ainda se movem levemente, rangendo como se estivessem prestes a se soltar. O ar é pesado, impregnado de ferrugem e poeira antiga, e qualquer movimento errado pode provocar um colapso")
desfiladeiro_estreito = N('Desfiladeiro_Estreito',
                          "O caminho se fecha abruptamente entre duas paredes altas de pedra, formando um corredor natural. O som metálico se intensifica aqui, reverberando de forma distorcida. Cada passo ecoa, e o espaço apertado dá a sensação de que não há como recuar rapidamente.")
margem_pedregosa = N("Margem_Pedregosa",
                     "Ao alcançar a outra margem, o terreno se eleva em pedras irregulares. Símbolos rudimentares estão marcados em algumas rochas, como se alguém tivesse deixado avisos ou orientações. O local transmite a sensação de que já foi usado como passagem antes.")
ilhota_submersa = N("Ilhota_Submersa", 
                    "Uma pequena elevação de pedras emerge no meio da água. Algo reflete a luz sob a superfície, chamando atenção. Porém, o nível da água parece subir lentamente, e a corrente ao redor da ilhota fica cada vez mais forte.")
interior_do_moinho = N("Interior_do_Moinho",
                       "O interior é escuro e abafado. O chão está coberto de serragem antiga, madeira podre e poeira. No centro, um eixo profundo desce para a escuridão, com um alçapão parcialmente aberto, sugerindo um caminho que poucos ousariam seguir.")
caminho_dos_campos = N("Caminho_dos_Campos",
                       "Um caminho aberto se estende para campos abandonados. A vegetação cresce de forma desordenada, e o silêncio é tão intenso que chega a incomodar. Não há sinais recentes de passagem, apenas o vento balançando a grama seca.")
corrente_ar = N('Corrente_de_ar',
                'Uma corrente de ar frio sopra por uma fenda. Você sente ela lhe convidando e chega a uma entrada de caverna ao lado de uma escora rochosa com um caminho estreito que você pode passar calmamente')
plataforma_oposta = N("plataforma_oposta",
                      "Após atravessar a ponte, você alcança uma plataforma de pedra cravada na lateral do penhasco. O local parece ter sido usado como ponto de observação ou apoio, com marcas de ferramentas antigas nas paredes. Daqui, é possível ver boa parte do vale, mas o vento forte dificulta permanecer por muito tempo.")
tunel_subterraneo = N("tunel_subterraneo", 
                      "Um túnel estreito se estende sob o moinho, cavado diretamente na rocha. O ar é frio e úmido, e gotas de água escorrem pelas paredes. O silêncio é quebrado apenas pelo eco distante de passos e pelo som abafado de algo se movendo nas profundezas.")
pegar_objeto = N("pegar_objeto",
                 "Ao mergulhar a mão na água fria, você consegue agarrar o objeto brilhante: um artefato antigo, coberto por símbolos desgastados. No entanto, o esforço desequilibra seu corpo, e a corrente começa a puxar com mais força.")
trilha_escura = N("trilha_escura",
                  "A trilha se estreita e a luz natural quase desaparece. Árvores densas bloqueiam o céu, e o chão está coberto por folhas úmidas que abafam os passos. É impossível saber se alguém observa das sombras.")
# Conexões
inicio.opcoes = {'1': floresta, 
                 '2': rio, 
                 '3': colina}
floresta.opcoes = {'1': rio, 
                   '2': colina, 
                   '3': acampamento, 
                   '4': arvore_caida}
rio.opcoes = {'1': ponte_velha, 
              '2': bifurcacao, 
              '3': arvore_caida}
tunel_subterraneo.opcoes = {'1':ruinas,
                     '2':corrente_ar}
trilha_escura.opcoes = {'1':bosque_claro,
                 '2':caminho_dos_campos}
bifurcacao.opcoes = {'1': penhasco, 
                     '2': trilha_longe, 
                     '3': pegada}
penhasco.opcoes = {'1': final_topo, 
                   '2': final_sem_saida, 
                   '3': ponte_de_pedra}
acampamento.opcoes = {'1': acampamento_antigo, 
                      '2': final_sabedoria}
ponte_arriscada.opcoes = {'1': ponte_suspensa, 
                          '2': final_queda,
                          '3': atravessar_com_cuidado,
                          '4': descer_pelo_abismo}
atravessar_com_cuidado.opcoes = {'1': plataforma_oposta,
                                 '2': final_queda}
descer_pelo_abismo.opcoes = { '1': plataforma_oposta,
                             '2': passagem_desmoronada}
neblina.opcoes = {'1': acampamento, 
                  '2': riacho, 
                  '3': final_fog}
caverna_entrada.opcoes = {'1': ruinas,
                           '2': corrente_ar,
                           '3':final_caverna}
colina.opcoes = {'1': acampamento, 
                 '2': mirante, 
                 '3': moinho}
ponte_velha.opcoes = {'1': ponte_arriscada, 
                      '2': ponte_suspensa, 
                      '3': final_queda}
trilha_longe.opcoes = {'1': caverna_entrada, 
                       '2': atalho_secreto, }
acampamento_antigo.opcoes = {'1': final_tesouro, 
                             '2': trilha_longe, 
                             '3': moinho}
moinho.opcoes = {'1':  trilha_antiga,
                 '2': interior_do_moinho,
                 '3': final_sucesso_parcial,
                 '4': caminho_dos_campos}
interior_do_moinho.opcoes = {'1': tunel_subterraneo,
                             '2': final_queda_eixo}
caminho_dos_campos.opcoes = {'1': mirante,
                             '2': bosque_claro}
bosque_claro.opcoes = {'1': final_sucesso_parcial, 
                       '2': moinho, 
                       '3': som_metalico}
ruinas.opcoes = {'1': ponte_velha, 
                 '2': pedra_escrita}
rastro_animais.opcoes = {'1': bosque_claro,
                         '2':trilha_antiga 
                         }
ladeira.opcoes = {'1': rastro_animais, 
                  '2': final_pedra_precaria}
barranco.opcoes = {'1': final_resgate, 
                   '2': ladeira}
ponte_suspensa.opcoes = {'1': barranco, 
                         '2':vento_forte}
mirante.opcoes = {'1': som_metalico, 
                  '2': neblina, 
                  '3': pegada}
passo_raso.opcoes = {'1': final_queda,
                     '2': margem_pedregosa,
                     '3': ilhota_submersa}
margem_pedregosa.opcoes = {'1': pedra_escrita,
                    '2': encosta_rochosa}
ilhota_submersa.opcoes = {'1': pegar_objeto,
                   '2': correnteza_fatal}

refugio.opcoes = {'1': mirante, 
                  '2': acampamento,
                  '3': trilha_dos_sinais,
                  '4': explorar_acampamento}
explorar_acampamento.opcoes = {'1': trilha_antiga,
                               '2': atalho_secreto}
trilha_dos_sinais.opcoes = {'1': encosta_rochosa,
                            '2': emboscada}
encosta_rochosa.opcoes = {'1': passo_raso, 
                          '2': final_sucesso_parcial}
ponte_de_pedra.opcoes = {'1': refugio, 
                         '2': encosta_rochosa}
atalho_secreto.opcoes = {'1': final_tesouro, 
                         '2': caverna_entrada}
pedra_escrita.opcoes = {'1': final_sabedoria, 
                        '2':ponte_suspensa}
riacho.opcoes = {'1': rastro_animais,
                 '2':acampamento_antigo}
vento_forte.opcoes = {'1': passo_raso,
                      '2':ladeira }
arvore_caida.opcoes = {'1': riacho, 
                       '2': neblina}
pegada.opcoes = {'1': pedra_escrita,
                 '2': rastro_animais }
trilha_antiga.opcoes = {'1': encosta_rochosa}
tempestade.opcoes = {'1': refugio, 
                     '2': final_queda}
som_metalico.opcoes = {'1': final_queda,
                       '2': estrutura_abandonada,
                       '3':desfiladeiro_estreito}
estrutura_abandonada.opcoes = { '1':sala_das_engrenagens,
                        '2': trilha_escura}
sala_das_engrenagens.opcoes = {'1': moinho,
                     '2': colapso_final}
desfiladeiro_estreito.opcoes = {'1': passo_raso,
                      '2':final_queda
}

corrente_ar.opcoes = {'1': passo_raso,
                      '2':ponte_velha}

plataforma_oposta.opcoes = {
    '1': mirante,
    '2':encosta_rochosa,
}

inicio_finais = [
    inicio, final_topo, final_sem_saida, final_queda, final_fog,
    final_sabedoria, final_caverna, final_sucesso_parcial,
    final_pedra_precaria, final_resgate, final_tesouro, passagem_desmoronada,
    colapso_final, final_queda_eixo,correnteza_fatal, emboscada
]

for f in inicio_finais:
    nodes[f.id] = f

# Funções auxiliares 
def listar_opcoes(caminho):
    items = []
    for i, (label, destino) in enumerate(caminho.opcoes.items(), start=1):
        descricao = getattr(destino, 'texto', '')
        descricao_short = descricao.strip().splitlines()[0] if descricao else destino.id
        items.append((str(i), descricao_short, destino.id, label))
    return items

# Função jogar 
def jogar():
    limpar()
    print("Bem-vindo à".center(70))
    print("ESCALADA: Chegue ao topo ou não".center(70))
    time.sleep(1)
    atual = inicio
    while True:
        limpar()
        print(f"Local: {atual.id}\n")
        print(atual.texto)
        if atual.eh_final():
            print(atual.final)
            break
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
        try:
            n = int(escolha)
            if 1 <= n <= len(lista_opcoes):
                _, _, id_destino, rotulo_original = lista_opcoes[n - 1]
                destino = atual.opcoes[rotulo_original]
                print(f"\nIndo para {destino.id}...")
                time.sleep(0.8)
                atual = destino
                continue
            else:
                raise ValueError
        except Exception:
            print("Escolha inválida — tente novamente.")
            time.sleep(1)
            continue

# Nova função para gerar mapa com graphviz
def gerar_mapa():
    dot = graphviz.Digraph("Escalada da Montanha Perigosa", format="png")
    dot.attr(rankdir="TB", size="25,30!", dpi="200")
    dot.attr("node", shape="box", style="filled,rounded", fontname="Helvetica", fontsize="10")

    # Adiciona todos os nós
    for no_id, no in nodes.items():
        label = f"{no.id}..."
        if no.eh_final():
            if "vitória" in no.final.lower():
                dot.node(no_id, label, fillcolor="limegreen" , fontcolor="white", style="filled,bold")
            elif "parcialmente vitorioso" in no.final.lower():
                dot.node(no_id, label, fillcolor="yellow", style="filled,bold")
            else:
                dot.node(no_id, label, fillcolor="firebrick", fontcolor="white", style="filled,bold")
                
        elif no_id == "Início":
            dot.node(no_id, label, fillcolor="lightgrey", style="filled,bold")
        else:
            dot.node(no_id, label, fillcolor="lightskyblue", style="filled")

    # Adiciona arestas
    for no_id, no in nodes.items():
        for rotulo, dest in no.opcoes.items():
            estilo = {"color": "darkgreen", "penwidth": "3"} if dest.eh_final() and "topo" in dest.id.lower() else \
                     {"color": "red", "penwidth": "2"} if dest.eh_final() else {"color": "gray"}
            dot.edge(no_id, dest.id, label=rotulo, **estilo)

    # Renderiza e exibe
    dot.render("escalada_mapa", format="png", cleanup=True)
    dot.render("escalada_mapa", format="pdf", cleanup=True)
    display(Image("escalada_mapa.png"))
    print(f"Mapa gerado! {len(nodes)} nós visualizados.")

# Loop principal com opção de mapa
while True:
    jogar()
    again = input("\nDeseja jogar novamente? (s/n): ").strip().lower()
    if again != 's':
        limpar()
        print("Obrigado por jogar! Até a próxima escalada.")
        time.sleep(1.5)
        ver_mapa = input("Ver mapa da árvore de decisão? (s/n): ").strip().lower()
        if ver_mapa in ['s', 'sim']:
            gerar_mapa()
            break
        break