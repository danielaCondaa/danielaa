nombre = "Tu Nombre"
edad = 25
correo = "tucorreo@example.com"
telefono = "1234567890"
experiencia = ["Experiencia 1", "Experiencia 2", "Experiencia 3"]
educacion = [("Título 1", "Institución 1", 2015), ("Título 2", "Institución 2", 2018)]

# Imprimir información personal
print("Nombre: " + nombre)
print("Edad: " + str(edad))
print("Correo electrónico: " + correo)
print("Teléfono: " + telefono)

# Imprimir experiencia laboral
print("Experiencia laboral:")
for exp in experiencia:
    print("- " + exp)

# Imprimir educación
print("Educación:")
for edu in educacion:
    print("- Título: " + edu[0])
    print("  Institución: " + edu[1])
    print("  Año de graduación: " + str(edu[2]))
