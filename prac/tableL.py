from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "squartle"])
table.add_column("Type", ["Electric", "Water"])

print(table)
