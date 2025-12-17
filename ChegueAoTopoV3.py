import os #módulo para auxiliar a visualização do jogo, será utilizado apenas para limpar a tela e melhorar a visualização de cada etapa
import time #módulo time para manter um fluxo controlado
import graphviz #módulo para gerar a árvore ao final
from IPython.display import Image, display #será utilizado na geração da imagem

# Limpa a tela
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

# Classe dos Nós
class No:
    def __init__(self, id, texto=None, opcoes=None, final=None):
        self.id = id #será o identificador do nó para ser puxado na árvore
        self.texto = texto or '' #texto descritivo do nó
        self.opcoes = opcoes or {} #opções de nós que poderá ser atingido a partir do nó que você está
        self.final = final #texto do nó folha, ou seja, o nó que marcará o final do jogo

    def eh_final(self): #verificação se o nó é uma folha ou não
        return self.final is not None

# construção dos Nós finais, recebe apenas o id e o final como parametros 
final_topo = No('Arriscar tudo', final="""
VOCÊ CHEGOU AO TOPO DA MONTANHA!
O vento sopra forte. O sol nasce.
Você ergue os braços em vitória!
PARABÉNS, AVENTUREIRO!""")
final_sem_saida = No('Parede_de_Pedra', final="""
CAMINHO SEM SAÍDA
Você chega a uma parede de pedra lisa.
Sem equipamentos... só resta voltar.
Derrota silenciosa...""")
final_queda = No('Pular', final="""
VOCÊ CAIU!!!
Seus pés escorregam na quando salta.
Você tenta se agarrar... mas é tarde.
*Game Over*""")
final_fog = No('Tentar_atravessar', final="""
PERDIDO NA NEBLINA
A névoa engole seus passos.
Você vaga sem rumo até cair exausto.
Fim trágico...""")
final_sabedoria = No('Falar_com_ancião', final="""
SABEDORIA DO ANCIÃO
Um velho guia lhe ensina um caminho secreto.
Com conhecimento, você atravessa a montanha.
Vitória pacífica.""")
final_caverna = No('Entrar_na_caverna', final="""
CAVERNA ESCURA
Dentro da caverna você encontra um lago subterrâneo.
As paredes desabam silenciosamente.
Você não consegue sair.""")
final_sucesso_parcial = No('Subir_plataforma', final="""
MEIO TOPO - parcialmente vitorioso
Você alcança uma plataforma elevada.
Não é o topo, mas é um lugar seguro para acampar.
Missão parcialmente cumprida.""")
final_pedra_precaria = No('Passar_pelas_pedras', final="""
PONTA INSTÁVEL
Uma pedra onde você pisa se solta.
Você consegue escapar por pouco, machucado.
Volte mais preparado.""")
final_resgate = No('Fazer_sinais_de_socorro', final="""
RESGATE INESPERADO - Vitória
Um helicóptero avista sua signal.
Você é resgatado para segurança.
Sobrevivência com honra.""")
final_tesouro = No('Pegar_tesouro', final="""
TESOURO ESCONDIDO - parcialmente vitorioso
Você encontra um pequeno tesouro deixado por antigos escaladores.
Não leva ao topo, mas muda seu destino.""")
passagem_desmoronada = No("Passagem_arriscada", final = """
A trilha pela lateral do penhasco termina abruptamente. 
Rochas soltas cedem sob o peso, e a passagem desaba, levando tudo consigo para o abismo abaixo.""" )
colapso_final = No("Arriscar_verificar_sala",final="""
Um estalo seco ecoa pelo ambiente. As engrenagens cedem, puxando vigas e correntes junto. 
Em segundos, a estrutura inteira começa a desmoronar, soterrando tudo sob metal e pedra.""")
final_queda_eixo = No("Verificar_eixo",final="""
Ao se aproximar do eixo central, o chão cede sem aviso. A queda é rápida e descontrolada, 
terminando em um impacto seco no fundo da estrutura. A escuridão toma conta, e o moinho finalmente silencia.""")
correnteza_fatal = No("Mergulhar",final="""
Ao mergulhar a mão na água fria, você consegue agarrar o objeto brilhante: um artefato antigo, coberto por símbolos desgastados. 
No entanto, o esforço desequilibra seu corpo, e a corrente começa a puxar com mais força.""")
emboscada = No("Verificar_sinais",final="""
Ao seguir os sinais, o silêncio se torna pesado demais. 
De repente, sombras surgem entre as árvores. Não há tempo para reagir. O caminho era uma armadilha desde o início.""")
ataque_animal = No("Verificar_barulho", final="""
Um rosnado ecoa próximo demais.
Antes que consiga reagir, algo salta da vegetação.
O ataque é rápido, violento e inesperado.
O terreno irregular impede a fuga,
e a montanha testemunha mais um fim silencioso.""")
topo_ao_amanhecer = No( "topo_ao_amanhecer", final="""
vitória - Exausto, você dá o último passo enquanto o sol começa a surgir no horizonte.
O topo é alcançado em silêncio, banhado pela luz do amanhecer.
Não há gritos, apenas respiração pesada e alívio.
A montanha foi vencida.
Você chegou onde poucos chegam.""")
desaparecido_na_neblina = No("ir_na_neblina",final="""
Seus rastros desaparecem lentamente, engolidos pela névoa.
Nenhum corpo é encontrado.
Com o tempo, seu desaparecimento se transforma em lenda.""")
erro_de_calculo = No("erro_de_calculo",final="""
Um passo mal calculado.
Uma pedra solta.
Um instante de desequilíbrio.
A queda é rápida e definitiva.""")
refugio_seguro = No("refugio_seguro",final="""
parcialmente vitorioso - Contra todas as expectativas, você encontra um abrigo sólido.
Não é o topo da montanha,
mas é sobrevivência.
Às vezes, vencer é saber parar.""")
segredo_da_montanha = No("ver_segredo_da_montanha",final="""
parcialmente vitorioso - Em uma câmara escondida, registros antigos revelam
por que tantos falharam antes.
O conhecimento adquirido muda sua visão da montanha para sempre.""")
aprisionado_pelo_deslizamento = No("seguir_caminho", final="""
Um estrondo ecoa pelos picos.
Rochas e gelo bloqueiam a única saída.
O silêncio que se segue é absoluto.""")
ataque_pantera = No( "seguir_pegada",final="""
O silêncio da floresta se torna absoluto.
Sem aviso, um impacto violento o derruba no chão.
A pantera surge das sombras, rápida e precisa,
atacando antes mesmo que você consiga vê-la por completo.
O terreno irregular impede qualquer reação eficaz.
Em poucos segundos, tudo termina.
A montanha volta ao silêncio, como se nada tivesse acontecido.""")
gps_encontrado = No( "gps", final="""
Vitória - Entre a neve e equipamentos abandonados, você encontra um GPS ainda funcional.
A bateria é suficiente e o aparelho marca sua posição com precisão.
Você não chegou ao topo da montanha,
mas agora sabe exatamente onde está e como sair com segurança.
Uma vantagem decisiva conquistada.""")
ataque_de_urso = No("explorar", final="""
O silêncio é quebrado por um rosnado grave atrás de você.
Antes que consiga reagir, um urso emerge da mata, enorme e furioso,
defendendo território ou cria.
Você tenta recuar, mas o terreno irregular impede a fuga.
O impacto é brutal.
A montanha testemunha mais um fim selvagem""")
mapa_corrigido = No("mapa", final="""
Vitória - Entre papéis rasgados e anotações antigas, você consegue reorganizar um mapa confiável.
Rotas perigosas ficam claras, assim como um caminho seguro de retorno.
O topo não foi alcançado,
mas agora a montanha perdeu parte de seu mistério.
""")
rota_segura_descoberta = No("rota_descoberta",final="""
parcialmente vitorioso - Após seguir marcas quase apagadas na rocha, você identifica uma rota segura de descida.
Ela não leva ao topo,
mas garante que você saia da montanha sem arriscar a vida novamente.
Conhecimento conquistado.""")
equipamento_recuperado = No("equipamento",final="""
parcialmente vitorioso - Você encontra equipamentos deixados por antigos escaladores:
cordas resistentes, grampos e suprimentos.
A escalada termina aqui,
mas agora você possui os meios certos para tentar novamente no futuro.""")
registro_dos_exploradores = No("registro", final="""
parcialmente vitorioso - Em um compartimento escondido, você encontra um diário detalhado.
Relatos de falhas, quedas e decisões erradas revelam como sobreviver à montanha.
Você não chegou ao topo,
mas voltou com informações que valem mais que glória.""")
topo_conquistado = No("tentar_subir",final="""
Após a última subida, o terreno finalmente se estabiliza.
Você está no topo da montanha.
O vento sopra forte, as nuvens ficam abaixo dos seus pés
e o mundo parece pequeno diante da conquista.
Cada risco valeu a pena.
Vitória absoluta.""")
queda_no_abismo = No("continuar_arriscando",final="""
Uma rajada de vento forte atinge seu corpo no momento errado.
O pé escorrega na pedra solta,
e o mundo se torna apenas queda e silêncio.""")
queda_na_ponte = No("seguir_na_ponte",final="""
Uma das tábuas se solta.
O estalo ecoa alto demais.
Antes que possa reagir, a ponte cede e você cai no vazio.""")
queda_na_encosta = No("manter_na_encosta",final="""
As pedras começam a rolar sob seus pés.
Você tenta se apoiar, mas a encosta inteira desliza.
A queda é longa e incontrolável.""")
queda_por_deslizamento = No("continuar_atravessando", final="""
As pedras sob seus pés começam a se mover.
Em segundos, o chão inteiro desliza encosta abaixo.
Você tenta se firmar, mas é arrastado junto,
desaparecendo entre rochas e neve.""")

