import matplotlib.pyplot as plt

Arroz = float(8500*(25-15)) - (500*(15))
Feijao = float(6200*(14-8)) - (300*(8)) 
Carne_Bovina = float(4000*(40-25)) - (400*(25))
Leite = float(7000*(6-3)) - (600*(3))
Frutas = float(9000*(5-2)) - (1200*(2))

print(f"Lucro em Arroz - R${Arroz}")
print(f"Lucro em Feijão - R${Feijao}")
print(f"Lucro em Carne Bovina - R${Carne_Bovina}")
print(f"Lucro em Leite - R${Leite}")
print(f"Lucro em Frutas - R${Frutas}")

Arroz_p = float(500*15)
Feijao_p = float(300*8) 
Carne_Bovina_p = float(400*25)
Leite_p = float(600*3) 
Frutas_p = float(1200*2)

produtos = ['Arroz', 'Feijão', 'Carne Bovina', 'Leite', 'Frutas']
valores_perdidos = [Arroz_p, Feijao_p, Carne_Bovina_p, Leite_p, Frutas_p]
cores = ['#f4a582', '#92c5de', '#ca0020', '#0571b0', '#f7f7f7']

maior_perda = max(valores_perdidos)
indice_maior = valores_perdidos.index(maior_perda)
produto_mais_perdido = produtos[indice_maior]

print(f"Produto com maior perda: {produto_mais_perdido}, com R${maior_perda:.2f} perdidos.")

explode = [0.1 if i == indice_maior else 0 for i in range(len(produtos))]

plt.figure(figsize=(8, 6))
plt.pie(valores_perdidos, labels=produtos, autopct='%1.1f%%', startangle=140,
        colors=cores, explode=explode, shadow=True)
plt.title('Participação das Perdas por Produto (em R$)')
plt.axis('equal')
plt.show()