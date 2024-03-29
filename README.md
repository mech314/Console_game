# Console game

Изначальная идея создать консольную игру с возможностью движения, выбора оружия, шмоток, каких то других обьектов. Игра подорузумевает драки с врагами, выполнение квестов итд. Боевка должна быть похожа на боевку бойцовского клуба (гугл). 

Есть ряд характеристик персонажа:
- Имя
- Пол
- Клан
- Уровень
- Количество опыта
- Количество очков распределения навыков\характеристик
- Уровень жизни
- Удача
- Сила
- Ловкость
- Движение
- Интелект
- Шанс критического удара
- Навыки владения разным типом оружия
- Специализация (дает бонусы по оружию)

Оружие и предметы будут добавлять характеристики или отнимать их. Позже появятся предметы в виде артефактов, колец, ожирелий которые будут давать + к характеристикам.

Все характеристики так или иначе будут влиять на качество тех или иных действий. Сила удара, уворот, движение итд.

Игра будет от одного лица, то есть, есть герой и ты им играешь, прокачиваешь, набираешься опыта и так далее.

(ЕЩЕ НЕ ГОТОВО) Первая законченная итерации игры должна иметь безпрерывний режим, где игрок может драться с врагами, провышать уровень и характеристики, подбирать лут, переодеваться и менять оружие, пить зелья. Битва с врагами должна быть опциональной. Поднимать навык вледния оружием.


## ГЕЙМПЛЕЙ

### Что работает:
- Создание персонажей
- Создание специальностей
- Одевание шмоток и оружия выбирая из рюкзака, вещи убираются из рюкзака (bag) и добавляются в список (_what_is_on)
- Снятие оружия и шмоток работает, вещи убираются из списка (_what_is_on) и добавляются oбратно в список (bag)
- Работает бой
- В бою работает критический урон
- Работает зарабатывание опыта
- Работает повышение уровня по набору опыта
- Работает добавление скиллов при повышении уровня
- Можно пить зелья здоровья
- Замена шмоток на персоонаже (если в руках топор, при выборе нового оружия преидущая вещь должна вернутся в рюкзак)

### ДО ПРОМЕЖУТОЧНОЙ ЦЕЛИ СДЕЛАТЬ:
- Сделать возможность посмотреть что выпало и подобрать (типа работает подобрать работает)
- Проверить выпадение шмотья, проверить подбирание шмотья.

### Известный БАГ
- Эффекты от локаций не прибавляются к статам героя, почему то все преобразовывается в тупл а не инт.
- пока эта фича отключена.

## ИГРОВАЯ МЕХАНИКА:

### Работает:
- Рандомная генерация врагов с возможностью тонкой настройки генерации
- Рандомная генерация оружия и брони с возможностью тонкой настройки генерации
- Рандомная генерация одежды и оружия одетых на рандомных врагах в зависимости от уровня
- На Врагах все параметры шмоток и оружия добавляются к статам
- Можно посмотреть что одето на персоонаже фунцией print_whats_on
- Раандомная генерация содержимого рюкзака врагов
- Передвижение по локациям

### Сделать:
- Сделать зелья, не только лечения но и другие
- Сделать абстрактные методы
- Сделать приватные атрибуты с помощью __setattr__
- Сохранять персонажей с помощью pickle or shelve

### Продумать следующие механики
- Сделать возможность выбирать что делать дальше в любой момент кроме боя
- Подумать над механикой оружия

### Дальнейшая перспектива развития
- Износ оружия и вещей, поломка вещей
- Сделать возможность сбежать из боя (теряя опыт, вещи?)
- Механика уворота и блокировок удара
- Артифакты и щиты
- Сохранение и возобновление игры


## Более дальнаяя перспектива
- Карта, движение
- Сделать онлайн

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
## Gameplay
python3 game/main.py