# Dicionário onde será armazenado os nós
nodes = {}

# Função para criar nós intermediários
def N(id, texto=''): 
    caminho = No(id, texto=texto)#a função criará o nó com o id e o texto descritivo
    nodes[id] = caminho #é adicionado o nó no dicionário criado anteriormente
    return caminho

# Criação dos nós intermediários com a função
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
riacho = N('Riacho',"""
Um pequeno riacho corta a trilha. Água limpa, parece potável.
Ao seguir o rio você pode chegar em um acampamento...
Se preferir arriscar, pode ir seguindo um rastro que viu antes de chegar ao riacho
""")
vento_forte = N('Vento_forte',
'Ventos fortes sopram pedras soltas. você fica com medo. Você pode ir em passos rasos ou para ir rapidamente até uma ladeira que avistou...')
arvore_caida = N('Arvore_caida',
'Uma árvore caída forma uma ponte sobre um córrego. você atravessa, mas mais a frente há um riacho que dá para atravessar andando ou pode ir até um caminho meio nebuloso')
pegada = N('Pegada',"""
Pegadas frescas seguem por uma trilha estreita.
Ao chegar em um ponto você vê uma pedra com escritas e uma entrada de caverna.
Você percebe que não pode ir em ambos devido a noite que está chegado, então deve escolher...""")
trilha_antiga = N('Trilha_antiga',
'Uma trilha antiga com corrimões de madeira fez você chegar em um ponto que deve passar por uma encosta de rochas, não há escolhas')
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
plataforma_oposta = N("plataforma_oposta",
"Após atravessar a ponte, você alcança uma plataforma de pedra cravada na lateral do penhasco. O local parece ter sido usado como ponto de observação ou apoio, com marcas de ferramentas antigas nas paredes. Daqui, é possível ver boa parte do vale, mas o vento forte dificulta permanecer por muito tempo.")
tunel_subterraneo = N("tunel_subterraneo", 
"Um túnel estreito se estende sob o moinho, cavado diretamente na rocha. O ar é frio e úmido, e gotas de água escorrem pelas paredes. O silêncio é quebrado apenas pelo eco distante de passos e pelo som abafado de algo se movendo nas profundezas.")
pegar_objeto = N("pegar_objeto",
"Ao mergulhar a mão na água fria, você consegue agarrar o objeto brilhante: um artefato antigo, coberto por símbolos desgastados. No entanto, o esforço desequilibra seu corpo, e a corrente começa a puxar com mais força.")
trilha_escura = N("trilha_escura",
"A trilha se estreita e a luz natural quase desaparece. Árvores densas bloqueiam o céu, e o chão está coberto por folhas úmidas que abafam os passos. É impossível saber se alguém observa das sombras.")
trilha_dos_ossos = N("trilha_dos_ossos",
"""O caminho se estreita e ossos antigos aparecem parcialmente enterrados na neve. 
Alguns parecem humanos. O vento sopra entre eles, produzindo um som estranho, 
como um aviso silencioso deixado pela montanha.""")
campo_das_cruzes = N("campo_das_cruzes",
"""Cruzes de madeira tortas surgem fincadas no solo congelado. Algumas carregam nomes apagados 
pelo tempo, outras estão quebradas, como se até a memória dos que falharam estivesse se desfazendo.""")
eco_na_neblina = N("eco",
"""Um grito distante ecoa através da névoa densa. Não é possível saber se alguém pede ajuda
ou se o vento brinca com sua mente, testando seus nervos.""")
escadaria_de_pedra = N("escadaria_de_pedra",
"""Degraus antigos surgem cravados diretamente na rocha. Muitos estão quebrados ou cobertos 
por gelo, e não há proteção alguma entre você e o abismo ao lado.""")

