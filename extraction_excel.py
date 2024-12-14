import pandas as pd


fichiers = [f"donnees_arbre{i}.xlsx" for i in range(4, 21)]


valeurs = []

for fichier in fichiers:
    try:
        
        data = pd.read_excel(fichier, header=None)
        
        valeur = data.iloc[1, 5]
        valeurs.append(valeur)
    except Exception as e:
        print(f"Erreur avec le fichier {fichier}: {e}")
        valeurs.append(None)  


import matplotlib.pyplot as plt
x=[n for n in range(4,21)]
#y_theorique = [(1/50000000)*((n**3)*(2**n)) for n in range(4,21)]
#y_theorique_MIS = [5*(1.2**n) for n in range(4, 21)]

plt.plot(x, valeurs, marker='o', linestyle='-', color='b', label="valeurs pratiques")  
#plt.plot(x, y_theorique, marker='o', linestyle='-', color='r', label="valeurs theoriques")  
#plt.plot(x, y_theorique_MIS, marker='o', linestyle='-', color='g', label="valeurs du MIS")


plt.xlabel("nombres de noeuds")
plt.ylabel("temps (en s)")
plt.title("complexité")
plt.legend()    
plt.grid(True)  
plt.show()      
