n1, n2, n3, n4 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = float(((n1*2)+(n2*3)+(n3*4)+n4)/10)
print("Media: %0.1f"%media)
if media>=7.0:
    print("Aluno aprovado.")
elif media<5.0:
    print("Aluno reprovado.")
elif media>=5.0 or media<=6.9:
    print("Aluno em exame.")
    exame = float(input())
    print("Nota do exame: %0.1f"%exame)
    final = float((exame+media)/2)
    if final >=5.0:
        print("Aluno aprovado.")
        print("Media final: %0.1f"%final)
    else:
        print("Aluno reprovado.")
        print("Media final: %0.1f" % final)
