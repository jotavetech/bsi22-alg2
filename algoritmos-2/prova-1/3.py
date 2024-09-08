values_list = []

def get_values():
  for i in range(5):
    value = float(input("Digite um valor número: "))
    values_list.append(value)

get_values()

higher_value = max(values_list)
lower_value = min(values_list)

print(f"O maior valor é {higher_value}, na posição {values_list.index(higher_value)} do array")
print(f"O menor valor é {lower_value}, na posição {values_list.index(lower_value)} do array")