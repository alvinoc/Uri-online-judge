A,B,C = input().split()
triangulo = (float(A)*float(C))/2
circulo = float(C)*float(C)*3.14159
trapezio = ((float(A)+float(B))*float(C))/2
quadrado = float(B)*float(B)
retangulo = float(A)*float(B)
print("TRIANGULO: %0.3f"%triangulo)
print("CIRCULO: %0.3f"%circulo)
print("TRAPEZIO: %0.3f"%trapezio)
print("QUADRADO: %0.3f"%quadrado)
print("RETANGULO: %0.3f"%retangulo)