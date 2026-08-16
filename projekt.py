class Room:
    def __init__(self, name, description, items: list, exits: dict):
        self.name = name
        self.description = description
        self.items = items
        self.exits = exits

    def describe(self):
        return f"Szoba neve: {self.name}, Leiras: {self.description}, Targyak: {self.items} kijaratok: {list(self.exits.keys())}"

class Player:
    total_players = 0

    def __init__(self, name,current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
        Player.total_players += 1

    def move(self, direction, rooms):
        if direction not in self.current_room.exits:
            raise ValueError("Nem letezo irany")

        room_name = self.current_room.exits[direction]
        self.current_room = rooms[room_name]

    def show_inventory(self):
        return self.inventory       

    def pick_up(self, item_name):
        if item_name in self.current_room.items:
            self.inventory.append(item_name)
            self.current_room.items.remove(item_name)
        else:
            raise ValueError('Nem letezo targy.')
        


class Game:
    def __init__(self):
        self.rooms = {}

    def add_room(self, room):
        self.rooms[room.name] = room

    def process_command(self, player, command):
        parts = command.split(' ')
        action = parts[0]
        object_name = parts[1] if len(parts) > 1 else None

        if action == "look":
            print(player.current_room.describe())
        elif action == "inventory":
            print(f"{player.name} inventory: {player.show_inventory()}")
        elif action == "take":
            player.pick_up(object_name)
        elif action == "move":
            player.move(object_name, self.rooms)
        else:
            raise ValueError('Nem letezo parancs')


hall = Room(
    "Hall",
    "Egy tágas előcsarnok, porlepte csillárral a mennyezeten.",
    items=["torch", "key"],
    exits={"north": "Library", "east": "Kitchen"}
)

library = Room(
    "Library",
    "Padlótól plafonig érő könyvespolcok, dohos papírszaggal.",
    items=["old_book", "candle"],
    exits={"south": "Hall", "east": "Study"}
)

kitchen = Room(
    "Kitchen",
    "Egy elhagyatott konyha, penészes edényekkel a mosogatóban.",
    items=["knife", "bread"],
    exits={"west": "Hall", "north": "Study"}
)

study = Room(
    "Study",
    "Egy kis dolgozószoba, íróasztallal és egy zárt fiókkal.",
    items=["quill", "map"],
    exits={"south": "Kitchen", "west": "Library"}
)

game = Game()
game.add_room(hall)
game.add_room(library)
game.add_room(kitchen)
game.add_room(study)


player = Player("test_ember", hall)  # kezdő szoba: Hall

# Parancsok tesztelése
game.process_command(player, "look")
game.process_command(player, "take torch")
game.process_command(player, "move north")
game.process_command(player, "look")
game.process_command(player, "take old_book")
game.process_command(player, "inventory")
game.process_command(player, "move south")
try:   # vissza a Hall-ba
    game.process_command(player, "move west")
except ValueError as e:
    print(e)
try:  # érvénytelen irány -> hibaüzenet
    game.process_command(player, "take nonexistent_item")
except ValueError as e:
    print(e)  # nem létező tárgy -> hibaüzenet
