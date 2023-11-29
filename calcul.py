from simplifier import Simplifier


class Calcul(Simplifier):
    def __init__(self):
        self.total = 0

    @staticmethod
    def fract_to_tuple(frac_ent: str) -> tuple:
        """
        Méthode qui convertit une fraction stringifiée en tuple.
        En effet, lors de la déclaration de la fraction dans le main, on recoit des strings, et donc,
        les num et den ne sont pas des integer et aucune operation n'est alors possible.
        C'est donc à ca que sert cette méthode, formater une fraction en tuple tout en changant le type des chiffres en int.
        On en profite aussi pour convertir les entiers comme 5 en fraction (5, 1) pour avoir un format standard.

        Pre: fraction ou entier de type string
        Post: tuple de la fraction ou les nums et dens sont de type int.
        """
        if "/" in frac_ent:
            num = int(frac_ent.split("/")[0].strip())
            den = int(frac_ent.split("/")[1].strip())
            return num, den
        else:
            return int(frac_ent.strip()), 1

    def somme(self, frac_1: tuple, frac_2: tuple) -> tuple:
        """
        Effectue un somme de 2 tuples (fractions).
        La seule particularitée de cette méthode est que si les dens sont identiques, on ne fait que la somme des numerateurs
        sinon on multiplie les den entre eux tout en multipliant les numerateurs avec leur denominateurs
        Une fois fini, on simplifie le résultat si simplifiable.


        Pre: La fraction attendue doit être de type tuple, et le contenu des tuples doivent être des integers
        Post: Renvoie la fraction sous forme de tuple. Garantie que la fraction est simplifiée a son maximum
        """
        num1, num2 = frac_1[0], frac_2[0]
        den1, den2 = frac_1[1], frac_2[1]
        if den1 == den2:
            num = num1 + num2
            den = den1
        else:
            num = (num1 * den2) + (num2 * den1)
            den = den1 * den2

        self.total = self.simplifier_values(fraction=(num, den))
        return self.total

    def soustraction(self, frac_1: tuple, frac_2: tuple) -> tuple:
        """
        Effectue un soustraction de 2 tuples (fractions).
        Une fois fini, on simplifie le résultat si simplifiable.

        Pre: La fraction attendue doit être de type tuple, et le contenu des tuples doivent être des integers
        Post: Renvoie la fraction sous forme de tuple. Garantie que la fraction est simplifiée a son maximum
        """
        num1, num2 = frac_1[0], frac_2[0]
        den1, den2 = frac_1[1], frac_2[1]
        num = (num1 * den2) - (num2 * den1)
        den = den1 * den2

        self.total = self.simplifier_values(fraction=(num, den))
        return self.total

    def division(self, frac_1: tuple, frac_2: tuple) -> tuple:
        """
        Effectue un division de 2 tuples (fractions).
        Une fois fini, on simplifie le résultat si simplifiable.

        Pre :La fraction attendue doit être de type tuple, et le contenu des tuples doivent être des integers
        Post : Renvoie la fraction sous forme de tuple. Garantie que la fraction est simplifiée a son maximum
        """
        num1, num2 = frac_1[0], frac_2[0]
        den1, den2 = frac_1[1], frac_2[1]
        num = num1 * den2
        den = den1 * num2

        self.total = self.simplifier_values(fraction=(num, den))
        return self.total

    def multiplication(self, frac_1: tuple, frac_2: tuple) -> tuple:
        """
        Effectue un multiplication de 2 tuples (fractions).
        Une fois fini, on simplifie le résultat si simplifiable.

        Pre :La fraction attendue doit être de type tuple, et le contenu des tuples doivent être des integers
        Post : Renvoie la fraction sous forme de tuple. Garantie que la fraction est simplifiée a son maximum
        """
        num1, num2 = frac_1[0], frac_2[0]
        den1, den2 = frac_1[1], frac_2[1]
        num = num1 * num2
        den = den1 * den2

        self.total = self.simplifier_values(fraction=(num, den))
        return self.total
