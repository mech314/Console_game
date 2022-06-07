# Console game

```textmate
Изначальная идея создать консольную игру с возможностью движения, выбора оружия, шмоток, каких то других обьектов. Игра подорузумевает драки с врагами, выполнение квестов итд. Боевка должна быть похожа на боевку бойцовского клуба (гугл). Есть ряд характеристик персоонажа:
** Имя **
Пол
Клан
Уровень
Количество опыта
Количество очков распределения навыков\характеристик
Уровень жизни
Удача
Сила
Ловкость
Движение
Интелект
Шанс критического удара
Навыки владения разным типом оружия
Специализация (дает бонусы по оружию)

Оружие и предметы будут добавлять характеристики или отнимать их. Позже появятся предметы в виде артефактов, колец, ожирелий которые будут давать + к характеристикам.

Все характеристики так или иначе будут влиять на качество тех или иных действий. Сила удара, уворот, движение итд. 
Игра будет от одного лица, то есть есть герой и ты им играешь, прокачиваешь, набираешься опыта и так далее.
(ЕЩЕ НЕ ГОТОВО) Первая законченная итерации игры должна иметь безпрерывний режим, где игрок может драться с врагами, провышать уровень и характеристики, подбирать лут, переодеваться и менять оружие, пить зелья. Битва с врагами должна быть опциональной. Поднимать навык вледния оружием.


## ГЕЙМПЛЕЙ
# Что работает:
Создание персонажей
Создание специальностей
Одевание шмоток выбирая из рюкзака
Работает бой
В бою работает критический урон
Работает зарабатывание опыта
Работает повышение уровня по набору опыта
Работает добавление скиллов при повышении уровня

# Не сделано:
Пить зелья лечения
Снимание шмоток
Снимание оружия
Выбор оружия из рюкзака

## ИГРОВАЯ МЕХАНИКА:
#Работает:
Рандомная генерация врагов с возможностью тонкой настройки генерации
Рандомная генерация оружия и брони с возможностью тонкой настройки генерации

# Сделать:
Сделать рандомную генерацию одежды и оружия одетых на врагах
Сделать рандомную генерацию содержимого рюкзака врагов
Сделать выпадение части рюкзака и одетых шмоток со врага при смерти
Сделать возможность посмотреть что выпало и подобрать (подобрать работает)
Сделать зелья, не только лечения но и другие


# Продумать следующие механики
Сделать возможность выбирать что делать дальше в любой момент кроме боя
Подумать над механикой оружия
Сделать возможность пить зелья в бою
Возможность взглянуть на врага (броня, оружие) в любое время боя

## Дальнейшая перспектива развития
Износ оружия и вещей, поломка вещей
Сделать возможность сбежать из боя (теряя опыт, вещи?)
Механика уворота и блокировок удара
Артифакты и щиты
Сохранение и возобновление игры


## Более дальнаяя перспектива
Карта, движение
Сделать онлайн

```

## Installation

```bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

## Testing
```bash
python3 game/tests.py
```
