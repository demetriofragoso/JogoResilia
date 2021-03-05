def comecar_jogo():
    print()
    print(">>> Digite o nome do seu personagem...")
    nome = input("")
    print()
    print("Escolha o que seu personagem no filme.\n"
        "[Estágiario]\n"
        "[Pesquisador]\n"
        "[Professor]\n")
    print("Escolha o que seu personagem no filme!")
    personagem = input("")
    print()
    input('>>> Aperte enter para continuar...')
    sleep(1)
    print()
    print("Uma produtora de filmes brasileiro está no Egito para as gravações do novo filme que será lançado \n" 
    "em 2022 com um elenco de estrelas como, Juliana Paes (Cleópatra) e Rodrigo Lombardi (Marco Antônio).\n" 
    "Entre essas estrelas está um",personagem,"que se chama" ,nome, "ele é apaixonado pela civilização egípcia \n"
    "com isso está auxiliando a produção, junto com o seu chefe Jacó para o roteiro da história não fugir\n"
    "dos acontecimentos históricos vividos na época da civilização egípcia.")
    sleep(3)
    print()
    input('>>> Aperte enter para continuar...')
    print()
    print("Em um certo momento da gravação o produtor do filme resolveu consultar mais informações históricas \n"
    "sobre Cleópatra a equipe de arqueologia onde" ,nome, "fazia parte, com isso o chefe Jacó procurou você e disse: ")
    sleep(2)
    print()
    print(f"{'='*120}")
    print(" Você deve se dirigir a biblioteca nacional do Egito amanhã cedo para coletar mais informações \n"
            "sobre a Rainha Cleópatra, traga tudo anotado e registre documentos históricos.")
    print(f"{'='*120}")
    sleep(2)
    print()
    input('>>> Aperte enter para continuar...')
    print()
    print("Chegando à biblioteca nacional, muito empolgado já começa a buscar todos os livros e documentos \n"
    "históricos sobre Cleópatra, conforme o seu chefe pediu.  Enquanto procurava os livros aparece um homem \n"
    "velho com um cajado de madeira e uma manta cobrindo parcialmente o seu rosto se aproxima de você e diz...")
    sleep(2)
    print()
    input('>>> Aperte enter para continuar...')
    print()
    print(f"{'='*120}")
    print("Vejo que você não é daqui, vejo também que procura algo sobre Cleópatra a nossa Rainha,\n"
    "tenho informações que você não vai encontrar nessa biblioteca, que irá te deixar perplexo, já parou \n"
    "para pensar que você pode ficar olho a olho coma nossa Rainha VIVA? ")
    print(f"{'='*120}")
    sleep(3)
    print()
    input('>>> Aperte enter para continuar...')
    print()
    print("Deseja me acompanhar até o porão da biblioteca? ")
    print()
    print("[A] - Sim, irei acompanhar você! Espero que seja verdade tudo isso que você fala!")
    print()
    print("[B] - Não acredito em você, és mais um velho mendigo que fica perturbando \n"
        "     a todos, saia da minha frente estou com pressa preciso entregar ao meu chefe as informações.")
    print()
    resposta_1 = input("Escolha entre a opção A ou B: ")
    print()
    while True:
        if resposta_1 == "A":
            print("Ótimo, garoto você não vai se arrepender! Mantenha os seus olhos e ouvidos atentos\n"
            "a partir de agora!")
            break
        elif resposta_1 == "B":
            print("FIM DE JOGO!")
            print("Você voltou aos estudios de gravação entregou os livros e documentos sobre Cleópatra a produção \n"
            "e seu chefe o parabenizou!")
            print("Volte do inicio...tente novamente!")
            comecar_jogo()
            break
    sleep(1)
    print()
    input('>>> Aperte enter para continuar...')
    print()
    print(f"{'='*120}")
    print("Ao chegar ao local, você se assusta com um lugar escuro e sombrio e cheio\n"
        "de múmias, sarcófagos e armas egípcias.")
    print(f"{'='*120}")
    sleep(1)
    print()
    input('>>> Aperte enter para continuar...')
    print()
    print("Você fica com medo e pensa em voltar, o que você vai fazer?")
    print("[A] - Continuar!")
    print()
    print("[B] - Estou com muito medo, vou voltar a biblioteca")
    print()
    resposta_2 = input("Escolha entre a opção A ou B: ")
    print()
    while True:
        if resposta_2 == "A":
            print("Você é muito corajoso!")
            break
        elif resposta_2 == "B":
            print("FIM DE JOGO!")
            print("Velho misterioso fala...'OK, iremos voltar, depois não venha me procurar mais!'")
            print("Volte do inicio...tente novamente!")
            comecar_jogo()
            break
    print()
    print("Quando o velho do cajado nota que você está assustado e diz...")
    print()
    sleep(1)
    print()
    input('>>> Aperte enter para continuar...')
    print()
    print(f"{'='*120}")
    print("Não se assuste, tenho algo a mostrar a você!\n"
    "Este é o perfume de Cleópatra, usado por ela à mais de 3 mil anos atrás!\n" 
    "Com ele você poderá ressuscita-la derramando todo esse frasco sobre ela mumificada em seu sarcófago.\n"
    "Para isso precisa ir até esfinge de Gizé, você vai escalar até o topo e colocar este meu cajado \n"
    "dentro do olho deste grande monumento de pedra.")
    print(f"{'='*120}")
    print()
    input('>>> Aperte enter para continuar...')
    print()
    print(nome,"fala... 'O que acontece depois?'")
    print("Velho miterioso diz... “Você resolverá o enigma da esfinge tome muito cuidado, não erre!”")
    sleep(1)
    print()
    input('>>> Aperte enter para continuar...')
    print()
    print(f"{'='*120}")
    print("Velho misterioso fala...")
    print("Depois de tudo que falei você ainda deseja olhar com os seus próprios olhos a Rainha Cleópatra?")
    print(f"{'='*120}")
    sleep(1)
    print()
    input('>>> Aperte enter para continuar...')
    print()
    resposta_3 = input("Responda SIM ou NÃO: ")
    print()
    while True:
        if resposta_3 == "SIM":
            print("Ótimo, você não irá se arrepender você encontrar a mais bela e inteligente rainha \n"
            "que esse mundo já teve.")
            break
        elif resposta_3 == "NÃO":
            print("FIM DE JOGO!")
            print("Uma pena, agora que você sabe meu segredo manterei você preso aqui no porão da biblioteca")
            print("Volte do inicio...tente novamente!")
            comecar_jogo()
            break
    print()
    sleep(1)
    print()
    input('>>> Aperte enter para continuar...')
    print()
    print("Ainda pela manhã, ",nome, "sai correndo ao estúdio de produção entrega todas as anotações, fotos de \n"
    "documentos e livros ao seu chefe Jacó, com isso a produção irá seguir normalmente com o filme.\n" 
    "Agora com o tempo livre, [nome] chega no hotel para se prepara levando tudo precisa (Perfume e cajado) \n"
    "para ir à esfinge na madrugada desta noite.")
    sleep(3)
    print()
    input('>>> Aperte enter para continuar...')
    print()
    print("Ao chegar ao local, por volta das 2h da manhã o arqueólogo começa a escalar a esfinge, ouve alguns \n"
    "barulhos e avista os seguranças do local mas fica muito cauteloso, e continua sua escalada.")
    print()
    sleep(1)
    print()
    input('>>> Aperte enter para continuar...')
    print()
    print(f"Já nos olhos da esfinge, ",nome," empunha o cajado dentro do olho, ao fazer isso escuta-se \n"
    "um som que parece ter saído da esfinge, no mesmo instante, uma parede se abre com uma passagem para entrar \n"
    "na Esfinge de Gizé, porém está fechada e contém alguns manuscritos egípcios. Ao que parece será preciso\n" 
    "traduzir o enigma para entrar no monumento.")
    sleep(2)
    print()
    input('>>> Aperte enter para continuar...')
    print()
    print("Esse é o enigma da esfinge caso você errar irei te amaldiçoar para sempre!")
    print()
    print("QU3 4N1M4L 4ND4 P3L4 M4NH4 5OBR3 QUA7RO P4T4S, 4 T4RD3 5OBR3 DU4S E 4 N01T3 S0BR3 TR3S?")
    print()
    print("[A] - G4T0")
    print("[B] - C4CH0RR0")
    print("[C] - H0M3M")
    print("[D] - P4SS4R0")
    print()
    resposta_4 = input("Digite a alternativa correta! ")
    print()
    while True:
        if resposta_4 == "A":
            print("Reposta errada! UAHMUAUAH")
            print("FIM DE JOGO!")
            print("Volte do inicio...tente novamente!")
            comecar_jogo()
            break
        elif resposta_4 == "B":
            print("Reposta errada! UAHMUAUAH")
            print("Reposta errada! UAHMUAUAH")
            print("FIM DE JOGO!")
            print("Volte do inicio...tente novamente!")
            comecar_jogo()
            break
        elif resposta_4 == "C":
            print("O homem, pois engatinha na infância, anda ereto na idade adulta e necessita de bengala na velhice")
            print("RESPOSTA CERTA! Deixarei você passar!")
            break
        elif resposta_4 == "D":
            print("Reposta errada! UAHMUAUAH")
            print("Reposta errada! UAHMUAUAH")
            print("FIM DE JOGO!")
            print("Volte do inicio...tente novamente!")
            comecar_jogo()
            break
    sleep(2)
    print()
    input('>>> Aperte enter para continuar...')
    print()
    print(nome," consegue entrar na esfinge e já se depara com o sarcófago no meio da sala, iluminada \n"
    "com tochas. Em seguida já retirada do bolso o perfume, empurra a tampa do sarcófago.")
    sleep(1)
    print()
    input('>>> Aperte enter para continuar...')
    print()
    print(f"{'='*100}")
    print(nome," - 'Pelos Deuses egípcios é realmente a múmia de Cleópatra, o velho estava certo! Irei despejar\n"
    "todo frasco nela e esperar o que vai acontecer!'")
    print(f"{'='*100}")
    sleep(1)
    print()
    input('>>> Aperte enter para continuar...')
    print()
    print("Quando a última gota de perfume é derramada sobre ela, a tapa se fecha novamente!")
    print("O lugar começa a tremer e parece que tudo vai desmoronar sobre você as tochas se apagam,\n"
          "mas de repente ouvisse um silêncio absoluto.")
    print("...")
    sleep(1)
    print("...")
    print()
    input('>>> Aperte enter para continuar...')
    print()
    print("Tudo escuro, uma tocha se acende e ao que parece está sendo carregada por alguém ao se aproximar, ela fala...")
    print()
    input('>>> Aperte enter para continuar...')
    print()
    print(f"{'='*100}")
    print("Sempre serei grato daquele que me renasceu, diga o seu nome?")
    sleep(1)
    print("Meu nome é ",nome)
    print("Olá, ",nome," eu sou a Cleópatra a rainha do Egito")
    print(f"{'='*100}")
    print()
    input('>>> Aperte enter para continuar...')
    print()
    print(nome," ainda muito assustado com tudo isso que estava acontecendo, ela se aproxima e o olhar em \n"
    "seus olhos ela nota que você se parece muito com o seu Marido falecido Marco Antônio, mas tenta disfarça\n"
    "esse sentimento.")
    sleep(1)
    print()
    input('>>> Aperte enter para continuar...')
    print()
    print(f"{'='*100}")
    print("“Vamos sair daqui logo antes que os seguranças cheguem, iremos para um lugar seguro onde você possa\n"
    "trocar de roupa, comer alguma coisa!")
    sleep(1)
    print(f"{'='*100}")
    print("Chegando no quarto do hotel, você desce para o andar de baixo onde se encontra o seu chefe,\n"
    "enquanto a Cleópatra se trocava em seu quarto!")
    print("No momento que você iria dizer sobre a verdadeira Cleópatra foi ressuscitada o seu chefe interrompe você e fala...")
    sleep(1)
    print()
    input('>>> Aperte enter para continuar...')
    print()
    print(f"{'='*100}")
    print("Onde você estava? Você soube o que aconteceu com Juliana Paes e Rodrigo Lombardi? Estavam fazendo \n"
    "o último take do filme na cena de ação sofreram um acidente, e as gravações foram paralisadas estão procurando \n"
    "substitutos, porque os vistos do nosso passaporte no Egito já irão se encerrar")
    print(f"{'='*100}")
    sleep(3)
    print("Nesse momento, chega Cleópatra já vestida com roupas dos tempos de hoje, junto com o ela  estava o diretor do filme e ele fala.... ")
    print()
    input('>>> Aperte enter para continuar...')
    print()
    print(f"{'='*100}")
    print("Diretor - 'Encontrei! Encontrei! Meninos acabei de achar a substituta de Juliana Paes que interpretará \n"
    "a Cleópatra para a última cena do filme, mas ainda estou preocupado não achei um substituto para Rodrigo Lombardi'")
    print(f"{'='*100}")
    sleep(1)
    print()
    input('>>> Aperte enter para continuar...')
    print()
    print(f"{'='*100}")
    print("Cleópatra - 'Não fique preocupado, você acaba de achar o meu Marco Antônio será ele, ",nome)
    print("Diretor - Meu Deus! Como eu não tinha notado isso antes {nome} é muito parecido com Marco Antônio, \n"
    "consequentemente é parecido também com Rodrigo Lombardi!")
    print(f"{'='*100}")
    sleep(2)
    print("Diretor - ",nome," Você aceita o papel?")
    print()
    resposta_5 = input("Responda SIM ou NÃO")
    print()
    while True:
        if resposta_5 == "SIM":
            print("Diretor - 'M-A-R-A-V-I-L-H-A ",nome,", se prepare que vocês entram no estúdio amanhã cedo!")
            break
        elif resposta_5 == "NÃO":
            print("FIM DE JOGO!")
            print("Diretor - 'Uma pena, iremos voltar ao Brasil sem a gravar a ultima cena! FIM DE JOGO!'")
            print("Volte do inicio...tente novamente!")
            comecar_jogo()
            break
    sleep(3)
    print()
    input('>>> Aperte enter para continuar...')
    print()
    print("Com as cenas gravadas no dia seguinte o final ficou assim a cidade foi invadida pelos inimigos e \n"
    "Cleópatra e Marco Antônio, estão muito feridos beirando a morte mas se declaram um para o outro antes \n" 
    "de morrer e dão o ultimo beijo deles.")
    print()
    input('>>> Aperte enter para continuar...')
    print()
    sleep(2)
    print(f"{'='*100}")
    print("Cleópatra - ',",nome," hoje estou aqui nesse seu tempo, renascida não por causa dos Deuses, mas graças a você!'")
    print("Cleópatra - 'Meu coração está completamente apaixonado por você, não porque es parecido com Marco Antônio,\n"
            "mas sim pela sua coragem, determinação e amor a civilização egípcia.'")
    print("Cleópatra - 'Vamos ficar juntos, quero aprender com você essa nova cultura desse novo “mundo” que estou \n"
          "vivendo agora, iremos ser muitos felizes!'")
    print(f"{'='*100}")
    sleep(4)
    print()
    input('>>> Aperte enter para continuar...')
    print()
    resposta_6 = input("O que você me diz? Responda SIM ou NÃO: ")
    print()
    while True:
        if resposta_6 == "SIM":
            print("Nunca senti nada que fosse tão especial quanto aquele beijo, vamos comigo voltar ao Brasil!")
            print("Eles voltaram ao Brasil, Cleópatra está totalmente adaptada ao novo 'mundo', ela grávida de gêmios!")
            print("F I M  <3 ")
            break
        elif resposta_6 == "NÃO":
            print("Não posso fazer isso, você não pertence a esse mundo, irei retornar a Esfinge de Gizé onde eu te encontrei!")
            print("Passou anos e nunca",nome," se casou e nem encontrou o amor da sua vida.")
            print("F I M")
            break

