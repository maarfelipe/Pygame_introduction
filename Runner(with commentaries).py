import pygame
from sys import exit


# criando uma função para apresentar o score
def display_score():
    # método .get_ticks() retorna o valor em milissegundos de execução do programa
    current_time = int(pygame.time.get_ticks() / 100) - start_time
    # criando um objeto para receber a variável de tempo, com as configurações de renderização de texto
    score_surf = test_font.render(f'{current_time}', False, (64, 64, 64))
    # criando um rectângulo com o método .get_rect e posicionando 400x50y
    score_rect = score_surf.get_rect(center=(400, 50))
    # posicionando na tela o objeto gerado (score_surf) na posição definida (score_rect)
    screen.blit(score_surf, score_rect)
    return current_time


# comando para iniciar o pygame e todas as suas funções
pygame.init()
# define o display surface, a tela que será apresentada ao usuário (width, height)
screen = pygame.display.set_mode((800, 400))
# define o título apresentado na janela
pygame.display.set_caption('Runner')
# define um objeto clock, utilizado para controle de framerate (é preciso ser "chamado" posteriormente)
clock = pygame.time.Clock()
# define um estilo de font que pode ser importado, o seu tamanho também é definido agora
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
# criando uma varíavel booleana para poder resetar o game quando o player perder
game_active = False
# definindo uma variável para o tempo de jogo
start_time = score = 0

'''# dentro de uma variável, é possível guardar o tamanho de uma superfície e posteriormente "enchê-la" com uma cor
test_surface = pygame.Surface((100, 200))
test_surface.fill('Red')'''

'''é possível também importar uma imagem por exemplo,
é necessário utilizar o .convert() para facilitar o "entendimento" do pygame ao que está sendo importado'''
sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

"""'''cria um objeto que acessa o estilo previamente criado e recebe 3 parâmetros:
o texto que será exibido, boolean para filtro anti-aliasing e cor do texto'''
score_surf = test_font.render('My Game', False, (64, 64, 64))
# cria um retângulo para o objeto score posicionado no meio da tela (400 metade de 800 acessado pelo centro do rect)
score_rect = score_surf.get_rect(center=(400, 50))"""

# para objetos que vão se mover ou receber algum tipo de animação, é recomendado a utilização de .convert_aplha()
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
'''cria uma variável que recebe o objeto previamente importado junto com as medidas de um retângulo
os valores entre parênteses definem qual é a posição na tela daquele ponto do retângulo escolhido'''
snail_rect = snail_surf.get_rect(bottomright=(600, 300))

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
"""para parametrizar os retângulos, podemos acessar os valores das seguintes formas:
    tuplas(x, y):
        podemos acessar cada valor separado em nove possíveis posições:
            topleft         midtop          topright
            midleft         center          midright
            bottomleft      midbottoom      bottomright
    valores individuais:
        pode-se acessar os valores de um lado inteiro individualmente:
                            top
            left    centerx OU centery  right
                            bottom"""
player_rect = player_surf.get_rect(midbottom=(80, 300))
# definindo um objeto gravidade, que deverá funcionar para manter o player no chão
player_gravity = 0

'''# criando um objeto que ficará na tela de início/reset
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
# utilizando o método .transform.scale no objeto criado para alterar o seu tamanho
player_stand = pygame.transform.scale(player_stand, (200, 400))
# criando o retângulo do objeto através do método .get_rect
player_stand_rect = player_stand.get_rect(center=(400, 200))'''

'''# criando um objeto a partir do método .load e alterando seu tamanho com o método .transform.scale
player_stand = pygame.transform.scale(pygame.image.load('graphics/Player/player_stand.png').convert_alpha(), (200, 300))
player_stand_rect = player_stand.get_rect(center=(400, 200))'''

'''# criando um objeto que ficará na tela de início/reset
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
# utilizando o método .transform.scale2x no objeto criado para alterar o seu tamanho
player_stand = pygame.transform.scale2x(player_stand)
# criando o retângulo do objeto através do método .get_rect
player_stand_rect = player_stand.get_rect(center=(400, 200))'''

# criando um objeto que ficará na tela de início/reset
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
# utilizando o método .transform.rotozoom no objeto criado para alterar o seu tamanho
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)  # o segundo valor altera o ângulo do objeto
# criando o retângulo do objeto através do método .get_rect
player_stand_rect = player_stand.get_rect(center=(400, 200))

game_name = test_font.render('Pixel Runner', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center=(400, 80))

game_message = test_font.render('Pressione espaco para correr', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center=(400, 330))

