import matplotlib.pyplot as plt; plt.rcdefaults()
musicas = 'Die With A Smile', 'DtMF', 'BIRDS OS A FEATHER', 'APT', 'BAILE INoLVIDABLE'
acessos = [67749436, 56046762, 55010564, 45616277, 39763363]
colors = ['green', 'yellow', 'turquoise', 'orange', 'khaki']
patches, text, autotexts = plt.pie(acessos, colors=colors, autopct='%1.1f%%', startangle=90)
plt.legend(patches, musicas, loc='lower right')
plt.axis('equal')
plt.title('Ranking do Spotify do dia 31 de Janeiro a 06 de Fevereiro 2025')
plt.show()