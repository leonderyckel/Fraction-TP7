class Fraction:
    def __init__(self, numerateur: int, denominateur: int):
        """Construit la fraction avec un numérateur et dénominateur

               PRE : le numérateur int, et le dénominateur int
               POST : construit la fraction, de numerateur et denominateur indiqué en parametre, si le dénominateur est négatif,
                      on passe le - au numérateur et si le numérateur et le dénominateur sont négatifs les 2 deviennent positifs.
                      le self.__num et le self.__den sont privés et ne sont pas modifiable en dehors de la classe (encapsulation)
               RAISES : ZeroDivisionError si le denominateur est nul, TypeError si un élément n'est pas un int

        """
        if denominateur == 0:
            raise ZeroDivisionError("Le dénominateur ne peut pas être 0.")
        if not isinstance(numerateur, int) or not isinstance(denominateur, int):
            raise TypeError("Le numérateur et le dénominateur doivent être des entiers.")
        if denominateur < 0:
            numerateur = -numerateur
            denominateur = -denominateur

        if numerateur < 0 and denominateur < 0:
            numerateur = abs(numerateur)
            denominateur = abs(denominateur)

        self.__numerateur = numerateur
        self.__denominateur = denominateur
        self._simplify()

    def __add__(self, other: 'Fraction') -> 'Fraction':
        """
        Effectue la somme de deux fractions. Surcharge de l'opérateur + pour les fractions

        Pre: self, la fraction. other, l'autre fraction à ajouter.
        Post: retourne un object de la classe Fraction egale à la somme des deux fractions
        """
        self._validate_fraction(other)
        num = self.__numerateur * other.__denominateur + other.__numerateur * self.__denominateur
        den = self.__denominateur * other.__denominateur
        return Fraction(num, den)

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        """
        Effectue la soustraction de deux fractions.Surcharge de l'opérateur - pour les fractions.

        Pre: self, la fraction. other, l'autre fraction à soustraire
        Post:  retourne un object de la classe Fraction egale à la différence des deux fractions
        """
        self._validate_fraction(other)
        num = self.__numerateur * other.__denominateur - other.__numerateur * self.__denominateur
        den = self.__denominateur * other.__denominateur
        return Fraction(num, den)

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        """
        Effectue la multiplication de deux fractions.Surcharge de l'opérateur * pour les fractions.

        Pre: self, la fraction. other, l'autre fraction à multiplier
        Post:  retourne un object de la classe Fraction egale à la multiplication des deux fractions
        """
        self._validate_fraction(other)
        num = self.__numerateur * other.__numerateur
        den = self.__denominateur * other.__denominateur
        return Fraction(num, den)

    def __truediv__(self, other: 'Fraction') -> 'Fraction':
        """
        Effectue la division de deux fractions.Surcharge de l'opérateur / pour les fractions.

        Pre: self, la fraction. other, le diviseur
        Post: retourne un object de la classe Fraction egale à la division des deux fractions
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
        Surcharge de l'opérateur ** pour les fractions.
        PRE :self, la fraction. Other, la fraction doit être un nombre entier positif. donc le dénominateur doit etre 1
        POST : retourne un nouveau objet Fraction egale à la puissance de la premiere par la seconde
        RAISES : ValueError si l'exposant n'est pas un entier, si l'exposant est négatif
        """
        if other.__denominateur != 1:
            raise ValueError("Le dénominateur doit etre 1.")
        if other.__numerateur < 0:
            raise ValueError("Pas d'exposant négatif possible")

        num = self.__numerateur ** other.__numerateur
        den = self.__denominateur ** other.__numerateur
        return Fraction(num, den)

    def __eq__(self, other: 'Fraction') -> bool:
        """
        Vérifie l'égalité entre les 2 fractions. Surcharge de l'opérateur == pour les fractions.
        PRE : self, la fraction. other, la fraction a comparer
        POST : retourne 'True' si les deux fractions sont égales (les mêmes)quand elles sont simplifiées,
        sinon retourne 'False'.
        """
        self._validate_fraction(other)

        num1 = self.__numerateur * other.__denominateur
        num2 = other.__numerateur * self.__denominateur
        return num1 == num2

    def __float__(self):
        """
         Renvoie la valeur décimale de la fraction. Surcharge de la méthode __float__

         PRE : self, La fraction
         POST : retourne La valeur décimale de cette fraction
        """
        return self.__numerateur / self.__denominateur

    def is_zero(self):
        """
        Vérifier si la valeur d'une fraction est 0

        PRE : self, La fraction
        POST : retourne 'True' si la fraction est égale à zero, sinon renvoi 'False'
        """
        return self.__numerateur == 0

    def is_integer(self):
        """
        Vérifie si une fraction est un entier

        PRE : self, La fraction
        POST : retourne 'True' si la fraction est un entier, sinon renvoi 'False'
        """
        return self.__numerateur % self.__denominateur == 0

    def is_proper(self):
        """
        Vérifie si la valeur absolue de la fraction est < 1

        PRE : self, La fraction
        POST : retourne True si la fraction est propre, False sinon
                """
        return abs(self.__numerateur) < abs(self.__denominateur)

    def is_unit(self):
        """
        Vérifie si le numérateur d'une fraction est 1 sous sa forme réduite

        PRE : self, La fraction
        POST : retourne 'True' si le numérateur est 1, sinon renvoi 'False'
               """
        gcd_value = self._gcd(self.__numerateur, self.__denominateur)
        return self.__numerateur // gcd_value == 1

    def is_adjacent_to(self, other):
        """
            Vérifier si deux fractions diffèrent d'une fraction unitaire

            Deux fractions sont adjacentes si la valeur absolue de leur différence est une fraction unitaire

            PRE : self, La fraction other, l'autre fraction
            POST : retourne 'True' si les deux fraction diffèrent d'une fraction unitaire, sinon retourne 'False'
        """
        self._validate_fraction(other)
        num = (self.__numerateur * other.__denominateur) - (other.__numerateur * self.__denominateur)
        den = (self.__denominateur * other.__denominateur)
        gcd_value = self._gcd(num, den)
        return abs(num // gcd_value) == 1

    def as_mixed_number(self):
        """
            Renvoie la forme réduite de la fraction sous la forme d'un nombre fractionnaire
            Un nombre fractionnaire est la somme d'un entier et d'une fraction propre

            PRE : self, la fraction
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

         Pre: le numérateur int et le dénominateur int de la fraction
         Post: renvoie a, le GCD de a et b
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
         Raise: si other n'est pas une instance de la classe fraction
        """
        if not isinstance(other, Fraction):
            raise TypeError("L'opérateur doit être une instance de Fraction.")

    def _simplify(self):
        """
        Simplifie la fraction.

        PRE : self, La fraction de numérateur et dénominateur
        POST : Modifie cette fraction, simplifiée au maximum.
        """
        gcd_value = self._gcd(self.__numerateur, self.__denominateur)
        self.__numerateur //= gcd_value
        self.__denominateur //= gcd_value

    def __str__(self) -> str:
        """
        Affiche (print)la fraction sous forme de chaîne de caractères. Surcharge de la méthode __str__ python

        Pre: self, la fraction
        Post: renvoi str, représentation textuelle de la fraction
        """
        return f"{self.__numerateur}/{self.__denominateur}" if self.__denominateur != 1 else str(self.__numerateur)

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
