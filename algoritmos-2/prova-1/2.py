values_list = []


def add_values():
  for i in range(3):
    value = int(input("Digite um número inteiro:"))
    values_list.append(value)

def get_negative_values():
  negative_values_counter = 0

  for i in range(len(values_list)):
    if values_list[i] == 0:
      print(f"O valor na posição {i} do array é zero.")
      negative_values_counter += 1
    
    if values_list[i] < 0:
      print(f"O valor {values_list[i]} na posição {i} do array é menor que 0.")

  if negative_values_counter == 0:
    print("Nenhum valor é menor ou igual a zero.")

add_values()
get_negative_values()