# o loop é criado para que a tela e os eventos permaneçam acontecendo, senão, tudo iria ser executado somente uma vez
while True:
    for event in pygame.event.get():
        # loop for criado para acessar cada evento de forma independente
        if event.type == pygame.QUIT:
            '''pygame.quit() é literalmente o oposto de pygame.init()
            permitindo que tudo seja encerrado dá forma correta sem apresentar nenhum tipo de erro'''
            pygame.quit()
            # importado do sys, exit() encerra e fecha a janela da forma correta
            exit()

        '''if event.type == pygame.MOUSEMOTION: # .MOUSEMOTION acessa a movimentação do mouse
            # print(event.pos) # mostra no console os valores (x,y) da posição do mouse'''
        '''if event.type == pygame.MOUSEBUTTONDOWN: # .MOUSEBUTTONDOWN é o evento quando um botão do mouse é pressionado
            print('mouse down')'''
        '''if event.type == pygame.MOUSEBUTTONUP: # .MOUSEBUTTONUP é o evento quando o botão do mouse é solto
            print('mouse up')'''

        if game_active:
            """# criamos um if que reconhece o evento .MOUSEBUTTONDOWN
            if event.type == pygame.MOUSEBUTTONDOWN:
                '''depois outro if que dentro do evento .MOUSEBUTTONDOWN reconhece a colisão entre a posição do mouse e o
                retângulo do player, AND, verifica se o player está na posição 300, ou seja, no floor, permitindo assim
                somente um pulo'''
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20
                    
            # criamos um if que reconhece um tipo de evento, chamado .KEYDOWN
            if event.type == pygame.KEYDOWN:
                '''depois outro if que dentro do evento .KEYDOWN reconhece a tecla de espaço, que será utilizada para 
                efetuar os pulos do jogador, AND, verifica se o player está na posição 300, ou seja, no floor, 
                permitindo assim somente um pulo'''
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20"""

            # juntando os dois últimos ifs para otimização de código
            if player_rect.bottom >= 300:
                if event.type == pygame.MOUSEBUTTONDOWN and player_rect.collidepoint(event.pos) \
                        or event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks() / 100)

    if game_active:
        '''# aqui estamos acessando a variável da superfície vermelha e escolhendo qual a sua posição
        screen.blit(test_surface, (0, 0))'''
        # acessando o objeto sky_surface que foi previamente carregado fora do loop
        screen.blit(sky_surface, (0, 0))
        '''os valores entre parênteses definem a posição da imagem na tela criada,
        a ordem de chamada do screen.blit influencia na posição das imagens (o que fica na frente do que)'''
        screen.blit(ground_surface, (0, 300))
        '''o método .draw neste caso foi usado para desenhar um rect que recebe três parâmetros:
            ele ficará sobre na tela
            sua cor de fundo 
            e por último, será posicionado junto com score_rect
        é possível ainda modificar a margem ou o border-radius do rect desenhado colocando mais parâmetros'''
        '''pygame.draw.rect(screen, '#c0e8ec', score_rect)
        pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        screen.blit(score_surf, score_rect)'''
        # chamando a função para apresentar o score
        score = display_score()

        # posiciona na tela o objeto snail_surf posição snail_rect (que foi o retângulo previamente criado)
        screen.blit(snail_surf, snail_rect)
        # acessando o eixo X do retângulo para definir sua motimentação na tela
        snail_rect.x -= 4
        # se a posição da direita do retângulo for menor que 0 no eixo X
        if snail_rect.right < 0:
            # a posição esquerda do retângulo no eixo X é definida para 800
            snail_rect.left = 800

        '''como na vida real, a gravidade nos puxa para baixo, portanto a mecânica utilizada segue este padrão, em todas
        as interações do loop a gravidade tenta puxar o player para baixo, quando ESPAÇO ou MOUSE são pressionados, ela
        recebe um valor negativo (-20), fazendo o player pular'''
        player_gravity += 1
        player_rect.y += player_gravity
        '''o player não cai infinitamente pois criamos um floor utilizando a posição 300 na tela, que é a mesma posição do
        ground_surface'''
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)

        score_message = test_font.render(f'Score: {score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center=(400, 330))
        screen.blit(game_name, game_name_rect)
        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)

    '''keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        print('jump')'''

    '''método .colliderect() testa se há colisões entre retângulos: 0 - false // 1 - true
    if player_rect.colliderect(snail_rect):'''

    """# variável criada para receber a posição do mouse através do método mouse.get_pos()
    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):
        '''print('collision') # teste de if
        método mouse.get_pressed() testa cada botão do mouse, retornando valor booleano para cada um'''
        print(pygame.mouse.get_pressed())"""

    '''este comando atualiza frame por frame o que está acontecendo dentro do loop,
    é ele que mostra para o usuário a animação acontecendo'''
    pygame.display.update()
    '''o valor dentro dos parênteses indica quantas repetições por segundo acontecerão
    no caso, 60fps ... o loop vai se repetir 60 vezes por segundo'''
    clock.tick(60)
