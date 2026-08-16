# Text Adventure Game Project

## Projekt Leírása (Project Description)

Ez egy egyszerű szöveges kalandjáték, amely az objektumorientált programozás (OOP) koncepcióit mutatja be. A játék egy kastély különböző szobáiból áll, ahol a játékos tárgyakat gyűjthet és szobák között mozoghat.

*This is a simple text-based adventure game demonstrating object-oriented programming (OOP) concepts. The game consists of different rooms in a castle where the player can collect items and move between rooms.*

---

## Fő Osztályok (Main Classes)

### `Room`
Egy játék szobát reprezentál.
- **Paraméterek (Parameters):**
  - `name`: A szoba neve
  - `description`: A szoba leírása
  - `items`: A szobában lévő tárgyak listája
  - `exits`: A szobakijáratok szótára (irány → szoba név)

- **Metódus (Method):**
  - `describe()`: Visszaadja a szoba teljes leírását

### `Player`
A játékost reprezentálja.
- **Paraméterek (Parameters):**
  - `name`: A játékos neve
  - `current_room`: A játékos aktuális szobája
  - `inventory`: A játékos tárgyai (lista)
  - `total_players`: Osztályváltozó, a játékosok száma

- **Metódusok (Methods):**
  - `move(direction, rooms)`: Mozgás egy adott irányba
  - `show_inventory()`: Az inventory tartalmának kilistázása
  - `pick_up(item_name)`: Tárgy felvétele a szobából

### `Game`
A játék fő vezérlőosztálya.
- **Paraméterek (Parameters):**
  - `rooms`: Az összes szoba szótára

- **Metódusok (Methods):**
  - `add_room(room)`: Szoba hozzáadása a játékhoz
  - `process_command(player, command)`: Parancs feldolgozása

---

## Játék Parancsok (Game Commands)

| Parancs | Leírás | Példa |
|---------|--------|-------|
| `look` | A jelenlegi szoba leírása | `look` |
| `inventory` | Az inventory tartalmának megjelenítése | `inventory` |
| `take [tárgy]` | Tárgy felvétele | `take torch` |
| `move [irány]` | Mozgás egy szobába | `move north` |

---

## Szobák (Rooms)

1. **Hall** - A kastély előcsarnoka (torch, key)
2. **Library** - Könyvtár (old_book, candle)
3. **Kitchen** - Konyha (knife, bread)
4. **Study** - Dolgozószoba (quill, map)

---

## Futtatás (Running the Game)

```bash
python projekt.py
```

---

## Példa Gameplay (Example Gameplay)

```
Szoba neve: Hall, Leiras: Egy tágas előcsarnok, porlepte csillárral a mennyezeten., Targyak: ['torch', 'key'] kijaratok: ['north', 'east']
test_ember inventory: ['torch']
Szoba neve: Library, Leiras: Padlótól plafonig érő könyvespolcok, dohos papírszaggal., Targyak: ['old_book', 'candle'] kijaratok: ['south', 'east']
test_ember inventory: ['torch', 'old_book']
```

---

## OOP Koncepciók (OOP Concepts)

- **Encapsulation**: Az adatok és metódusok egy osztályban vannak csoportosítva
- **Inheritance**: (Kész az kiterjesztésre)
- **Polymorphism**: A `process_command()` metódus különböző parancsokra reagál
- **Abstraction**: A játék logikája rejtett az osztályok mögött

---