# Conexões, adição das opções dos nós, ou seja, os ramos de cada um.
inicio.opcoes = {'1': floresta, 
                 '2': colina}
floresta.opcoes = {'1': rio}
rio.opcoes = {'1': ponte_velha, 
              '2': bifurcacao, 
              '3': arvore_caida}
tunel_subterraneo.opcoes = {'1':eco_na_neblina}
trilha_escura.opcoes = {'1':caminho_dos_campos}
bifurcacao.opcoes = {'1': penhasco, 
                     '2': trilha_longe, }
penhasco.opcoes = {'1': final_topo, 
                   '2': final_sem_saida, 
                   '3': ponte_de_pedra}
acampamento.opcoes = {'1':  final_sabedoria}
ponte_arriscada.opcoes = {'1': atravessar_com_cuidado,
                          '2': descer_pelo_abismo,
                          '3': final_queda}
atravessar_com_cuidado.opcoes = {'1': plataforma_oposta,
                                 '2': queda_no_abismo,}
descer_pelo_abismo.opcoes = { '1': passagem_desmoronada}
neblina.opcoes = {'1': final_fog}
caverna_entrada.opcoes = {'1': ruinas,
                           '2':final_caverna}
colina.opcoes = {'1': pegada, }
ponte_velha.opcoes = {'1': queda_na_ponte}
trilha_longe.opcoes = {'1': ataque_de_urso,}
acampamento_antigo.opcoes = {'1': final_tesouro, 
                             '2': moinho}
