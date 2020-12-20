#Colas - se debe importar para utilizarlo

from collections import deque

colas = deque(["Anderson", "Gatos", "Familia", "Peludos"])
print(colas)

colas.pop()
print(colas)

print(colas.popleft())
print(colas)