from time import sleep
print()
print('{::^120}'.format(""))
print('{:=^120}'.format(" RESILIA ENTERTAINMENT "))
print('{::^120}'.format(""))
print()
print()
sleep(2)
print('{:=^120}'.format("  A relíquia perdida da rainha Cleópatra!  "))
sleep(1)
print()
print("""\n
            _                                                      
            __ -                                                   
        /     __   \                                               
          /   _ -    |                                             
      | '  | (_)  |                        _L/L                    
         |  __  /   /                    _LT/l_L_                  
        \ \  __  /                     _LLl/L_T_lL_                
            -      _T/L              _LT|L/_|__L_|_L_              
                 _Ll/l_L_          _TL|_T/_L_|__T__|_l_            
               _TLl/T_l|_L_      _LL|_Tl/_|__l___L__L_|L_          
             _LT_L/L_|_L_l_L_  _'|_|_|T/_L_l__T _ l__|__|L_        
           _Tl_L|/_|__|_|__T _LlT_|_Ll/_l_ _|__[ ]__|__|_l_L_      
   _ ___ _LT_l_l/|__|__l_T _T_L|_|_|l/___|_ _|__l__|__|__|_T_l_  __
        . ";;:;.;;:;.;;;;_Ll_|__|_l_/__|___l__|__|___l__L_|_l_LL_  
          .  .:::.:::..:::.";;;;:;;:.;.;;;;,;;:,;;;.;:,;;,;::;:".' 
              . ,::.:::.:..:.: ::.::::;..:,:::,::::.::::.:;:.:..   
                 . .:.:::.:::.:::: .::.::. :::.::::..::..:.::. . . 
                   . ::.:.: :. .:::  ::::.::.:::.::...:. .:::. .   
                       .:. ..   . ::.. .: ::. ::::.:: ::::::.   .  
                       .  :.         .. :::.::: ::.::::. ::. .     
                         . .           .:. :.. :::. ::..: :.       
             nn_r   nn_r   .              :  .:::.:: ::..:  .      
            /l(\   /l)\      nn_r          . ::. :. : : ..         
            `'"``  ``"``    /\(\              . . .:. . : .        
                            ' "``                  . :. .          
                                                    .   .          
                                                       .
\n""")
sleep(2)
print("Carregando...")
print()
input('>>> Aperte enter para continuar...')
print()
print("""\n
                     ====================================================
                            A RELÍQUIA PERDIDA DA RAINHA CLEÓPATRA! 
                     ====================================================
                                    ---------------------
                                    | 0 - Iniciar jogo  |
                                    | 1 - Créditos      |
                                    | 2 - Sair          |
                                    ---------------------
    \n""")
menu_inicial = input("Escolha uma opção: ")

while True:
    if menu_inicial == '0':
        comecar_jogo()
        break
    elif menu_inicial == '1':
        print('{::^80}'.format(" Desenvolvido por Demétrio Fragoso "))
        print('{:=^80}'.format(" Turma_VamoAi (Resilia-Ifood) "))
        break
    elif menu_inicial == '2':
        print("Volte a jogar em breve! ")
        break
    else:
        print("Opção inválida!")
        break