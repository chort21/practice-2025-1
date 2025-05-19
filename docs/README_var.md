
# Документация: вариативная часть задания

## Отчет по проектной практике: Создание игры "Арканоид" на Python с использованием PyGame

## Введение

В рамках проектной практики была выбрана тема "Создание игры" из списка проектов codecrafters-io/build-your-own-x. С помощью библиотеки PyGame языка Python был реализован классический арканоид - игра, где игрок управляет платформой, отбивая мяч и разрушая кирпичи.

## 1. Исследование предметной области

### 1.1 Анализ существующих решений

Перед началом разработки было изучено несколько реализаций арканоида на Python. Основные выводы:

-   достаточно большой объем реализаций использует Pygame как основной фреймворк;
    
-   базовая механика включает: управление платформой, движение мяча, разрушение блоков;
    
-   продвинутые версии включают систему уровней, бонусы, боссов;
    

### 1.2 Выбор стека технологий

Для реализации был выбран следующий стек:

-   **Python 3.13+**  - основной язык программирования;
    
-   **PyGame**  - библиотека для создания игр;
    
-   **Git**  - система контроля версий;
    
-   **Markdown**  - для документации.
    

## 2. Техническое руководство по созданию игры

### 2.1 Настройка окружения

1.  Установите Python с официального сайта;
    
2.  Установите PyGame.

### 2.2 Основные компоненты

#### 2.2.1 Инициализация Pygame

```python
import pygame
pygame.init()
screen = pygame.display.set_mode((500, 600))
```
#### 2.2.2 Игровые объекты

Игра состоит из нескольких классов:

-   GameObject  - базовый класс для всех объектов;
    
-   Ball  - мяч;
    
-   Paddle  - платформа игрока;
    
-   Brick  - кирпичи;
    
-   Boss  - босс (финальный уровень).
    

#### 2.2.3 Главный игровой цикл

```python
while True:
    game.handle_events()
    game.update()
    game.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
```
### 2.3 Полный код игры:

### 1. Инициализация и константы

```python
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
```
**Разбор:**

-   импортируются необходимые библиотеки:  pygame  для графики и звука,  sys  для выхода из игры,  os  для работы с файлами,  random  для случайных значений (хотя в текущей версии не используется);
    
-   инициализируются системы Pygame и микшера для звука;
    
-   задаются константы:
    
    -   размеры экрана (500x600);
        
    -   частота кадров (60 FPS);
        
    -   цвета в формате RGB для использования в игре.
        

### 2. Настройка уровней

```python
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
```
**Разбор:**

-   определяются цветовые схемы для разных уровней:
    
    -   LEVEL_BACKGROUNDS  - фоны для каждого из 3 уровней;
        
    -   LEVEL_BUTTON_COLORS  - цвета кнопок выбора уровней в меню;
        
-   создается игровое окно с заданными размерами и заголовком "Арканоид";
    
-   инициализируется объект  clock  для контроля FPS.
    

### 3. Базовый класс GameObject

```python
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
```
**Разбор:**

-   базовый класс для всех игровых объектов;
    
-   принимает параметры:
    
    -   позиция (x, y);
        
    -   размеры (width, height);
        
    -   цвет (по умолчанию белый);
        
    -   путь к изображению (опционально);
        
-   создает прямоугольник (pygame.Rect) для коллизий и отрисовки;
    
-   поддерживает как цветную заливку, так и спрайты;
    
-   метод  draw  отрисовывает объект на переданной поверхности.
    

### 4. Класс Button

```python
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
```
**Разбор:**

-   класс для создания интерактивных кнопок;
    
-   параметры:
    
    -   позиция, размеры;
        
    -   текст на кнопке;
        
    -   основной цвет и цвет при наведении;
        
    -   цвет текста и размер шрифта;
        
-   функциональность:
    
    -   draw  - отрисовывает кнопку с учетом состояния (наведение, активность);
        
    -   check_hover  - проверяет, находится ли курсор над кнопкой;
        
    -   is_clicked  - проверяет, была ли кнопка нажата.
        

### 5. Класс Ball (мяч)

```python
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
```
**Разбор:**

-   наследуется от  GameObject;
    
-   инициализируется с изображением 'ball.png' или желтым цветом;
    
