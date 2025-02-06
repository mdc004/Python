import numpy as np

# Dati forniti
ore_studio = np.array([6, 14, 3, 22, 9, 11, 12, 5, 18, 24, 15, 17])
punteggio_gpa = np.array([2.8, 3.2, 3.1, 3.6, 3.0, 3.3, 3.4, 2.7, 3.1, 3.8, 3.0, 3.9])

# Calcolo del coefficiente di correlazione di Pearson
correlazione = np.corrcoef(ore_studio, punteggio_gpa)[0, 1]
print(correlazione)
