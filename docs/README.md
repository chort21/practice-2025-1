# Документация: базовая часть задания
## Создание статического веб-сайта с помощью HTML/CSS
### 1.Главная страница (index.html)
###HTML-структура

'''html
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
Уникальные стили для главной страницы
Герой-секция (Hero Section)
css
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
'''
###Эффекты:
- Фоновое изображение на всю ширину.
- Логотип поверх изображения с точным позиционированием.

###Информационные плашки
'''css
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
'''
###Ключевые особенности:
- Гибкая структура (текст + изображение).
- Интерактивные кнопки с анимацией.
- Полупрозрачность для современного вида.








