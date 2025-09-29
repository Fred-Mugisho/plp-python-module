# Devoir : Gestion des fichiers et des exceptions en Python
# Auteur : MUGISHO Frederick
# Description :
#   - Lit un fichier
#   - Écrit une version modifiée dans un nouveau fichier
#   - Gère les erreurs proprement

def lire_et_modifier_fichier(fichier_entree, fichier_sortie):
    try:
        with open(fichier_entree, "r") as f:
            contenu = f.read()

        # Modifier le contenu en majuscules
        contenu_modifie = contenu.upper()

        with open(fichier_sortie, "w") as f:
            f.write(contenu_modifie)

        print(f"✅ Fichier '{fichier_sortie}' créé avec succès.")

    except FileNotFoundError:
        print(f"❌ Erreur : le fichier '{fichier_entree}' est introuvable.")
    except PermissionError:
        print(f"❌ Erreur : permission refusée pour accéder à '{fichier_entree}'.")
    except Exception as e:
        print(f"⚠️ Erreur inattendue : {e}")


if __name__ == "__main__":
    # Demande à l’utilisateur le nom du fichier à lire
    nom_fichier = input("Entrez le nom du fichier à lire : ").strip()
    fichier_sortie = "modifie_" + nom_fichier

    lire_et_modifier_fichier(nom_fichier, fichier_sortie)