moinho.opcoes = {'1':  trilha_antiga,
                 '2': interior_do_moinho,
                 '3': mapa_corrigido,}
interior_do_moinho.opcoes = {'1': tunel_subterraneo,
                             '2': final_queda_eixo}
caminho_dos_campos.opcoes = {'1': rota_segura_descoberta,
                             '2': topo_conquistado,
                             '3': ataque_animal}
bosque_claro.opcoes = {'1': final_sucesso_parcial, 
                       '2': som_metalico}
ruinas.opcoes = {'1': ponte_arriscada,
                 '2': equipamento_recuperado}
ladeira.opcoes = {'1': bosque_claro, 
                  '2': final_pedra_precaria}
barranco.opcoes = {'1': final_resgate, 
                   }
ponte_suspensa.opcoes = {'1': barranco, 
                         '2':vento_forte}
passo_raso.opcoes = {'1': margem_pedregosa,
                     '2': ilhota_submersa}
margem_pedregosa.opcoes = {'1': ponte_suspensa,}
ilhota_submersa.opcoes = {'1': pegar_objeto,
                          '2': correnteza_fatal}
pegar_objeto.opcoes = {'1': gps_encontrado,}
refugio.opcoes = {'1': acampamento, 
                  '2': trilha_dos_sinais,
                  '3': explorar_acampamento}
explorar_acampamento.opcoes = {'1': caverna_entrada}
trilha_dos_sinais.opcoes = {'1': trilha_dos_ossos,
                            '2': emboscada}
