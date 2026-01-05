#!/usr/bin/env python3
"""
Year Compass - Plan Initialization Script

Creates empty planning template and session state for a new year.

Usage:
    python init_plan.py --year 2026 --framework navigator
    python init_plan.py --year 2026 --framework year-compass --output-dir ./Personal/Planning
"""

import argparse
import json
import os
from datetime import datetime
from pathlib import Path

# Framework configurations
FRAMEWORKS = {
    "navigator": {
        "name": "Navigator",
        "sections": {
            "retro": [
                "calendar_review",
                "life_spheres",
                "victories",
                "challenges",
                "forgiveness",
                "energy_audit",
                "year_summary"
            ],
            "planning": [
                "vision",
                "priorities_selection",
                "priority_1",
                "priority_2",
                "priority_3",
                "wishes",
                "pre_mortem",
                "january_plan"
            ]
        }
    },
    "year-compass": {
        "name": "Year Compass",
        "sections": {
            "retro": [
                "calendar_review",
                "life_domains",
                "key_moments",
                "six_questions",
                "best_moments",
                "achievements_challenges",
                "forgiveness",
                "letting_go",
                "year_summary"
            ],
            "planning": [
                "dream_big",
                "vision",
                "magic_threes",
                "wishes",
                "word_of_year",
                "secret_wish",
                "commitment"
            ]
        }
    },
    "hybrid": {
        "name": "Гибрид",
        "sections": {
            "retro": [
                "calendar_review",
                "life_spheres",
                "key_moments",
                "six_questions",
                "victories",
                "challenges",
                "forgiveness",
                "letting_go",
                "energy_audit",
                "year_summary"
            ],
            "planning": [
                "dream_big",
                "vision",
                "priorities_selection",
                "priority_1",
                "priority_2",
                "priority_3",
                "magic_threes",
                "wishes",
                "pre_mortem",
                "january_plan"
            ]
        }
    }
}

SECTION_NAMES = {
    "calendar_review": "Обзор календаря",
    "life_spheres": "Сферы жизни",
    "life_domains": "8 доменов жизни",
    "key_moments": "Ключевые моменты",
    "six_questions": "6 вопросов о себе",
    "best_moments": "Лучшие моменты",
    "victories": "Победы и достижения",
    "achievements_challenges": "Достижения и вызовы",
    "challenges": "Вызовы и уроки",
    "forgiveness": "Прощение",
    "letting_go": "Отпускание",
    "energy_audit": "Аудит энергии",
    "year_summary": "Итоги года",
    "dream_big": "Мечтай по-крупному",
    "vision": "Видение 3-5 лет",
    "priorities_selection": "Выбор 3 приоритетов",
    "priority_1": "Приоритет #1",
    "priority_2": "Приоритет #2",
    "priority_3": "Приоритет #3",
    "magic_threes": "Волшебные тройки",
    "wishes": "10 желаний",
    "word_of_year": "Слово года",
    "secret_wish": "Секретное желание",
    "pre_mortem": "Pre-Mortem анализ",
    "january_plan": "План на январь",
    "commitment": "Обязательство"
}


def create_empty_plan(year: int, framework: str) -> str:
    """Generate empty plan markdown content."""
    fw = FRAMEWORKS[framework]
    today = datetime.now().strftime("%Y-%m-%d")

    content = f"""---
title: Годовой план {year}
created: {today}
framework: {framework}
last_updated: {today}
status: not_started
iteration: 1
---

# Годовой план {year}

> Создан с помощью фреймворка {fw['name']}
> Фасилитатор: Claude (year-compass skill)

---

## Часть 1: Ретроспектива {year - 1} года

"""

    # Add retro sections
    for i, section_id in enumerate(fw["sections"]["retro"], 1):
        section_name = SECTION_NAMES.get(section_id, section_id)
        content += f"""### 1.{i} {section_name}
**Глубина:** ☆☆☆☆☆ (не заполнено)

<!-- TODO: Заполнить -->

---

"""

    content += f"""
## Часть 2: Планирование {year} года

"""

    # Add planning sections
    for i, section_id in enumerate(fw["sections"]["planning"], 1):
        section_name = SECTION_NAMES.get(section_id, section_id)
        content += f"""### 2.{i} {section_name}
**Глубина:** ☆☆☆☆☆ (не заполнено)

<!-- TODO: Заполнить -->

---

"""

    content += f"""
## Метаданные

- **Дата создания:** {today}
- **Фреймворк:** {fw['name']}
- **Итерация:** 1 (первое заполнение)
- **Цель глубины:** ⭐⭐⭐☆☆ (3/5 для первого прохода)
"""

    return content


