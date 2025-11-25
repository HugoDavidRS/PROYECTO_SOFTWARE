import os

# Mensaje secreto legible
mensaje = b"Mensaje secreto: firmado por Jesus, 12/11/2025\n"

# Tamaño total del archivo en bytes (1 KB)
tamano_total = 1024  

# Relleno binario aleatorio
relleno = os.urandom(tamano_total - len(mensaje))

# Combina y guarda
contenido = mensaje + relleno

with open("dummy_firmable.bin", "wb") as f:
    f.write(contenido)

print("Archivo binario con mensaje secreto generado: dummy_firmable.bin")