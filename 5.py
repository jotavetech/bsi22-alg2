matrix = [[], [], [], [], []]

def get_matrix_values(): 
  for i in range(5):
    for j in range(5):
      value = int(input(f"Digite o valor número da linha {i} na coluna {j}: "))
      matrix[i].append(value)

def find_minimax_value(matrix):
  higher_value = 0
  higher_value_row = 0

  for i in range(3):
    higher_matrix_value = max(matrix[i])

    if higher_matrix_value > higher_value: 
      higher_value = higher_matrix_value
      higher_value_row = i

    
  return min(matrix[higher_value_row])

def get_prettier_matrix(matrix):
  print(f"Linha 0: {matrix[0]}")
  print(f"Linha 1: {matrix[1]}")
  print(f"Linha 2: {matrix[2]}")
  print(f"Linha 3: {matrix[3]}")
  print(f"Linha 4: {matrix[4]}")

get_matrix_values()

print("Na matriz:")
get_prettier_matrix(matrix)

print(f"O minimax é o valor {find_minimax_value(matrix)}")

    


