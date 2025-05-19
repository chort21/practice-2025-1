# Документация: базовая часть задания
## Создание статического веб-сайта с помощью HTML/CSS
### Введение
Необходимо создать сайт о проекте Shiver - видеоигре в сеттинге киберпанка, поэтому общий стиль сайта выполнен в темных холодных тонах с контрастным оранжевым цветом (он отсылает нас к сюжетно важному веществу оранжевого цвета). Таким образом, сайт будет подчеркивать стилистику игры. Планируется 5 страниц - Главная, Об игре, О проекте, Команда, Ресурсы. 

Основной стиль и общие элементы в соответствии требованиями оформляются так: 
```
:root {
  --bg-dark: #0a0e17;       /* Основной тёмно-синий фон */
  --bg-darker: #05080f;     /* Ещё более тёмный фон для контраста */
  --accent-blue: #00c8ff;   /* Голубой акцент (используется для границ, hover-эффектов) */
  --accent-orange: #ffb347; /* Оранжевый акцент (кнопки, активные элементы) */
  --text-light: #e0e0e0;    /* Цвет основного текста */
  --content-padding: 0 10%; /* Отступы по бокам для контента */
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box; /* Упрощает работу с padding и margin */
  font-family: 'Exo 2', sans-serif; /* Основной шрифт */
}

body {
  background-color: var(--bg-darker);
  color: var(--text-light);
  line-height: 1.6; /* Улучшает читаемость текста */
}
```
Стиль хедера:
```
header {
  background-color: var(--bg-dark);
  padding: 1rem 10%; /* Отступы 1rem сверху/снизу, 10% по бокам */
  display: flex;
  justify-content: space-between; /* Лого слева, навигация справа */
  align-items: center;
  border-bottom: 1px solid var(--accent-blue); /* Подчёркивание */
}

.logo img {
  height: 50px; /* Фиксированная высота логотипа */
}

nav ul {
  display: flex;
  list-style: none;
  gap: 20px; /* Расстояние между пунктами меню */
}

nav a {
  color: var(--text-light);
  text-transform: uppercase; /* Все буквы заглавные */
  letter-spacing: 1px; /* Разряженный текст */
  transition: color 0.3s; /* Плавное изменение цвета */
}

nav a:hover, nav a.active {
  color: var(--accent-orange); /* Подсветка активной/наведённой ссылки */
}
```
Стиль футера:
```
footer {
  background-color: var(--bg-dark);
  padding: 1.5rem;
  text-align: center;
  border-top: 1px solid var(--accent-blue); /* Граница как в хедере */
}
```

## 1.Главная страница (index.html)

### HTML-структура
```html
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Shiver — Главная</title>
  <link rel="stylesheet" href="styles.css">
  <link href="https://fonts.googleapis.com/css2?family=Exo+2:wght@400;600&display=swap" rel="stylesheet">
</head>
<body>
  <header>...</header>

  <main class="main-content">
    <!-- Герой-секция -->
    <section class="hero">
      <img src="art.png" alt="Концепт-арт Shiver">
      <div class="hero-logo">
        <img src="logo.png" alt="Логотип Shiver">
      </div>
    </section>

    <!-- Заголовок и описание -->
    <section>
      <h1>Встречайте Shiver!</h1>
      <p>Уникальная 2D игра с головоломками в сеттинге фрост-киберпанка...</p>
    </section>

    <!-- Информационные плашки -->
    <section class="info-plate left-aligned">
      <div class="text-content">
        <h2>Об игре</h2>
        <p>Погрузитесь в атмосферу ледяного киберпанка...</p>
        <a href="about.html" class="btn">Узнать больше</a>
      </div>
      <div class="image-content">
        <img src="screen2.png" alt="Геймплей">
      </div>
    </section>

    <!-- Ещё 3 аналогичные плашки -->
    ...
  </main>

  <footer>
    <p>2025 Shiver. МосПолитех.</p>
  </footer>
</body>
</html>

```
### Уникальные стили для главной страницы
**Герой-секция (Hero Section):**
```css
.hero {
  position: relative; /* Для абсолютного позиционирования логотипа */
  margin-bottom: 2rem;
}

.hero img {
  width: 100%;
  max-height: 500px;
  object-fit: cover; /* Обрезает изображение, сохраняя пропорции */
}

.hero-logo {
  position: absolute;
  top: 15%;
  left: 5%;
  max-width: 450px; /* Ограничение размера лого */
}
```
**Эффекты:**
- Фоновое изображение на всю ширину.
- Логотип поверх изображения с точным позиционированием.

