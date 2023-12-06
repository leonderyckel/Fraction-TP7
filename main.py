from calcul import Fraction
from os import system
from platform import system as platform_system


def commande(string: str) -> str:
    return input(f"\n -> {string} > ")


def fract_to_tuple(frac_ent: str) -> tuple:
    try:
        if "/" in frac_ent:
            num, den = map(int, frac_ent.split("/"))
            return num, den
        else:
            return int(frac_ent), 1
    except ValueError:
        raise ValueError("La fraction doit être composée de nombres entiers.")


def clear():
    if platform_system() in ['Darwin', 'Linux']:
        system("clear")
    else:
        system("cls")


if __name__ == "__main__":
    first_help = True
    while True:
        if first_help:
            print(
                "+------------------------------------------------------------------------------------+\n"
                "|  Bienvenue dans le mode interactif de la calculette. Tapez !h pour plus d'aide...  |\n"
                "+------------------------------------------------------------------------------------+\n"
            )
            first_help = False
        command = commande(string="Entrez une commande:")
        if command == "!h" or command == "":
            print("\n+------------------------------------------------------+\n"
                  "|                        Aide                          |\n"
                  "+------------------------------------------------------+\n"
                  "|  !h                ->   Mode aide                    |\n"
                  "|  !q                ->   Quitter le mode calculette   |\n"
                  "|  !c                ->   Faire un calcul simple       |\n"
                  "+------------------------------------------------------+\n"
                  )
            continue
        elif command == "!q":
            print("Merci d'avoir utilisé cette super calculatrice du tonnerre !")
            break

        elif command == "!c":

            try:

                fraction_une = Fraction(*fract_to_tuple(commande(string="Entrez votre première fraction")))

                fraction_deux = Fraction(*fract_to_tuple(commande(string="Entrez votre seconde fraction")))

                operateur = commande(string="Quelle opération voulez-vous effectuer [+ - * / ** ==]").strip()

                if operateur == '+':

                    result = fraction_une + fraction_deux

                elif operateur == '-':

                    result = fraction_une - fraction_deux

                elif operateur == '*':

                    result = fraction_une * fraction_deux

                elif operateur == '/':

                    result = fraction_une / fraction_deux

                elif operateur == '**':

                    result = fraction_une ** fraction_deux

                elif operateur == '==':
                    result = fraction_une == fraction_deux
                    print(f"\nLe résultat de l'opération est: {result}")
                    continue

                else:

                    raise ValueError("Opérateur non valide.")

                print(f"\nLe résultat de l'opération est: {result}")
                print(f"Valeur décimale (float): {float(result)}")
                print(f"Sous forme de nombre fractionnaire (mixed_number): {result.as_mixed_number()}")

                if result.is_zero():
                    print("Le résultat est zéro (is_zero)")
                if result.is_integer():
                    print("Le résultat est un entier (is_integer)")
                if result.is_proper():
                    print("Le résultat est une fraction propre (is_proper)")
                if result.is_unit():
                    print("Le numérateur vaut 1 (is_unit)")
                if result.is_adjacent_to(fraction_deux):
                    print("Les fractions sont adjacente (is_adjacent_to)")

            except ValueError as e:
                print(f"Erreur: {e}")
            except Exception as e:
                print(f"Une erreur inattendue est survenue: {e}")

        else:
            print(f"ERREUR: {command} n'est pas une instruction connue...")
