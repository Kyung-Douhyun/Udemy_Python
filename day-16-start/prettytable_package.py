from prettytable import PrettyTable

# 객체 생성
table = PrettyTable()

# 객체 함수
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# 객체 속성
table.align = "l"


print(table)
