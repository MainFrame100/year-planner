# Установка для Claude Code

## Требования

- Claude Code CLI установлен и настроен
- Доступ к локальной файловой системе

## Установка

### Вариант 1: Копирование папки

```bash
# Перейти в корень вашего проекта
cd /path/to/your/project

# Создать директорию для skills (если её нет)
mkdir -p .claude/skills

# Скопировать skill
cp -r /path/to/year-compass/claude-code/year-compass .claude/skills/
```

### Вариант 2: Git clone

```bash
# Клонировать репозиторий
git clone https://github.com/dmitrii-yu/year-compass.git

# Скопировать нужную версию
cp -r year-compass/claude-code/year-compass .claude/skills/
```

## Структура после установки

```
your-project/
├── .claude/
│   └── skills/
│       └── year-compass/
│           ├── SKILL.md
│           ├── scripts/
│           │   └── init_plan.py
│           └── references/
│               ├── coaching-principles.md
│               ├── evidence-based-methods.md
│               ├── session-management.md
│               ├── templates.md
│               ├── year-compass.md
│               ├── navigator.md
│               ├── hybrid.md
│               ├── goal-types.md
│               ├── problem-solution-mapping.md
│               └── monthly-review.md
└── Personal/
    └── Planning/           # Здесь будут храниться ваши планы
```

## Использование

### Первый запуск

```
> /year-compass

Claude: Добро пожаловать в Year Compass!
        Какой фреймворк вы хотите использовать?
        A) Year Compass — эмоциональная глубина
        B) Navigator — 3 приоритета
        C) Гибрид — лучшее из обоих
```

### Инициализация плана

После выбора фреймворка Claude создаст:
- `Personal/Planning/2026_annual_plan.md` — ваш план
- `Personal/Planning/.planning-session.json` — состояние сессий

### Команды

| Команда | Действие |
|---------|----------|
| `/year-compass` | Запустить skill |
| `status` | Показать прогресс |
| `start [section]` | Начать раздел |
| `break` | Сделать перерыв |
| `review` | Месячный обзор |

## Продолжение работы

При следующем вызове `/year-compass` Claude автоматически:
1. Загрузит состояние из `.planning-session.json`
2. Покажет ваш прогресс
3. Предложит продолжить с места остановки

## Troubleshooting

### Skill не найден

Убедитесь, что папка `year-compass` находится в `.claude/skills/`:

```bash
ls -la .claude/skills/year-compass/
```

### Ошибка при init

Проверьте, что Python 3 установлен:

```bash
python --version
# или
python3 --version
```

---

Last Updated: 2026-01-05
