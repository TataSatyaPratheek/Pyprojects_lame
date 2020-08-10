#part 1, the defining region
import pygame, sys, random

#general set up
pygame.init()
clock = pygame.time.Clock()

#Setting up the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Pong bruh")

#game rectangels
ball = pygame.Rect(screen_width/2 -15, screen_height/2 -15, 30,30)
player = pygame.Rect(screen_width-20,screen_height/2 -70,10,140)
opponent = pygame.Rect(10,screen_height/2 - 70,10,140)

bg_color = pygame.Color('black')
grey = (200,200,200)

ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
player_speed = 0
opponent_speed = 7


def ball_animation():
  global ball_speed_x,ball_speed_y, player_score, opponent_score, score_time
  ball.x += ball_speed_x
  ball.y += ball_speed_y

  if ball.top <=0 or ball.bottom >=screen_height:
    ball_speed_y *=-1
  
  if ball.left <=0:
    player_score +=1
    score_time = pygame.time.get_ticks()
  
  if ball.right >=screen_width:
    opponent_score +=1
    score_time = pygame.time.get_ticks()

  if ball.colliderect(player) or ball.colliderect(opponent):
    ball_speed_x *=-1


def player_animation():
  
  if player.top <= 0:
    player.top = 0
  
  if player.bottom >= screen_height:
    player.bottom = screen_height


def opponent_animation():

  if opponent.top < ball.y:
    opponent.top += opponent_speed

  if opponent.bottom > ball.y:
    opponent.bottom -= opponent_speed

def ball_restart():
  global ball_speed_x, ball_speed_y, score_time
  
  current_time = pygame.time.get_ticks()
  
  ball.center = (screen_width/2,screen_height/2)

  if current_time - score_time < 700:
    number_3 = game_font.render('3', False, grey)
  
  if 700 < current_time - score_time < 1400:
    number_2 = game_font.render('2', False, grey)
  
  if 1400 < current_time - score_time < 2100:
    number_1 = game_font.render('1', False, grey)
  
  if current_time - score_time < 2100:
    ball_speed_x, ball_speed_y = 0,0
  else:
    ball_speed_x = 7 * random.choice((1,-1))
    ball_speed_y = 7 * random.choice((1,-1))
    score_time = None

#Text variables to display the scores
player_score = 0
opponent_score = 0 
game_font = pygame.font.Font('freesansbold.ttf', 32)


#score timer 
score_time = True


#part 2, the execution region
while True:

  #to handle input

  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    if event.type == pygame.KEYDOWN:

      if event.key == pygame.K_DOWN:
        player_speed +=7

      if event.key == pygame.K_UP:
        player_speed -=7
  
    if event.type == pygame.KEYUP:

      if event.key == pygame.K_DOWN:
        player_speed -=7

      if event.key == pygame.K_UP:
        player_speed +=7


  ball_animation()
  player_animation()
  opponent_animation()

  player.y +=player_speed
  
  
  #the drawings 
  screen.fill(bg_color)
  pygame.draw.rect(screen, grey, player)
  pygame.draw.rect(screen, grey, opponent)
  pygame.draw.ellipse(screen, grey, ball)
  pygame.draw.aaline(screen, grey, (screen_width/2,0), (screen_width/2, screen_height))
  
  if score_time:
    ball_restart()

  player_text = game_font.render(f'{player_score}',False, grey)
  screen.blit(player_text,(666,420))

  opponent_text = game_font.render(f'{opponent_score}',False, grey)
  screen.blit(opponent_text,(600,420))
  
  #for updating the window
  pygame.display.flip()
  clock.tick(60)