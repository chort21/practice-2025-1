import pygame
import sys
import os
import random

# Инициализация Pygame
pygame.init()
pygame.mixer.init()

# Константы
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
FPS = 60

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (200, 200, 200)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
BORDO = (128, 0, 32)

# Цвета фона для уровней
LEVEL_BACKGROUNDS = [
    (25, 25, 112),   # Темно-синий (Уровень 1)
    (75, 0, 130),    # Индиго (Уровень 2)
    BORDO            # Бордовый (Уровень 3)
]

# Цвета кнопок уровней
LEVEL_BUTTON_COLORS = [
    (50, 50, 150),   # Уровень 1
    (100, 0, 180),   # Уровень 2
    (150, 0, 50)     # Уровень 3
]

# Настройка экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Арканоид")
clock = pygame.time.Clock()

class GameObject:
    def __init__(self, x, y, width, height, color=None, image_path=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color if color else WHITE
        self.image = None
        
        if image_path:
            try:
                self.image = pygame.image.load(image_path)
                self.image = pygame.transform.scale(self.image, (width, height))
            except:
                self.image = pygame.Surface((width, height))
                self.image.fill(color if color else RED)
    
    def draw(self, surface):
        if self.image:
            surface.blit(self.image, self.rect)
        else:
            pygame.draw.rect(surface, self.color, self.rect)

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, text_color=BLACK, font_size=24):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.font = pygame.font.SysFont('Bahnschrift', font_size)
        self.is_hovered = False
        self.enabled = True
    
    def draw(self, surface):
        if not self.enabled:
            color = GRAY
        else:
            color = self.hover_color if self.is_hovered else self.color
            
        pygame.draw.rect(surface, color, self.rect, border_radius=5)
        pygame.draw.rect(surface, BLACK, self.rect, 2, border_radius=5)
        
        text_surface = self.font.render(self.text, True, self.text_color if self.enabled else GRAY)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
    
    def check_hover(self, pos):
        self.is_hovered = self.rect.collidepoint(pos) and self.enabled
        return self.is_hovered
    
    def is_clicked(self, pos, click):
        return self.rect.collidepoint(pos) and click and self.enabled

class Ball(GameObject):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size, YELLOW, 'ball.png')
        self.reset(x, y)
    
    def reset(self, x, y):
        self.rect.center = (x, y)
        self.direction = pygame.math.Vector2(0, -1)
        self.speed = 5
    
    def update(self):
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed
        
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.direction.x *= -1
        if self.rect.top <= 0:
            self.direction.y *= -1
        
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