**Информационные плашки**
```css
.info-plate {
  display: flex;
  background: rgba(40, 45, 60, 0.6); /* Полупрозрачный фон */
  border-radius: 8px;
  padding: 2rem;
  margin: 2rem 0;
  align-items: center;
  border-left: 3px solid var(--accent-orange); /* Акцентная полоса */
}

.text-content {
  flex: 1;
  padding: 0 2rem;
}

.image-content img {
  width: 100%;
  height: auto;
  border-radius: 5px;
}

.btn {
  background-color: var(--accent-orange);
  color: var(--bg-dark);
  padding: 0.8rem 1.5rem;
  border-radius: 3px;
  transition: all 0.3s;
}

.btn:hover {
  background-color: var(--accent-blue);
  transform: translateY(-2px); /* Эффект "подпрыгивания" */
}
```
**Особенности:**
- Гибкая структура (текст + изображение).
- Интерактивные кнопки с анимацией.


## **2. Страница "Об игре" (`about.html`)**

### HTML-структура

```html
<!DOCTYPE html>
<html lang="ru">
<head>
  <!-- Стили и шрифты как на главной -->
</head>
<body>
  <header>...</header>

  <main class="main-content">
    <section class="about-section">
      <h1>Об игре</h1>
      
      <!-- Секция "Сеттинг" -->
      <h2>Сеттинг</h2>
      <div class="about-text clearfix">
        <p>Shiver - это атмосферная 2D игра...</p>
      </div>

      <!-- Секция "История мира" с парными изображениями -->
      <h2>История мира</h2>
      <div class="about-text">
        <div class="image-pair">
          <img src="ref.png" alt="Концепт">
          <img src="ref2.png" alt="Концепт">
        </div>
        <p>Солнце погасло, вместе с ним пропала луна...</p>
      </div>

      <!-- Секция "Особенности игры" -->
      <h2>Особенности игры</h2>
      <div class="about-text">
        <p>- уникальная история и сеттинг;</p>
        <p>- интересные головоломки;</p>
      </div>

      <!-- Галерея скриншотов -->
      <h2>Скриншоты</h2>
      <div class="about-text">
        <div class="image-pair">
          <img src="screen1.png" alt="Геймплей">
          <img src="screen3.png" alt="Геймплей">
        </div>
        <div class="image-pair">
          <img src="screen4.png" alt="Геймплей">
          <img src="screen2.png" alt="Геймплей">
        </div>
      </div>
    </section>
  </main>
  <footer>...</footer>
</body>
</html>
```


### **Уникальные стили для страницы**

**Текстовые блоки и отступы**

```css
.about-section {
  margin-bottom: 3rem; /* Отступ снизу секции */
}

.about-text {
  margin-bottom: 2rem;
  text-align: justify; /* Выравнивание по ширине */
}

h2 {
  font-size: 1.8rem;
  color: var(--accent-orange);
  margin: 2rem 0 1rem; /* Отступы: сверху 2rem, снизу 1rem */
}
```
**Зачем:**

-   Чёткое разделение секций.
    
-   Текст выглядит аккуратнее с выравниванием по ширине.
    



**Парные изображения (image-pair):**

```css
.image-pair {
  display: flex;
  justify-content: space-between;
  margin: 2rem 0;
  gap: 1.5rem; /* Расстояние между изображениями */
}

.image-pair img {
  width: 48%; /* Делает изображения одинаковой ширины */
  border-radius: 5px;
  object-fit: cover;
  box-shadow: 0 0 10px rgba(0, 200, 255, 0.2); /* Лёгкое свечение */
}
```
**Эффекты:**

-   Изображения всегда равны по ширине.
    
-   Тень подчёркивает технологичный стиль игры.
    

----------

#### **Обтекание изображений (float):**

```css
.image-float {
  max-width: 45%;
  margin: 1rem;
  border-radius: 5px;
  box-shadow: 0 0 15px rgba(0, 200, 255, 0.2);
}

.image-float.left {
  float: left; /* Обтекание справа */
  margin-left: 0;
}

.image-float.right {
  float: right; /* Обтекание слева */
  margin-right: 0;
}

.clearfix::after {
  content: "";
  display: table;
  clear: both; /* Отмена обтекания */
}
```


