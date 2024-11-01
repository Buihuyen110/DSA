### Вариант 1: Легкий уровень работы с репозиторием (без веток и pull request'ов)
Подходит для небольших проектов, где над кодом работает один человек. Здесь все изменения делаются напрямую в главную ветку без сложной структуры.

**Шаги:**

1. **Создание репозитория:**
   - Создать новый репозиторий на GitHub (или другом хостинге Git-репозиториев).
   - Клонировать репозиторий на свой локальный компьютер:
     ```bash
     git clone <ссылка на репозиторий>
     ```

2. **Добавление изменений:**
   - Добавить/изменить файлы в проекте.
   - Просмотреть состояние файлов:
     ```bash
     git status
     ```
   - Добавить измененные файлы для коммита:
     ```bash
     git add <файл>   # либо git add .
     ```

3. **Коммит и пуш изменений:**
   - Закоммитить изменения с описанием:
     ```bash
     git commit -m "Описание изменений"
     ```
   - Отправить изменения на удалённый сервер:
     ```bash
     git push origin main  # или master, в зависимости от главной ветки
     ```

4. **Получение обновлений с сервера:**
   - Если были изменения в репозитории (например, через GitHub), их можно получить с сервера:
     ```bash
     git pull origin main
     ```

Этот способ прост и удобен для студентов, которые только начинают учиться работать с Git и не работают в команде.

---

### Вариант 2: Работа с ветками и pull request'ами (профессиональный уровень)
Этот метод используется в командах, где каждый участник работает в своей ветке, а изменения отправляются через pull request для проверки и слияния в основную ветку.

**Шаги:**

1. **Создание ветки для задач:**
   - Создать новую ветку для работы над задачей:
     ```bash
     git checkout -b <название-ветки>
     ```

2. **Работа в ветке:**
   - Выполнить необходимые изменения.
   - Добавить изменения в staged-область:
     ```bash
     git add <файл>   # либо git add .
     ```
   - Закоммитить изменения:
     ```bash
     git commit -m "Описание изменений"
     ```

3. **Пуш ветки на сервер:**
   - Отправить свою ветку на удалённый репозиторий:
     ```bash
     git push origin <название-ветки>
     ```

4. **Создание pull request:**
   - На GitHub перейти к ветке и создать pull request (PR) для слияния изменений в основную ветку (например, `main`).
   - Команда просматривает изменения, оставляет комментарии и одобряет PR.

5. **Слияние ветки:**
   - После одобрения PR ветка сливается в главную ветку, и изменения становятся частью основного проекта.
   - Локально необходимо обновить главную ветку:
     ```bash
     git checkout main
     git pull origin main
     ```

6. **Удаление ветки:**
   - Локально:
     ```bash
     git branch -d <название-ветки>
     ```
   - На сервере:
     ```bash
     git push origin --delete <название-ветки>
     ```

---

**Резюме:**
- **Вариант 1** прост и подходит для личных проектов.
- **Вариант 2** сложнее, но необходим для работы в команде и соблюдения контроля версий.
