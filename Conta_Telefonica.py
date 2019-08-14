#import numpy as np
import matplotlib.pyplot as plt

meses=['Janeiro', 'Fevereiro', 'Março','Abril','Maio', 'Junho', 'Julho','Agosto',
       'Setembro','Outubro', 'Novembro', 'Dezembro']
conta_telefonica=[48,45.99,50.91,10.62,23.90,11.15,65.29,15.60,36.70,29.90,49.84,55.90]
valor_total=(48+45.99+50.91+10.62+23.90+11.15+65.29+15.60+36.70+29.90+49.84+55.90)/12
plt.plot(meses, conta_telefonica, label='pontos', color='red')

plt.grid(True)
plt.xticks(meses)
plt.ylabel("valores da conta")
plt.xlabel("\nmeses de 2014")
plt.title("Gráfico Representativo do Gasto na Conta Telefonica\n", color='Green')


print ("Em média, você gastou {} reais em conta telefonica durante o ano de 2014".format(valor_total))
plt.show()
