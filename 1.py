a = []
b = []

inverted_a = []
inverted_b = []

def add_list_elements():
  print("\nLista A")
  for i in range(3):
    a.append(input(f"Digite o valor do {i + 1} elemento: "))

  print("\nLista B")
  for i in range(3):
    b.append(input(f"Digite o valor do {i + 1} elemento: "))
    

def reverse_lists():
  for i in reversed(range(3)):
    inverted_a.append(a[i])
    inverted_b.append(b[i])

add_list_elements()
reverse_lists()

print(f"\nLista A invertida: ", inverted_a)
print(f"Lista B invertida: ", inverted_b)