class Paddle(GameObject):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, BLUE, 'platform.png')
        self.speed = 8
    
    def update(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

class Brick(GameObject):
    def __init__(self, x, y, width, height, color=RED):
        super().__init__(x, y, width, height, color, 'enemy.png')

class Boss(GameObject):
    def __init__(self, x, y):
        # Используем тот же спрайт, что и для обычных врагов, но в 3 раза больше
        super().__init__(x, y, 120, 120, PURPLE, 'enemy.png')
        self.speed = 3
        self.direction = 1
        self.hits_required = 5
        self.hits_remaining = self.hits_required
    
    def update(self):
        self.rect.x += self.speed * self.direction
        
        if self.rect.right >= SCREEN_WIDTH or self.rect.left <= 0:
            self.direction *= -1

class Game:
    def __init__(self):
        self.current_level = 1
        self.unlocked_levels = 1
        self.level_scores = [0, 0, 0]
        self.high_score = 0
        self.score = 0
        self.state = "menu"  # menu, level_select, game, game_over, boss_fight
        self.boss = None
        
        self.reset_game()
        
        # Создание кнопок
        button_width, button_height = 200, 50
        center_x = SCREEN_WIDTH // 2 - button_width // 2
        
        self.start_button = Button(
            center_x, 250, button_width, button_height,
            "Выбор уровня", GREEN, (100, 255, 100)
        )
        
        self.quit_button = Button(
            center_x, 320, button_width, button_height,
            "Выход", RED, (255, 100, 100)
        )
        
        self.level_buttons = [
            Button(center_x, 200 + i*70, button_width, button_height,
                  f"Уровень {i+1}", 
                  LEVEL_BUTTON_COLORS[i] if i < self.unlocked_levels else GRAY,
                  (min(LEVEL_BUTTON_COLORS[i][0] + 50, 255),
                   min(LEVEL_BUTTON_COLORS[i][1] + 50, 255),
                   min(LEVEL_BUTTON_COLORS[i][2] + 50, 255)),
                  WHITE)
            for i in range(3)
        ]
        
        self.back_button = Button(
            20, 20, 100, 40,
            "Назад", GRAY, (200, 200, 200)
        )
        
        self.restart_button = Button(
            center_x, 400, button_width, button_height,
            "Играть снова", GREEN, (100, 255, 100)
        )
        
        self.menu_button = Button(
            center_x, 470, button_width, button_height,
            "В меню", BLUE, (100, 100, 255)
        )
    
    def reset_game(self):
        self.ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100, 20)
        self.paddle = Paddle(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 30, 100, 15)
        self.bricks = []
        self.score = 0
        self.create_bricks()
        self.boss = None
    
    def create_bricks(self):
        brick_width = 50
        brick_height = 50
        rows = 3 + (self.current_level - 1)
        cols = SCREEN_WIDTH // brick_width
        
        for row in range(rows):
            for col in range(cols):
                if row < 2:
                    color = RED
                elif row < 4:
                    color = GREEN
                else:
                    color = YELLOW
                
                brick = Brick(
                    col * brick_width, 
                    row * brick_height + 50, 
                    brick_width - 2, 
                    brick_height - 2, 
                    color
                )
                self.bricks.append(brick)
    
    def start_boss_fight(self):
        self.boss = Boss(SCREEN_WIDTH // 2 - 60, 100)
        self.state = "boss_fight"
    
    def handle_collisions(self):
        if self.ball.rect.colliderect(self.paddle.rect):
            relative_intersect_x = (self.paddle.rect.centerx - self.ball.rect.centerx) / (self.paddle.rect.width / 2)
            bounce_angle = relative_intersect_x * (5 * 3.14159 / 12)
            
            self.ball.direction = pygame.math.Vector2()
            self.ball.direction.from_polar((1, -bounce_angle * 180 / 3.14159))
            self.ball.direction.y = -abs(self.ball.direction.y)
        
        # Столкновение с кирпичами
        for brick in self.bricks[:]:
            if self.ball.rect.colliderect(brick.rect):
                self.bricks.remove(brick)
                self.score += 10
                self.level_scores[self.current_level-1] += 10
                
                if (self.ball.rect.centerx < brick.rect.left or 
                    self.ball.rect.centerx > brick.rect.right):
                    self.ball.direction.x *= -1
                else:
                    self.ball.direction.y *= -1
                break
        
        # Столкновение с боссом
        if self.boss and self.ball.rect.colliderect(self.boss.rect):
            self.boss.hits_remaining -= 1
            self.score += 10
            self.level_scores[self.current_level-1] += 10
            
            if self.boss.hits_remaining <= 0:
                self.state = "game_over"
                if self.current_level < 3:
                    self.unlocked_levels = max(self.unlocked_levels, self.current_level + 1)
                return
            
            # Изменяем направление мяча
            if (self.ball.rect.centerx < self.boss.rect.left or 
                self.ball.rect.centerx > self.boss.rect.right):
                self.ball.direction.x *= -1
            else:
                self.ball.direction.y *= -1
    
    def update(self):
        if self.state == "game":
            keys = pygame.key.get_pressed()
            self.paddle.update(keys)
            self.ball.update()
            self.handle_collisions()
            
            if self.ball.rect.top > SCREEN_HEIGHT:
                self.state = "game_over"
                self.high_score = max(self.high_score, sum(self.level_scores))
            
            if not self.bricks:
                if self.current_level == 3:
                    self.start_boss_fight()
                else:
                    self.state = "game_over"
                    self.unlocked_levels = max(self.unlocked_levels, self.current_level + 1)
                    self.high_score = max(self.high_score, sum(self.level_scores))
        
        elif self.state == "boss_fight":
            keys = pygame.key.get_pressed()
            self.paddle.update(keys)
            self.ball.update()
            self.boss.update()
            self.handle_collisions()
            
            if self.ball.rect.top > SCREEN_HEIGHT:
                self.state = "game_over"
                self.high_score = max(self.high_score, sum(self.level_scores))
    
    def draw(self, screen):
        if self.state in ["game", "boss_fight"]:
            screen.fill(LEVEL_BACKGROUNDS[self.current_level-1])
        elif self.state == "level_select":
            screen.fill((50, 50, 80))
        else:
            screen.fill(BLACK)
        
        if self.state == "menu":
            title_font = pygame.font.SysFont('Bahnschrift', 64)
            title_text = title_font.render("BONES", True, BORDO)
            title_rect = title_text.get_rect(center=(SCREEN_WIDTH//2, 100))
            screen.blit(title_text, title_rect)
            
            score_font = pygame.font.SysFont('Bahnschrift', 36)
            score_text = score_font.render(f"Всего: {self.high_score}", True, WHITE)
            score_rect = score_text.get_rect(center=(SCREEN_WIDTH//2, 180))
            screen.blit(score_text, score_rect)
            
            levels_text = score_font.render(f"Открыто уровней: {self.unlocked_levels}/3", True, WHITE)
            levels_rect = levels_text.get_rect(center=(SCREEN_WIDTH//2, 220))
            screen.blit(levels_text, levels_rect)
            
            self.start_button.draw(screen)
            self.quit_button.draw(screen)
        
        elif self.state == "level_select":
            title_font = pygame.font.SysFont('Bahnschrift', 48)
            title_text = title_font.render("ВЫБОР УРОВНЯ", True, WHITE)
            title_rect = title_text.get_rect(center=(SCREEN_WIDTH//2, 100))
            screen.blit(title_text, title_rect)
            
            for i, button in enumerate(self.level_buttons):
                button.enabled = (i+1) <= self.unlocked_levels
                if button.enabled:
                    button.color = LEVEL_BUTTON_COLORS[i]
                    button.hover_color = (
                        min(LEVEL_BUTTON_COLORS[i][0] + 50, 255),
                        min(LEVEL_BUTTON_COLORS[i][1] + 50, 255),
                        min(LEVEL_BUTTON_COLORS[i][2] + 50, 255)
                    )
                button.draw(screen)
            
            self.back_button.draw(screen)
        
        elif self.state == "game":
            for brick in self.bricks:
                brick.draw(screen)
            
            self.paddle.draw(screen)
            self.ball.draw(screen)
            
            font = pygame.font.SysFont('Bahnschrift', 24)
            score_text = font.render(f"Очки: {self.score}", True, WHITE)
            screen.blit(score_text, (10, 10))
            
            level_text = font.render(f"Уровень: {self.current_level}", True, WHITE)
            screen.blit(level_text, (SCREEN_WIDTH//2 - level_text.get_width()//2, 10))
            
            high_text = font.render(f"Всего: {self.high_score}", True, WHITE)
            screen.blit(high_text, (SCREEN_WIDTH - high_text.get_width() - 10, 10))
        
        elif self.state == "boss_fight":
            self.paddle.draw(screen)
            self.ball.draw(screen)
            self.boss.draw(screen)
            
            font = pygame.font.SysFont('Bahnschrift', 24)
            score_text = font.render(f"Очки: {self.score}", True, WHITE)
            screen.blit(score_text, (10, 10))
            
            level_text = font.render(f"Уровень: {self.current_level} - БОСС", True, WHITE)
            screen.blit(level_text, (SCREEN_WIDTH//2 - level_text.get_width()//2, 10))
            
            hits_text = font.render(f"Здоровье босса: {self.boss.hits_remaining}", True, WHITE)
            screen.blit(hits_text, (SCREEN_WIDTH//2 - hits_text.get_width()//2, 40))
            
            high_text = font.render(f"Всего: {self.high_score}", True, WHITE)
            screen.blit(high_text, (SCREEN_WIDTH - high_text.get_width() - 10, 10))
        
        elif self.state == "game_over":
            result_font = pygame.font.SysFont('Bahnschrift', 48)
            
            if not self.bricks or (self.boss and self.boss.hits_remaining <= 0):
                result_text = result_font.render("ПОБЕДА!", True, GREEN)
            else:
                result_text = result_font.render("ПОРАЖЕНИЕ", True, RED)
            
            result_rect = result_text.get_rect(center=(SCREEN_WIDTH//2, 150))
            screen.blit(result_text, result_rect)
            
            score_font = pygame.font.SysFont('Bahnschrift', 36)
            score_text = score_font.render(f"Ваш счет: {self.score}", True, WHITE)
            score_rect = score_text.get_rect(center=(SCREEN_WIDTH//2, 220))
            screen.blit(score_text, score_rect)
            
            level_text = score_font.render(f"Уровень: {self.current_level}", True, YELLOW)
            level_rect = level_text.get_rect(center=(SCREEN_WIDTH//2, 260))
            screen.blit(level_text, level_rect)
            
            high_text = score_font.render(f"Всего: {self.high_score}", True, YELLOW)
            high_rect = high_text.get_rect(center=(SCREEN_WIDTH//2, 300))
            screen.blit(high_text, high_rect)
            
            self.restart_button.draw(screen)
            self.menu_button.draw(screen)
    
    def handle_events(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_click = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.state in ["game", "boss_fight"]:
                        self.state = "menu"
                    elif self.state == "level_select":
                        self.state = "menu"
        
        if self.state == "menu":
            self.start_button.check_hover(mouse_pos)
            self.quit_button.check_hover(mouse_pos)
            
            if self.start_button.is_clicked(mouse_pos, mouse_click):
                self.state = "level_select"
                for i, button in enumerate(self.level_buttons):
                    button.enabled = (i+1) <= self.unlocked_levels
                    if button.enabled:
                        button.color = LEVEL_BUTTON_COLORS[i]
                        button.hover_color = (
                            min(LEVEL_BUTTON_COLORS[i][0] + 50, 255),
                            min(LEVEL_BUTTON_COLORS[i][1] + 50, 255),
                            min(LEVEL_BUTTON_COLORS[i][2] + 50, 255)
                        )
            
            if self.quit_button.is_clicked(mouse_pos, mouse_click):
                pygame.quit()
                sys.exit()
        
        elif self.state == "level_select":
            self.back_button.check_hover(mouse_pos)
            
            for i, button in enumerate(self.level_buttons):
                button.check_hover(mouse_pos)
                if button.is_clicked(mouse_pos, mouse_click) and button.enabled:
                    self.current_level = i + 1
                    self.reset_game()
                    self.state = "game"
            
            if self.back_button.is_clicked(mouse_pos, mouse_click):
                self.state = "menu"
        
        elif self.state == "game_over":
            self.restart_button.check_hover(mouse_pos)
            self.menu_button.check_hover(mouse_pos)
            
            if self.restart_button.is_clicked(mouse_pos, mouse_click):
                self.reset_game()
                self.state = "game"
            
            if self.menu_button.is_clicked(mouse_pos, mouse_click):
                self.state = "menu"

def main():
    game = Game()
    try:
        pygame.mixer.music.load('anbermic3!.mp3')  
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)  
    except:
        pass
    while True:
        game.handle_events()
        game.update()
        game.draw(screen)
        
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