encosta_rochosa.opcoes = {'1': passo_raso, 
                          '2': queda_na_encosta}
ponte_de_pedra.opcoes = {'1': refugio, 
                         '2': queda_por_deslizamento}
riacho.opcoes = {'1': acampamento_antigo}
vento_forte.opcoes = {'1':  ladeira }
arvore_caida.opcoes = {'1': riacho, 
                       '2': neblina}
pegada.opcoes = {'1': ataque_pantera }
trilha_antiga.opcoes = {'1': encosta_rochosa}

som_metalico.opcoes = {'1': estrutura_abandonada,
                       '3':desfiladeiro_estreito}
estrutura_abandonada.opcoes = { '1':sala_das_engrenagens,
                        '2': trilha_escura}
sala_das_engrenagens.opcoes = {'1': colapso_final}
desfiladeiro_estreito.opcoes = {'1': registro_dos_exploradores,}
plataforma_oposta.opcoes = {'1':escadaria_de_pedra,
                            '2':campo_das_cruzes}
escadaria_de_pedra.opcoes ={'1':erro_de_calculo,
                            '2':topo_ao_amanhecer}
trilha_dos_ossos.opcoes = {'1':refugio_seguro}   
campo_das_cruzes.opcoes = {'1': aprisionado_pelo_deslizamento,
                           '2': segredo_da_montanha}
eco_na_neblina.opcoes = {'1': desaparecido_na_neblina}

#criação de uma lista com o inicio e os finais
inicio_finais = [
    inicio, final_topo, final_sem_saida, final_queda, final_fog,
    final_sabedoria, final_caverna, final_sucesso_parcial,
    final_pedra_precaria, final_resgate, final_tesouro, passagem_desmoronada,
    colapso_final, final_queda_eixo,correnteza_fatal, emboscada,
    desaparecido_na_neblina,erro_de_calculo, refugio_seguro, segredo_da_montanha,
    aprisionado_pelo_deslizamento, gps_encontrado,
    mapa_corrigido, rota_segura_descoberta, equipamento_recuperado,
    registro_dos_exploradores, queda_no_abismo, queda_na_ponte, queda_na_encosta,
    queda_por_deslizamento, ataque_de_urso, ataque_pantera, topo_conquistado, ataque_animal,
    topo_ao_amanhecer
]
#adição de cada elemento da lista anterior no dicionário de armazenamento dos nós
for f in inicio_finais:
    nodes[f.id] = f

# Funções auxiliares
# função com for recebendo o nó para listar as opções de caminhos/ramos
def listar_opcoes(caminho):
    items = [] #lista para armazenar as opções 
    for i, (label, destino) in enumerate(caminho.opcoes.items(), start=1): #desempacotamento das opções colocando uma numeração
        descricao = getattr(destino, 'texto', '') #puxa o texto descritivo do destino
        descricao_short = descricao.strip().splitlines()[0] if descricao else destino.id #corta o texto descritivo para apenas a primeira linha depois que divide com o splitlines
        items.append((str(i), descricao_short, destino.id, label)) #adiciona na lista de opções como uma tupla
    return items

