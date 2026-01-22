# Console Game

Original idea is to create a console game with movement, weapon selection, gear, and other objects. The game involves fighting enemies, completing quests, etc. Combat should be similar to Fight Club combat (google it).

Character stats:
- Name
- Gender
- Clan
- Level
- Experience points
- Skill/stat distribution points
- Health level
- Luck
- Strength
- Dexterity
- Movement
- Intelligence
- Critical hit chance
- Weapon proficiency skills
- Specialization (gives weapon bonuses)

Weapons and items will add or subtract stats. Later there will be artifacts, rings, amulets that give stat bonuses.

All stats will somehow affect the quality of various actions. Strike power, dodge, movement, etc.

The game is first-person, meaning there's a hero and you play as them, level up, gain experience and so on.

(NOT READY YET) The first completed iteration should have an endless mode where the player can fight enemies, level up stats, pick up loot, change clothes and weapons, drink potions. Fighting enemies should be optional. Level up weapon proficiency.


## GAMEPLAY

### What works:
- Character creation
- Specialization creation
- Equipping gear and weapons by selecting from backpack, items are removed from bag and added to the equipped list (_what_is_on)
- Removing weapons and gear works, items are removed from the equipped list (_what_is_on) and added back to the bag
- Combat works
- Critical damage works in combat
- Experience earning works
- Leveling up by gaining experience works
- Skill point allocation on level up works
- Can drink health potions
- Replacing gear on character (if holding an axe, when selecting new weapon the previous item should return to backpack)

### TO DO BEFORE INTERMEDIATE GOAL:
- Make it possible to view what dropped and pick it up (pickup kinda works)
- Test gear drops, test gear pickup.

### KNOWN BUG
- Location effects don't add to hero stats, for some reason everything converts to tuple instead of int.
- this feature is currently disabled.

## GAME MECHANICS:

### Works:
- Random enemy generation with fine-tuned generation settings
- Random weapon and armor generation with fine-tuned generation settings
- Random clothing and weapon generation equipped on random enemies based on level
- On enemies all gear and weapon parameters are added to stats
- Can view what's equipped on character with print_whats_on function
- Random generation of enemy backpack contents
- Movement between locations

### To Do:
- Make potions, not just healing but others too
- Make abstract methods
- Make private attributes using __setattr__
- Save characters using pickle or shelve

### Think through the following mechanics
- Make it possible to choose what to do next at any moment except combat
- Think about weapon mechanics

### Future development perspective
- Weapon and item durability, item breakage
- Make it possible to flee from combat (losing experience, items?)
- Dodge and block mechanics
- Artifacts and shields
- Saving and resuming game


## More distant perspective
- Map, movement
- Make it online

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
```bash
python3 game/main.py
```
