import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddles and ball dimensions
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
BALL_SIZE = 10

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

# Paddle class
class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([PADDLE_WIDTH, PADDLE_HEIGHT])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move_up(self):
        if self.rect.y > 0:
            self.rect.y -= 5

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - PADDLE_HEIGHT:
            self.rect.y += 5

# Ball class
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([BALL_SIZE, BALL_SIZE])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
        self.rect.y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
        self.velocity = [random.choice([5, -5]), random.choice([5, -5])]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        # Bounce off top and bottom
        if self.rect.y <= 0 or self.rect.y >= SCREEN_HEIGHT - BALL_SIZE:
            self.velocity[1] = -self.velocity[1]

        # Bounce off paddles
        if pygame.sprite.spritecollide(self, paddles, False):
            self.velocity[0] = -self.velocity[0]

# Game objects
left_paddle = Paddle(30, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
right_paddle = Paddle(SCREEN_WIDTH - 30 - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
ball = Ball()

# Sprite groups
all_sprites = pygame.sprite.Group()
paddles = pygame.sprite.Group()

all_sprites.add(left_paddle)
all_sprites.add(right_paddle)
all_sprites.add(ball)

paddles.add(left_paddle)
paddles.add(right_paddle)

# Score variables
left_score = 0
right_score = 0

# Font for displaying the score
font = pygame.font.Font(None, 74)

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        left_paddle.move_up()
    if keys[pygame.K_s]:
        left_paddle.move_down()
    if keys[pygame.K_UP]:
        right_paddle.move_up()
    if keys[pygame.K_DOWN]:
        right_paddle.move_down()

    all_sprites.update()

    # Check for ball out of bounds
    if ball.rect.x <= 0:
        right_score += 1
        ball.rect.x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
        ball.rect.y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
        ball.velocity = [random.choice([5, -5]), random.choice([5, -5])]
    if ball.rect.x >= SCREEN_WIDTH - BALL_SIZE:
        left_score += 1
        ball.rect.x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
        ball.rect.y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
        ball.velocity = [random.choice([5, -5]), random.choice([5, -5])]

    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Display scores
    left_text = font.render(str(left_score), True, WHITE)
    screen.blit(left_text, (SCREEN_WIDTH // 4, 10))

    right_text = font.render(str(right_score), True, WHITE)
    screen.blit(right_text, (SCREEN_WIDTH * 3 // 4, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