-   методы:
    
    -   reset  - возвращает мяч в начальное положение;
        
    -   update  - обновляет позицию мяча, обрабатывает отскоки от стен;
        
-   использует  pygame.math.Vector2  для хранения направления движения.
    

### 6. Класс Paddle (платформа)

```python
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
```
**Разбор:**

-   наследуется от  GameObject;
    
-   управляется клавишами стрелок или A/D;
    
-   метод  update:
    
    -   обрабатывает ввод с клавиатуры;
        
    -   ограничивает движение в пределах экрана;
        
-   имеет фиксированную скорость движения.
    

### 7. Классы Brick и Boss

```python
class Brick(GameObject):
    def __init__(self, x, y, width, height, color=RED):
        super().__init__(x, y, width, height, color, 'enemy.png')

class Boss(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, 120, 120, PURPLE, 'enemy.png')
        self.speed = 3
        self.direction = 1
        self.hits_required = 5
        self.hits_remaining = self.hits_required
    
    def update(self):
        self.rect.x += self.speed * self.direction
        
        if self.rect.right >= SCREEN_WIDTH or self.rect.left <= 0:
            self.direction *= -1
```
**Разбор:**

-  Brick - простой кирпич, наследующий от GameObject;
    
-  Boss - особый игровой объект:
    
    -   большего размера (120x120);
        
    -   двигается горизонтально, меняя направление у краев;
        
    -   требует 5 попаданий для уничтожения;
        
    -   отслеживает оставшееся здоровье (hits_remaining).
        

### 8. Основной класс Game

```python
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
        
        self.start_button = Button(center_x, 250, button_width, button_height,
            "Выбор уровня", GREEN, (100, 255, 100))
        
        self.quit_button = Button(center_x, 320, button_width, button_height,
            "Выход", RED, (255, 100, 100))
        
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
        
        self.back_button = Button(20, 20, 100, 40, "Назад", GRAY, (200, 200, 200))
        self.restart_button = Button(center_x, 400, button_width, button_height,
            "Играть снова", GREEN, (100, 255, 100))
        self.menu_button = Button(center_x, 470, button_width, button_height,
            "В меню", BLUE, (100, 100, 255))
```
**Разбор:**

-   главный класс, управляющий состоянием игры;
    
-   содержит:
    
    -   текущий уровень и открытые уровни;
        
    -   систему очков (общий счет и по уровням);
        
    -   состояние игры (меню, игра и т.д.);
        
    -   все игровые объекты (мяч, платформа, кирпичи, босс);
        
    -   кнопки интерфейса.
        

### 9. Методы класса Game

### 9.1 Инициализация и сброс игры

```python
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
```
**Разбор:**

-   reset_game  - сбрасывает состояние игры:
    
    -   создает новый мяч и платформу;
        
    -   очищает кирпичи и счет уровня.
        
-   create_bricks  - генерирует кирпичи для текущего уровня:
    
    -   количество рядов увеличивается с уровнем;
        
    -   разные цвета кирпичей в зависимости от ряда.
        

### 9.2 Обработка столкновений

```python
def handle_collisions(self):
    # Столкновение с платформой
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
        
        if (self.ball.rect.centerx < self.boss.rect.left or 
            self.ball.rect.centerx > self.boss.rect.right):
            self.ball.direction.x *= -1
        else:
            self.ball.direction.y *= -1
```
**Разбор:**

-   обрабатывает три типа столкновений:
    
    -  с платформой - рассчитывает угол отскока в зависимости от точки попадания;
        
    -  с кирпичами - удаляет кирпич, добавляет очки, меняет направление мяча;
        
    - с боссом - уменьшает здоровье босса, обрабатывает победу.
        

### 9.3 Основной игровой цикл

```python
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
```
**Разбор:**

-   обновляет состояние игры в зависимости от текущего режима:
    
    -   в обычной игре ("game"):
        
        -   обновляет платформу и мяч;
            
        -   проверяет столкновения;
            
        -   обрабатывает проигрыш (мяч ушел за экран);
            
        -   переход к боссу на 3 уровне.
            
    -   в режиме босса ("boss_fight"):
        
        -   добавляет обновление босса;
            
        -   проверяет победу/поражение.
            

### 10. Отрисовка игры

