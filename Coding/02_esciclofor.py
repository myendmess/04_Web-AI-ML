# Stampa i numeri da 1 a 10 tranne il 5.
# Sfrutta il While True e la keyword Continue

i = 1
while True:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1
    if i > 10:
        break