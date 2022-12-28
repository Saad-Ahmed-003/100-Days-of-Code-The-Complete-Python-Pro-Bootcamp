from prettytable import PrettyTable

table = PrettyTable(["name", "type"])

table.align["name"] = "l"
table.align["type"] = "l"
table.padding_width = 1

table.add_row(["Chesnaught", "grass, fighting"])
table.add_row(["Greninja", "Water, dark"])
table.add_row(["Pikachu", "Electric"])
table.add_row(["Venusaur", "Grass, poison"])
table.add_row(["Charizard", "Fire, flight"])
table.add_row(["Blastoise", "Water"])

print(table)
