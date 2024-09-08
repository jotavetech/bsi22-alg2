col_values = []
matrix = [[], [], []]

def get_col_values():
  for i in range(3):
    value = input("Digite um valor: ")
    col_values.append(value)

def get_matrix_values(): 
  for i in range(3):
    for j in range(4):
      value = input(f"Digite o valor da linha {i} na coluna {j}: ")
      matrix[i].append(value)

def replace_col_one_values():
  for i in range(3):
    matrix[i][1] = col_values[i]

def get_prettier_matrix(matrix):
  print(f"Linha 0: {matrix[0]}")
  print(f"Linha 1: {matrix[1]}")
  print(f"Linha 2: {matrix[2]}")
  

print("Montando Coluna")
get_col_values()

print("\nMontando Matriz")
get_matrix_values()

print(f"Os valores a serem substituidos são: {col_values}")
print(f"\nA matriz antes:")

get_prettier_matrix(matrix)

replace_col_one_values()

print(f"\nA matriz final com os valores substituidos: ")

get_prettier_matrix(matrix)
