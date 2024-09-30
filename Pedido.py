from te import Te
from validate import validate

# Solicitar al usuario el sabor del té
sabor = validate([1, 2, 3], int(
    input(
        "¿Qué sabor de té desea? (Ingrese número de la opción)"
        "\n1. Té negro \n2. Té verde \n3. Agua de hierbas\n"
    )
))

# Solicitar al usuario el formato (gramos) deseado
formato = validate([500, 300], int(
    input(
        "¿Qué formato desea?. Tenemos disponible"
        " 300 y 500 gramos. Ingrese la cantidad de gramos deseada\n"
    )
))

# Crear instancia de la clase Te
sabores_te = Te()

# Obtener tiempo de preparación y recomendación según el sabor
tiempo, recomendacion = sabores_te.retorna_tiempo_y_recomendacion(sabor)

# Obtener el precio según el formato
precio = sabores_te.retorna_precio(formato)

# Definir el nombre del sabor basado en la selección del usuario
if sabor == 1:
    sabor_texto = "Té negro"
elif sabor == 2:
    sabor_texto = "Té verde"
elif sabor == 3:
    sabor_texto = "Agua de hierbas"
else:
    sabor_texto = "Sabor no válido"  # En caso de un error inesperado

# Validación de sabor y formato
if precio == 0:
    print("Formato o sabor no válidos.")
else:
    # Mostrar los detalles del pedido
    print(
        f"Se ingresó su pedido de {sabor_texto}, en formato de {formato} gramos, "
        f"el cual tiene un valor de ${precio}. Este té tiene un tiempo de preparación "
        f"de {tiempo} minutos, y se recomienda su uso {recomendacion}."
    )