# Função jogar 
def jogar():
    limpar() #chama a função que utiliza do módulo os para limpar a tela
    print("Bem-vindo à".center(70))
    print("ESCALADA: Chegue ao topo ou não".center(70))
    time.sleep(1) #espera 1s para executar os próximos códigos
    atual = inicio #inicia o jogo no nó chamado inicio
    while True: #loop principal
        limpar()
        print(f"Local: {atual.id}\n") 
        print(atual.texto)
        if atual.eh_final(): #verifica se o nó que o usuário está é um nó final ou intermediário
            print(atual.final)
            break
        lista_opcoes = listar_opcoes(atual) #chama a função de listar as opções do nó atual
        if not lista_opcoes: #caso não tenha opções definidas para aquele nó
            print("Não há caminhos daqui — fim prematuro.")
            break
        print('\nO que você faz?')
        for numero_opcao, descricao_short, id_destino, rotulo_original in lista_opcoes:#for para exibir as opções
            print(f"{numero_opcao}. Ir para: {id_destino}")
        print("0. Sair do jogo")
        escolha = input("Sua escolha: ").strip()
        if escolha == '0':
            print("Você decidiu abandonar a escalada. Fim de jogo.")
            break #caso o usuário decida sair, o jogo finaliza
        try:#tratar erro
            n = int(escolha) #conversão do que é digitado na escolha para int 
            if 1 <= n <= len(lista_opcoes):
                _, _, id_destino, rotulo_original = lista_opcoes[n - 1] #_ é para ignorar os valores que nao influenciarão
                destino = atual.opcoes[rotulo_original]
                print(f"\nIndo para {destino.id}...")
                time.sleep(0.8)
                atual = destino #o atual sempre será atualizado para o nó que o usuário estiver escolhido
                continue
            else:
                raise ValueError #caso o valor passado não seja numero
        except Exception:
            print("Escolha inválida — tente novamente.")
            time.sleep(1)
            continue

#Função para gerar mapa com graphviz
def gerar_mapa():
    dot = graphviz.Digraph("Escalada da Montanha Perigosa", format="png") #cria o gráfico direcionado
    dot.attr(rankdir="TB", size="25,30!", dpi="200") #Define atributos globais do grafo, direção, tamanho e resolução
    dot.attr("node", shape="box", style="filled,rounded", fontname="Helvetica", fontsize="10") #Define atributos padrão para todos os nós.

    # Adiciona todos os nós
    for no_id, no in nodes.items():
        label = f"{no.id}" #texto exibido no nó
        if no.eh_final(): #verifica se o nó é folha
            if "vitória" in no.final.lower(): #configuração do nó final com texto de vitória em sua descrição
                dot.node(no_id, label, fillcolor="limegreen" , fontcolor="white", style="filled,bold")
            elif "parcialmente vitorioso" in no.final.lower(): #configuração do nó final com texto de parcialmente vitorioso em sua descrição
                dot.node(no_id, label, fillcolor="yellow", style="filled,bold")
            else: #configuração padrão para nós de derrota
                dot.node(no_id, label, fillcolor="firebrick", fontcolor="white", style="filled,bold")
                
        elif no_id == "Início": #configuração do nó raiz
            dot.node(no_id, label, fillcolor="lightgrey", style="filled,bold")
        else: #configuração dos nós intermediários
            dot.node(no_id, label, fillcolor="lightskyblue", style="filled")

    # Adiciona setas que mostram o caminho
    for no_id, no in nodes.items():
        for rotulo, dest in no.opcoes.items(): #configuração visual das setas a depender do seu destino
            estilo = {"color": "darkgreen", "penwidth": "3"} if dest.eh_final() and "vitória" in dest.final.lower() else {"color": "yellow", "penwidth": "3"} if dest.eh_final() and "parcialmente vitorioso" in dest.final.lower() else \
                     {"color": "red", "penwidth": "2"} if dest.eh_final() else {"color": "gray"}
            dot.edge(no_id, dest.id, label=rotulo, **estilo)

    # Renderiza e exibe
    dot.render("escalada_mapa", format="png", cleanup=True) #geração da imagem em png
    dot.render("escalada_mapa", format="pdf", cleanup=True) #geração da imagem em pdf
    display(Image("escalada_mapa.png")) #caso use o notebook para testar o código
    print(f"Mapa gerado! {len(nodes)} nós visualizados.") #exive a confirmação da quantidade de nós 

# Loop principal com opção de mapa
while True:
    jogar() #função principal do jogo
    again = input("\nDeseja jogar novamente? (s/n): ").strip().lower() 
    if again not in ['s', 'sim', 'y','yes']: #caso o jogador não queira jogar novamente, basta digitar qualquer coisa diferente dos termos da lista
        limpar()
        print("Obrigado por jogar! Até a próxima escalada.")
        time.sleep(1.5)
        ver_mapa = input("Ver mapa da árvore de decisão? (s/n): ").strip().lower()
        if ver_mapa in ['s', 'sim', 'y','yes']: #caso o jogador queira ver o mapa completo
            gerar_mapa()
            break
        break