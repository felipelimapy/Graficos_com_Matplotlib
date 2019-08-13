import matplotlib.pyplot as plt


municipios=['Manaus', 'Tefé','Maués','Coari','PF', 'Iranduba']

media_pH=[7.5, 8, 5.6 , 6, 9.8, 1.2]

plt.plot(municipios, media_pH, label='pontos', color="green", marker='o')

plt.xticks(municipios)
plt.ylabel("pH no solo")
plt.xlabel("média do pH do solo")
plt.title("pH no solo de Presidente Figueiredo\n")
plt.show()
