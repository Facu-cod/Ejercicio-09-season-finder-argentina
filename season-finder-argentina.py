mes = input(
    "Ingresa el mes para determinar a qué estación pertenece: ").strip().lower()

if mes == "septiembre" or mes == "octubre" or mes == "noviembre":
    print(f"El mes de {mes.capitalize()} pertenece a la primavera.")
elif mes == "diciembre" or mes == "enero" or mes == "febrero":
    print(f"El mes de {mes.capitalize()} pertenece al verano.")
elif mes == "marzo" or mes == "abril" or mes == "mayo":
    print(f"El mes de {mes.capitalize()} pertenece al otoño.")
elif mes == "junio" or mes == "julio" or mes == "agosto":
    print(f"El mes de {mes.capitalize()} pertenece al invierno.")
else:
    print("El dato ingresado es erróneo.")