**Почему важно:**

-   Позволяет гармонично вписывать изображения в текст.
    
-   clearfix  предотвращает выпадение элементов.

## 3. Страница "О проекте" (`project.html`)

### HTML-структура

```html
<!DOCTYPE html>
<html lang="ru">
<head>
  <!-- Стили и шрифты (аналогично другим страницам) -->
</head>
<body>
  <header>...</header>

  <main class="main-content">
    <section class="project-section">
      <h1>О проекте</h1>

      <!-- Блок руководителя -->
      <h2>Информация</h2>
      <div class="project-leader">
        <div>
          <img src="marat.png" alt="Руководитель" class="leader-photo">
        </div>
        <div class="leader-info">
          <span class="leader-name">Юзбеков Марат Ахмедович</span>
          <span class="leader-position">Куратор проекта, кандидат наук</span>
          <p>Проект Shiver разрабатывается студентами МосПолитеха...</p>
        </div>
      </div>

      <!-- Цели и задачи -->
      <h2>Цель и задачи проекта</h2>
      <p>Цель - создание качественного игрового продукта...</p>
      <p>Задачи:</p>
      <p>- разработка полной концепции игры до 1 марта;</p>
      <p>- создание MVP проекта до 22 марта;</p>

      <!-- Таймлайн этапов -->
      <h2>Этапы работы над проектом</h2>
      <div class="project-timeline">
        <div class="project-phase">
          <h3>1. Подготовительный этап</h3>
          <p>Февраль 2025 - разработка концепции...</p>
        </div>
        <!-- Ещё 4 аналогичных этапа -->
      </div>

      <!-- Диаграмма Ганта -->
      <h2>Диаграмма Ганта</h2>
      <p>Подробный хронологический план работы:</p>
      <img src="gant.png" alt="Диаграмма Ганта" class="gantt-chart">
    </section>
  </main>

  <footer>...</footer>
</body>
</html>```
```
### Уникальные стили для страницы

**Блок руководителя**

```css
.project-leader {
  display: flex;
  gap: 2rem;
  margin: 2rem 0;
  align-items: flex-start; /* Выравнивание по верхнему краю */
}

.leader-photo {
  width: 200px;
  height: 200px;
  border-radius: 50%; /* Круглое фото */
  border: 3px solid var(--accent-orange);
  box-shadow: 0 0 10px rgba(255, 179, 71, 0.3); /* Свечение */
  object-fit: cover; /* Изображение заполняет круг */
}

.leader-info {
  flex: 1; /* Занимает всё доступное пространство */
}

.leader-name {
  font-size: 1.5rem;
  color: var(--accent-blue);
  margin-bottom: 0.5rem;
}

.leader-position {
  font-style: italic;
  color: var(--text-light);
  display: block; /* Отдельная строка */
  margin-bottom: 1rem;
}
```
**Зачем:**

-   Круглое фото с оранжевой рамкой — визуальный акцент.
    
-   Гибкое расположение (текст адаптируется под ширину фото).
    

**Таймлайн этапов**

```css
.project-timeline {
  margin: 3rem 0;
}

.project-phase {
  margin-bottom: 2rem;
  padding-bottom: 1.5rem;
  border-bottom: 1px dashed var(--accent-blue); /* Пунктирная граница */
}

.project-phase h3 {
  color: var(--accent-orange);
  margin-bottom: 0.5rem;
}
```
**Эффекты:**

-   Пунктирные разделители между этапами.
    
-   Оранжевые заголовки для выделения каждого этапа.
    

**Диаграмма Ганта**

```css
.gantt-chart {
  width: 100%;
  margin-top: 2rem;
  border-radius: 5px;
  box-shadow: 0 0 20px rgba(0, 200, 255, 0.1); /* Лёгкая тень */
}
```
**Важно:**

-   Изображение растягивается на всю ширину контейнера.

-   Закруглённые углы и тень для интеграции в общий стиль.

## **4. Страница "Команда" (`team.html`)**

### HTML-структура

```html
<!DOCTYPE html>
<html lang="ru">
<head>
  <!-- Стили и шрифты (как на других страницах) -->