def create_session_state(year: int, framework: str) -> dict:
    """Generate initial session state JSON."""
    fw = FRAMEWORKS[framework]
    today = datetime.now().isoformat()

    sections = {}

    # Add all sections as pending
    for section_id in fw["sections"]["retro"]:
        sections[section_id] = {
            "status": "pending",
            "depth": 0,
            "iteration": 1,
            "started_at": None,
            "completed_at": None,
            "duration_minutes": 0,
            "prompts_completed": [],
            "prompts_skipped": []
        }

    for section_id in fw["sections"]["planning"]:
        sections[section_id] = {
            "status": "pending",
            "depth": 0,
            "iteration": 1,
            "started_at": None,
            "completed_at": None,
            "duration_minutes": 0,
            "prompts_completed": [],
            "prompts_skipped": []
        }

    return {
        "framework": framework,
        "year": year,
        "created_at": today,
        "last_session": None,
        "sections": sections,
        "total_time_minutes": 0,
        "breaks_taken": 0,
        "current_section": None,
        "iteration": 1
    }


def main():
    parser = argparse.ArgumentParser(
        description="Initialize Year Compass planning documents"
    )
    parser.add_argument(
        "--year",
        type=int,
        default=datetime.now().year,
        help="Planning year (default: current year)"
    )
    parser.add_argument(
        "--framework",
        choices=["navigator", "year-compass", "hybrid"],
        default="navigator",
        help="Planning framework to use"
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="Personal/Planning",
        help="Output directory (default: Personal/Planning)"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing files"
    )

    args = parser.parse_args()

    # Create output directory
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Create monthly subdirectory
    monthly_dir = output_dir / f"{args.year}_monthly"
    monthly_dir.mkdir(exist_ok=True)

    # Create archive subdirectory
    archive_dir = output_dir / "archive"
    archive_dir.mkdir(exist_ok=True)

    # File paths
    plan_file = output_dir / f"{args.year}_annual_plan.md"
    session_file = output_dir / ".planning-session.json"

    # Check for existing files
    if plan_file.exists() and not args.force:
        print(f"❌ Файл {plan_file} уже существует. Используйте --force для перезаписи.")
        return 1

    # Create empty plan
    plan_content = create_empty_plan(args.year, args.framework)
    plan_file.write_text(plan_content, encoding="utf-8")
    print(f"✅ Создан: {plan_file}")

    # Create session state
    session_state = create_session_state(args.year, args.framework)
    session_file.write_text(
        json.dumps(session_state, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    print(f"✅ Создан: {session_file}")

    # Summary
    fw = FRAMEWORKS[args.framework]
    total_sections = len(fw["sections"]["retro"]) + len(fw["sections"]["planning"])

    print(f"""
┌─────────────────────────────────────────────────────────────┐
│                 ПЛАН ИНИЦИАЛИЗИРОВАН                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Год:        {args.year}                                         │
│  Фреймворк:  {fw['name']:<20}                          │
│  Секций:     {total_sections}                                          │
│                                                              │
│  Файлы:                                                      │
│  • {str(plan_file):<50} │
│  • {str(session_file):<50} │
│                                                              │
│  Следующий шаг: Начните заполнение командой 'start'         │
│                                                              │
└─────────────────────────────────────────────────────────────┘
""")

    return 0


if __name__ == "__main__":
    exit(main())
