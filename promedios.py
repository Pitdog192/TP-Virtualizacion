# Programa para calcular promedio de notas
print("Calculadora de Notas")
notas = []

for i in range(3):
    while True:
        try:
            nota = float(input(f"Ingrese la nota {i+1} (0-10): "))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("La nota debe estar entre 0 y 10")
        except ValueError:
            print("Por favor ingrese un número válido")

promedio = sum(notas) / len(notas)
print(f"\nNotas ingresadas: {notas}")
print(f"El promedio es: {promedio:.2f}")

if promedio >= 7:
    print("¡Excelente trabajo!")
elif promedio >= 5:
    print("Buen trabajo, pero se puede mejorar")
else:
    print("Es necesario estudiar más")