```python
def draw(self, screen):
    if self.state in ["game", "boss_fight"]:
        screen.fill(LEVEL_BACKGROUNDS[self.current_level-1])
    elif self.state == "level_select":
        screen.fill((50, 50, 80))
    else:
        screen.fill(BLACK)
    
    if self.state == "menu":
        # Отрисовка меню
        title_font = pygame.font.SysFont('Bahnschrift', 64)
        title_text = title_font.render("BONES", True, BORDO)
        screen.blit(title_text, (SCREEN_WIDTH//2 - title_text.get_width()//2, 100))
        
        score_font = pygame.font.SysFont('Bahnschrift', 36)
        score_text = score_font.render(f"Всего: {self.high_score}", True, WHITE)
        screen.blit(score_text, (SCREEN_WIDTH//2 - score_text.get_width()//2, 180))
        
        self.start_button.draw(screen)
        self.quit_button.draw(screen)
    
    elif self.state == "game":
        # Отрисовка игрового уровня
        for brick in self.bricks:
            brick.draw(screen)
        
        self.paddle.draw(screen)
        self.ball.draw(screen)
        
        # Отрисовка HUD (очки, уровень)
        font = pygame.font.SysFont('Bahnschrift', 24)
        screen.blit(font.render(f"Очки: {self.score}", True, WHITE), (10, 10))
        screen.blit(font.render(f"Уровень: {self.current_level}", True, WHITE), 
                   (SCREEN_WIDTH//2 - font.size(f"Уровень: {self.current_level}")[0]//2, 10))
    
    # ... (аналогичные блоки для других состояний)
```
**Разбор:**

-   в зависимости от состояния игры рисуется:
    
    -   меню с кнопками и статистикой;
        
    -   игровое поле с кирпичами, платформой и мячом;
        
    -   экран босса с индикатором здоровья;
        
    -   экран окончания игры (победа/поражение);
        
-   используются разные фоны для разных состояний;
    
-   интерфейс включает информацию об очках, уровне и рекорде.
    

### 11. Обработка событий

```python
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
    
    # Обработка кликов по кнопкам в разных состояниях
    if self.state == "menu":
        self.start_button.check_hover(mouse_pos)
        self.quit_button.check_hover(mouse_pos)
        
        if self.start_button.is_clicked(mouse_pos, mouse_click):
            self.state = "level_select"
        
        if self.quit_button.is_clicked(mouse_pos, mouse_click):
            pygame.quit()
            sys.exit()
    
    # ... (аналогичная обработка для других состояний)
```
**Разбор:**

-   обрабатывает:
    
    -   закрытие окна;
        
    -   нажатия мыши (для кнопок);
        
    -   клавишу ESC для возврата в меню.
        
-   в зависимости от состояния игры проверяет клики по соответствующим кнопкам.
    

### 12. Главная функция

```python
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
```
**Разбор:**

-   создает экземпляр игры;
    
-   пытается загрузить фоновую музыку;
    
-   запускает главный игровой цикл:
    
    -  обработка событий;
        
    -  обновление состояния игры;
        
    -  отрисовка;
        
    -  обновление экрана;
        
    -  контроль FPS.
        

**Итог**
Код представляет собой полноценную игру "Арканоид" с:

-   тремя уровнями сложности;
    
-   системой подсчета очков;
    
-   боссом на последнем уровне;
    
-   полированным интерфейсом;
    
-   обработкой всех основных игровых ситуаций.
    




## 3. Архитектура проекта
Архитектура построена вокруг главного класса  Game, который управляет состоянием и содержит все игровые объекты. Код хорошо структурирован и следует принципам ООП.
### 3.1 Диаграмма классов
Представлена в файле classes.

### 3.2 Схема состояний игры
Представлена в файле states.
## 4. Управление в игре

-   стрелки влево/вправо  или  A/D - движение платформы;
    
-   ESC - выход в меню;
    
-   мышь - взаимодействие с меню.
    
## 5. Заключение

В результате проектной практики была создана полноценная игра "Арканоид" с системой уровней, боссом и сохранением результатов. Проект демонстрирует применение принципов ООП, работу с графикой и обработку пользовательского ввода в Pygame.

Видео с демонстрацией прототипа приложено в данную директорию.
