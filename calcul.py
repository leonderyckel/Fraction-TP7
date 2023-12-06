class Fraction:
    def __init__(self, numerateur: int, denominateur: int):
        """Construit la fraction avec un numérateur et dénominateur

               PRE : 'num' int, 'den' int
               POST : construit la fraction, de numerateur et denominateur indiqué en parametre
               RAISES : ZeroDivisionError si le denominateur est nul, TypeError si un élément n'est pas un int

        """
        if denominateur == 0:
            raise ZeroDivisionError("Le dénominateur ne peut pas être 0.")
        if not isinstance(numerateur, int) or not isinstance(denominateur, int):
            raise TypeError("Le numérateur et le dénominateur doivent être des entiers.")
        if denominateur < 0:
            numerateur = -numerateur
            denominateur = -denominateur

        self.__numerateur = numerateur
        self.__denominateur = denominateur
        self._simplify()

    @property
    def numerateur(self):
        """
        Getter pour le numérateur
        PRE:/
        POST : Renvoie le numérateur de la fraction

        """
        return self.__numerateur

    @property
    def denominateur(self):
        """
        Getter pour le dénominateur
        PRE:/
        POST : Renvoie le dénominateur de la fraction

        """
        return self.__denominateur

    def __add__(self, other: 'Fraction') -> 'Fraction':
        """
        Effectue la somme de deux fractions. Surcharge du + pour les fractions

        Pre: other, l'autre fraction à ajouter
        Post: retourne une nouvelle Fraction egale à la somme des deux fractions
        """
        self._validate_fraction(other)
        num = self.__numerateur * other.__denominateur + other.__numerateur * self.__denominateur
        den = self.__denominateur * other.__denominateur
        return Fraction(num, den)

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        """
        Effectue la soustraction de deux fractions.Surcharge du - pour les fractions.

        Pre: other, l'autre fraction à soustraire
        Post:  retourne une nouvelle Fraction egale à la différence des deux fractions
        """
        self._validate_fraction(other)
        num = self.__numerateur * other.__denominateur - other.__numerateur * self.__denominateur
        den = self.__denominateur * other.__denominateur
        return Fraction(num, den)

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        """
        Effectue la multiplication de deux fractions.Surcharge du * pour les fractions.

        Pre: other, l'autre fraction à multiplier
        Post:  retourne une nouvelle Fraction egale à la multiplication des deux fractions
        """
        self._validate_fraction(other)
        num = self.__numerateur * other.__numerateur
        den = self.__denominateur * other.__denominateur
        return Fraction(num, den)

    def __truediv__(self, other: 'Fraction') -> 'Fraction':
        """
        Effectue la division de deux fractions.Surcharge du / pour les fractions.

        Pre: other, le diviseur
        Post:  retourne une nouvelle Fraction egale à la division des deux fractions
        Raises: ZeroDivisionError si le numerateur de other (le diviseur) vaut 0
        """
        self._validate_fraction(other)
        num = self.__numerateur * other.__denominateur
        den = self.__denominateur * other.__numerateur

        if den == 0:
            raise ZeroDivisionError("Division par zéro.")
        return Fraction(num, den)

    def __pow__(self, other: 'Fraction') -> 'Fraction':
        """
        Effectue la puissance de la premiere fraction avec le numérateur de la seconde
        Surcharge du ** pour les fractions.
        PRE : Other,  l'exposant doit être un nombre entier donc le dénominateur doit  etre 1
        POST : retourne un nouveau objet Fraction egale à la puissance de la premiere par la seconde
        RAISES : ValueError si l'exposant n'est pas un entier.
        """
        if other.denominateur != 1:
            raise ValueError("Le dénominateur doit etre 1.")
        num = self.__numerateur ** other.__numerateur
        den = self.__denominateur ** other.__numerateur
        return Fraction(num, den)

    def __eq__(self, other: 'Fraction') -> bool:
        """
        Vérifie l'égalité entre les 2 fractions. Surcharge du == pour les fractions.
        PRE : other, la fraction a comparer
        POST : retourne 'True' si les deux fractions sont égales (les mêmes)quand elles sont simplifiées, sinon retourne 'False'.
        """
        self._validate_fraction(other)

        num1 = self.__numerateur * other.__denominateur
        num2 = other.__numerateur * self.__denominateur
        return num1 == num2

    def __float__(self):
        """
         Renvoie la valeur décimale de la fraction

         PRE : La fraction résultante de l'opération faite par l'utilisateur
         POST : retourne La valeur décimale de cette fraction
        """
        return self.__numerateur / self.__denominateur

    def is_zero(self):
        """
        Vérifier si la valeur d'une fraction est 0

        PRE : La fraction résultante de l'opération faite par l'utilisateur
        POST : retourne 'True' si la fraction est égale à zero, sinon renvoi 'False'
        """
        return self.__numerateur == 0

    def is_integer(self):
        """
        Vérifie si une fraction est un entier

        PRE : La fraction résultante de l'opération faite par l'utilisateur
        POST : retourne 'True' si la fraction est un entier, sinon renvoi 'False'
        """
        return self.__numerateur % self.__denominateur == 0

    def is_proper(self):
        """
        Vérifie si la valeur absolue de la fraction est < 1

        PRE : La fraction résultante de l'opération faite par l'utilisateur
        POST : retourne True si la fraction est propre, False sinon
                """
        return abs(self.__numerateur) < abs(self.__denominateur)

    def is_unit(self):
        """
        Vérifie si le numérateur d'une fraction est 1 sous sa forme réduite

        PRE : La fraction résultante de l'opération faite par l'utilisateur
        POST : retourne 'True' si le numérateur est 1, sinon renvoi 'False'
               """
        gcd_value = self._gcd(self.__numerateur, self.__denominateur)
        return self.__numerateur // gcd_value == 1

    def is_adjacent_to(self, other):
        """
            Vérifier si deux fractions diffèrent d'une fraction unitaire

            Deux fractions sont adjacentes si la valeur absolue de leur différence est une fraction unitaire

            PRE : La fraction utiliser doit être un objet fraction.
            POST : retourne 'True' si les deux fraction diffèrent d'une fraction unitaire, sinon retourne 'False'
        """

        num = (self.__numerateur * other.__denominateur) - (other.__numerateur * self.__denominateur)
        den = (self.__denominateur * other.__denominateur)
        gcd_value = self._gcd(num, den)
        return abs(num // gcd_value) == 1

    def as_mixed_number(self):
        """
            Renvoie la forme réduite de la fraction sous la forme d'un nombre fractionnaire
            Un nombre fractionnaire est la somme d'un entier et d'une fraction propre

            PRE : La fraction résultante de l'opération faite par l'utilisateur
            POST :Retourne un string de la fraction sous la forme d'un nombre entier et d'une fraction
                """

        entier = self.__numerateur // self.__denominateur
        reste = self.__numerateur % self.__denominateur

        if reste == 0:
            return str(entier)

        elif entier != 0:
            return f"{entier} et {reste}/{self.__denominateur}"

        else:
            return f"{self.__numerateur}/{self.__denominateur}"

    @staticmethod
    def _gcd(a: int, b: int) -> int:
        """
        Calcule le plus grand diviseur commun (GCD) de deux entiers.

         Pre: int, premier nombre, int, deuxième nombre
         Post: int, le GCD de a et b
        """
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def _validate_fraction(other: 'Fraction'):
        """
        Valide la fraction other.

         Pre: Other, la fraction à valider
         Post: /
        """
        if not isinstance(other, Fraction):
            raise TypeError("L'opérateur doit être une instance de Fraction.")

    def _simplify(self):
        """
        Simplifie la fraction.

        PRE : La fraction sous la forme entrée par l'utilisateur.
        POST : Modifie cette même fraction simplifiée au maximum.
        """
        gcd_value = self._gcd(self.__numerateur, self.__denominateur)
        self.__numerateur //= gcd_value
        self.__denominateur //= gcd_value

    def __str__(self) -> str:
        """
        Affiche la fraction sous forme de chaîne de caractères.

        Post: renvoi str, représentation textuelle de la fraction
        """
        return f"{self.__numerateur}/{self.__denominateur}" if self.__denominateur != 1 else str(self.__numerateur)
