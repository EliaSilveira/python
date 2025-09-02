import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
Musicas = ('Die With A Smile', 'DtMF', 'BIRDS OS A FEATHER', 'APT', 'BAILE INoLVIDABLE')
Indice = np.arange(len(Musicas))
Acessos_por_Milhões=[67749436, 56046762, 55010564, 45616277, 39763363]
plt.bar(Indice, Acessos_por_Milhões)
plt.xticks(Indice, Musicas)
plt.ylabel('Acessos Por Milhões')
plt.title('Ranking do Spotify do dia 31 de Janeiro a 06 de Fevereiro 2025')
plt.show()