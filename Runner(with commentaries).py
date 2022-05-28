import pygame
from sys import exit

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

'''# dentro de uma variável, é possível guardar o tamanho de uma superfície e posteriormente "enchê-la" com uma cor
test_surface = pygame.Surface((100, 200))
test_surface.fill('Red')'''

'''é possível também importar uma imagem por exemplo,
é necessário utilizar o .convert() para facilitar o "entendimento" do pygame ao que está sendo importado'''
sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
'''cria um objeto que acessa o estilo previamente criado e recebe 3 parâmetros:
o texto que será exibido, boolean para filtro anti-aliasing e cor do texto'''
score_surf = test_font.render('My Game', False, (64, 64, 64))
# cria um retângulo para o objeto score posicionado no meio da tela (400 metade de 800 acessado pelo centro do rect)
score_rect = score_surf.get_rect(center=(400, 50))

# para objetos que vão se mover ou receber algum tipo de animação, é recomendado a utilização de .convert_aplha()
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
'''cria uma variável que recebe o objeto previamente importado junto com as medidas de um retângulo
os valores entre parênteses definem qual é a posição na tela daquele ponto do retângulo escolhido'''
snail_rect = snail_surf.get_rect(bottomright=(600, 300))

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
"""para parametrizar os retângulos, podemos acessar os valores de tudas formas:
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
        '''if event.type == pygame.MOUSEMOTION:
            if player_rect.collidepoint(event.pos):
                print('collision')'''

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
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
    screen.blit(score_surf, score_rect)

    # posiciona na tela o objeto snail_surf posição snail_rect (que foi o retângulo previamente criado)
    screen.blit(snail_surf, snail_rect)
    # acessando o eixo X do retângulo para definir sua motimentação na tela
    snail_rect.x -= 4
    # se a posição da direita do retângulo for menor que 0 no eixo X
    if snail_rect.right < 0:
        # a posição esquerda do retângulo no eixo X é definida para 800
        snail_rect.left = 800
    screen.blit(player_surf, player_rect)

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