</head>
<body>
  <header>...</header>

  <main class="main-content">
    <section class="team-section">
      <h1>Наша команда</h1>
      <p>15 талантливых студентов, создающих игру Shiver...</p>

      <!-- Секция "Руководство" -->
      <div class="team-category">
        <h2>Руководство</h2>
        <div class="team-grid">
          <!-- Карточка участника -->
          <div class="team-card">
            <img src="авы/vera.png" alt="Нагайцева Вера" class="team-photo">
            <div class="team-info">
              <div class="team-name">Нагайцева Вера</div>
              <div class="team-role">Тимлид, автор идеи</div>
            </div>
          </div>
          <!-- Ещё одна карточка -->
        </div>
      </div>

      <!-- Аналогичные секции для других ролей: 
           "Программирование", "Арт и дизайн" и т.д. -->
    </section>
  </main>

  <footer>...</footer>
</body>
</html>
```


### Уникальные стили для страницы

 **Грид-сетка для карточек**

```css
.team-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 1.5rem; /* Расстояние между карточками */
  margin-bottom: 2rem;
}
```
**Как это работает**:

-   `auto-fill`  автоматически подбирает количество колонок.
    
-   `minmax(350px, 1fr)`  задаёт минимальную ширину карточки в  `350px`, а максимальную — во всю доступную ширину.
    

**Пример отображения**:

-   На десктопе: 2–3 карточки в ряд (зависит от ширины экрана).
    
-   На планшетах: 2 карточки.
    
-   На мобильных: 1 карточка.
    

**Карточка участника**

```css
.team-card {
  background: rgba(40, 45, 60, 0.6); /* Полупрозрачный фон */
  border-radius: 8px;
  padding: 1.5rem;
  display: flex;
  align-items: center;
  gap: 1.5rem; /* Расстояние между фото и текстом */
  transition: transform 0.3s, box-shadow 0.3s;
  border-left: 3px solid var(--accent-orange); /* Акцентная полоса */
}

.team-card:hover {
  transform: translateY(-5px); /* Эффект "подъёма" */
  box-shadow: 0 5px 15px rgba(0, 200, 255, 0.2); /* Свечение */
}
```
 **Фото участника**

```css
.team-photo {
  width: 80px;
  height: 80px;
  border-radius: 50%; /* Круглое фото */
  border: 2px solid var(--accent-orange);
  object-fit: cover; /* Изображение заполняет круг */
}
```
**Текст в карточке**

```css
.team-name {
  font-size: 1.2rem;
  color: var(--accent-blue);
  margin-bottom: 0.3rem;
}

.team-role {
  font-size: 0.9rem;
  color: var(--text-light);
  opacity: 0.8; /* Лёгкая прозрачность */
}
```

## 5. Страница "Ресурсы" (`resources.html`)**

### HTML-структура

```html
<!DOCTYPE html>
<html lang="ru">
<head>
  <!-- Стили и шрифты -->
</head>
<body>
  <header>...</header>

  <main class="main-content">
    <section class="resources-section">
      <h1>Ресурсы</h1>
      <p>Здесь вы найдёте дополнительные материалы по игре...</p>

      <!-- Блок концепт-артов -->
      <h2>Концепт-арты</h2>
      <div class="resource-grid">
        <div class="resource-card">
          <img src="concept1.png" alt="Концепт-арт" class="resource-image">
          <div class="resource-info">
            <h3>Хозяйка мастерской</h3>
            <p>Ранние наброски персонажа</p>
          </div>
        </div>
        <!-- Ещё 3 аналогичные карточки -->
      </div>

      <!-- Аудио-секция -->
      <h2>Музыка и звуки</h2>
      <div class="audio-section">
        <div class="audio-header">
          <img src="sound.png" alt="Обложка саундтрека">
          <div>
            <h3>Саундтрек</h3>
            <p>Демо-версии композиций</p>
          </div>
        </div>
        <div class="audio-tracks">
          <div>
            <h4>Тема меню</h4>
            <audio controls class="audio-player">
              <source src="demo2_2.wav" type="audio/wav">
            </audio>
          </div>
          <!-- Второй трек -->
        </div>
      </div>

      <!-- Референсы -->
      <h2>Референсы</h2>
      <div class="resource-grid">
        <div class="resource-card">
          <img src="ref1.png" alt="Laika" class="resource-image">
          <div class="resource-info">
            <h3>Laika: Aged Through Blood</h3>
          </div>
        </div>
        <!-- Второй референс -->
      </div>

      <!-- Блог разработки -->
      <h2>Блог разработки</h2>
      <div class="blog-posts-horizontal">
        <div class="blog-card-horizontal">
          <img src="gg.png" alt="Дизайн персонажей" class="blog-image-horizontal">
          <div class="blog-content-horizontal">
            <div class="blog-date-horizontal">16 марта 2025</div>
            <h3 class="blog-title-horizontal">Дизайн персонажей</h3>
            <p class="blog-excerpt">Процесс создания главной героини...</p>
          </div>
        </div>
        <!-- Ещё 3 карточки -->
      </div>

      <!-- Ссылки -->
      <h2>Следите за разработкой</h2>
      <a href="https://t.me/shiver_game" class="external-link">@shiver_game →</a>
    </section>
  </main>

  <footer>...</footer>
