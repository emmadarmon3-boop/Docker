# hello.py
import os

print("Coucou ! GitHub Actions a lancé mon script Python.")
# On peut même afficher une variable pour faire "pro"
name = os.getenv("USER_NAME", "Inconnu")
print(f"Bravo {name}, ton automatisation fonctionne !")