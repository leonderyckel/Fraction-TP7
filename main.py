from simplifier import Simplifier
from calcul import Calcul
from subprocess import run


def commande(string: str) -> str:
    """
    Juste une fonction pour utiliser un prompt !
    Quoi qu'il soit écrit pour le param string, il n'y aura pas d'erreur
    Soit un None, soit ce qui a été tapé dans le string!

    **ATTENTION**: Si vous donnez des variables qui n'existent pas, uniquement dans ce cas là, il y aura un plantage !
    Mais encore une fois, il faudrait changer le nom d'une variable pour provoquer cette erreur, ce qui n'est pas prévu
    à être changé dans le code.

     Pre string: string qui sera affiché avant le >
     Post: une string dans le output
    """
    return input(f"\n{string} > ")


if __name__ == "__main__":
    calcul = Calcul()
    simple = Simplifier()
    first_help = True

    while True:
        if first_help:
            print(
                "+------------------------------------------------------------------------------------+\n"
                "|  Bienvenue dans le mode interactif de la calculette. Tapez !h pour plus d'aide...  |\n"
                "+------------------------------------------------------------------------------------+\n"
            )
            first_help = False
        command = commande(string=f"Entre une commande [{calcul.total}]")
        if command == "!h":
            print("\n+------------------------------------------------------+\n"
                  "|                        Aide                          |\n"
                  "+------------------------------------------------------+\n"
                  "|  !h                ->   Mode aide                    |\n"
                  "|  !n                ->   Nettoyer la mémoire          |\n"
                  "|  !q                ->   Quitter le mode calculette   |\n"
                  "|  !c                ->   Faire un calcul simple       |\n"
                  "+------------------------------------------------------+\n"
                  )
        elif command == "!q":
            print("Merci d'avoir utilisé cette super calculatrice du tonnerre !")
            break
        elif command == "!n":
            calcul.total = 0
            print("La mémoire a été vidée ! Vous repartez de 0 !")
        elif command == "":
            pass
        elif command == "!c":
            # Stocker en mémoire une string de la fraction et de son opérateur
            fraction_une = commande(string=f" -> Entrez la première fraction ou entier [{calcul.total}]")
            fraction_deux = commande(string=f" -> Entrez la deuxième fraction ou entier [{calcul.total}]")
            operateur = commande(string=f" -> Quelle opération voulez-vous effectuer [{calcul.total}]")

            # Simplifier les fractions et les transformer en tuple
            if fraction_une != 'Ans':
                fraction_une = simple.simplifier_values(fraction=calcul.fract_to_tuple(frac_ent=fraction_une))
            fraction_deux = simple.simplifier_values(fraction=calcul.fract_to_tuple(frac_ent=fraction_deux))

            # Vérifier que les fractions sont bien conformes
            if fraction_une != 'Ans' and simple.check_erreur(fract=fraction_une, operateur=operateur) == 1:
                continue
            if simple.check_erreur(fract=fraction_deux, operateur=operateur) == 1:
                continue

            # Faire une opération entre ces 2 fractions
            if operateur.strip() == '+':
                calcul.somme(frac_1=calcul.total if fraction_une == 'Ans' else fraction_une, frac_2=fraction_deux)
            elif operateur.strip() == '-':
                calcul.soustraction(frac_1=calcul.total if fraction_une == 'Ans' else fraction_une,
                                    frac_2=fraction_deux)
            elif operateur.strip() == '/':
                calcul.division(frac_1=calcul.total if fraction_une == 'Ans' else fraction_une, frac_2=fraction_deux)
            elif operateur.strip() == '*':
                calcul.multiplication(frac_1=calcul.total if fraction_une == 'Ans' else fraction_une,
                                      frac_2=fraction_deux)
        else:
            print(f"ERREUR: {command} n'est pas une instruction connue...")