</body>
</html>
```

### Уникальные стили для страницы

 **Блок концепт-артов и референсов**

```css
.resource-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr); /* 2 колонки */
  gap: 1.5rem;
  margin: 2rem 0;
}

.resource-card {
  background: rgba(40, 45, 60, 0.6);
  border-radius: 8px;
  overflow: hidden;
  border-left: 3px solid var(--accent-orange);
  transition: transform 0.3s;
}

.resource-card:hover {
  transform: translateY(-5px);
}

.resource-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.resource-info {
  padding: 1.5rem;
}
```
**Аудио-секция**

```css
.audio-section {
  background: rgba(40, 45, 60, 0.6);
  border-radius: 8px;
  padding: 2rem;
  margin: 2rem 0;
  border-left: 3px solid var(--accent-orange);
}

.audio-header {
  display: flex;
  align-items: center;
  margin-bottom: 1.5rem;
}

.audio-header img {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 2px solid var(--accent-orange);
  margin-right: 1.5rem;
}

.audio-tracks {
  display: grid;
  grid-template-columns: 1fr 1fr; /* 2 колонки */
  gap: 1.5rem;
}

.audio-player {
  width: 100%;
  margin-top: 0.5rem;
}
```
 **Горизонтальный блог**

```css
.blog-posts-horizontal {
  display: flex;
  gap: 1.5rem;
  overflow-x: auto; /* Горизонтальный скролл */
  padding-bottom: 1rem;
  scrollbar-width: none; /* Скрыть скроллбар в Firefox */
}

.blog-posts-horizontal::-webkit-scrollbar {
  display: none; /* Скрыть скроллбар в Chrome */
}

.blog-card-horizontal {
  min-width: 250px;
  background: rgba(40, 45, 60, 0.6);
  border-radius: 8px;
  overflow: hidden;
  border-left: 3px solid var(--accent-orange);
}

.blog-image-horizontal {
  width: 100%;
  height: 150px;
  object-fit: cover;
}

.blog-content-horizontal {
  padding: 1rem;
}

.blog-date-horizontal {
  color: var(--accent-blue);
  font-size: 0.8rem;
}
```
**Ссылки**

```css
.external-link {
  color: var(--accent-orange);
  text-decoration: none;
  transition: color 0.3s;
}

.external-link:hover {
  color: var(--accent-blue);
  text-decoration: underline;
}
```
## Заключение и выводы

В ходе проектной практики был разработан  полноценный многостраничный сайт для игры Shiver, соответствующий современным стандартам веб-разработки.

### Ключевые достижения:
 **Единый стиль**

-   Использование CSS-переменных для цветов, отступов и шрифтов.
    
-   Единый дизайн-код на всех страницах (хедер, футер, кнопки).

-   Эффекты при наведении (hover,  transform).
    
-   Горизонтальный скролл для блога разработки.
    
-   Стилизованные аудиоплееры.
    

**Структура контента**

   -   **Главная**  — акцент на визуальную презентацию.
        
    -   **Об игре**  — описание лора и геймплея.
        
    -   **О проекте**  — организация и этапы разработки.
        
    -   **Команда**  — наглядное представление участников и вклада каждого.
        
    -   **Ресурсы**  — дополнительные материалы для связи и погружения в атмосферу разработки.

Сайт успешно презентует игру Shiver через разнообразный контент и стильный дизайн, и демонстрирует структуру команды и этапы разработки.
