#import numpy as np
import matplotlib.pyplot as plt

anuidade=['2009', '2010','2011','2012','2013', '2014', '2015', '2016', '2017', '2018']

pH=[7, 8, 6.1, 6, 8, 6, 6.3 ,5, 5.9, 4.6]
n=(7+8+6.1+6+8+6+6.3+5+5.9+4.6)/10
plt.plot(anuidade, pH, color="green", marker='.')
plt.xticks(anuidade)
plt.ylabel("pH no solo")
plt.xlabel("anos decorrentes")
plt.title("pH no solo de Presidente Figueiredo\n")
plt.show()
print ("\n")
print ("A média do pH do solo é de", n)
print ("\n")
print ("Com moda de x ")
print ("")
#NÃO FOI FEITO COM DADOS VERIDICOS