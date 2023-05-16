def modificar_cfg(valor, nombre_archivo):
    with open('r-0.8.cfg', 'r') as archivo:
        lineas = archivo.readlines()

    for i in range(len(lineas)):
        if lineas[i].startswith('#-'):
            lineas[i + 1] = f'M {valor}\n'

    with open(nombre_archivo, 'w') as archivo_nuevo:
        archivo_nuevo.writelines(lineas)

    print(f"Se ha generado el archivo {nombre_archivo}.")

# Generar archivos para valores de 0.84 a 1.4 en incrementos de 0.04
for valor in range(84, 141, 4):
    valor_real = valor / 100
    nombre_archivo = f"r-{valor_real:.2f}.cfg"
    valor_m = input(f"Ingrese el valor de M para el archivo {nombre_archivo}: ")
    modificar_cfg(valor_m, nombre_archivo)
