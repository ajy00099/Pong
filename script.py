import pygame 
pygame.init()
WIDTH,HEIGHT= 600,400
screen =pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("My pong game")


class Rect:
    def __init__(self,x,y):
        self.x= x
        self.y=y
        self.rect= pygame.Rect(self.x, self.y, 10, 40)
        self.move_up= False
        self.move_down= False

    def draw_rect(self):
        pygame.draw.rect(screen,(122,122,122),self.rect)

    def move(self):
        
        if self.move_up :
            self.rect.y-=5
            if self.rect.centery<=0:
                self.rect.centery=0
        if self.move_down:
            self.rect.y+=5
            if self.rect.centery>=HEIGHT:
                self.rect.centery=HEIGHT

class Ball:
    def __init__(self):
        self.x= 20
        self.y= 10
        self.rect= pygame.Rect(self.x, self.y, 10, 10)
        self.change_position_x=2
        self.change_position_y=2

    def update(self):
        self.rect.x+=self.change_position_x
        self.rect.y+=self.change_position_y
        pygame.draw.rect(screen,(122,255,255),self.rect)
        
        
        if not 0<= self.rect.centery <= HEIGHT:
            self.change_position_y= -self.change_position_y

class MAIN:
    def __init__(self):
        self.rect= Rect(0,200)
        self.ball= Ball()
        self.rect_AI= Rect(WIDTH-10,self.ball.rect.centery+20)
    
    def update(self):
        self.ball.update()
        self.rect.move()
        self.rect_AI.rect.centery=self.ball.rect.centery 

            
        if self.rect.rect.colliderect(self.ball.rect) or self.rect_AI.rect.colliderect(self.ball.rect):
            self.ball.change_position_x=- self.ball.change_position_x
    def draw(self):
        self.rect.draw_rect()
        self.rect_AI.draw_rect()

clock= pygame.time.Clock()
main_game=MAIN()
running= True
while running:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running= False
        
        if event.type== pygame.KEYDOWN:
            if event.key== pygame.K_UP:
                main_game.rect.move_up= True
            elif event.key == pygame.K_DOWN:
                main_game.rect.move_down= True
            
        elif event.type== pygame.KEYUP:
            if event.key== pygame.K_UP:
                main_game.rect.move_up= False
            elif event.key== pygame.K_DOWN:
                main_game.rect.move_down= False
        
        
    clock.tick(60)
    screen.fill((0,0,0))
    main_game.update()
    main_game.draw()
    pygame.display.update()

    
   

pygame.quit()


