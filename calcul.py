class Fraction:
    def __init__(self, numerateur: int, denominateur: int):
        """Construit la fraction avec un numérateur et dénominateur

               PRE : 'num' entier, 'den' est un entier
               POST : crée une fraction
               RAISES : Erreur si denominateur est nul, si un élément n'est pas un int
        """
        if denominateur == 0:
            raise ValueError("Le dénominateur ne peut pas être 0.")
        if not isinstance(numerateur, int) or not isinstance(denominateur, int):
            raise TypeError("Le numérateur et le dénominateur doivent être des entiers.")
        self.numerateur = numerateur
        self.denominateur = denominateur

    def __add__(self, other: 'Fraction') -> 'Fraction':
        """
        Effectue la somme de deux fractions.

        Pre: Fraction, l'autre fraction à ajouter
        Post: Fraction, la somme des deux fractions
        """
        self._validate_fraction(other)
        num = self.numerateur * other.denominateur + other.numerateur * self.denominateur
        den = self.denominateur * other.denominateur
        return Fraction(num, den)._simplify()

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        """
        Effectue la soustraction de deux fractions.

        Pre: Fraction, l'autre fraction à soustraire
        Post: Fraction, la différence des deux fractions
        """
        self._validate_fraction(other)
        num = self.numerateur * other.denominateur - other.numerateur * self.denominateur
        den = self.denominateur * other.denominateur
        return Fraction(num, den)._simplify()

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        """
        Effectue la multiplication de deux fractions.

        Pre: Fraction, l'autre fraction à multiplier
        Post: Fraction, le produit des deux fractions
        """
        self._validate_fraction(other)
        num = self.numerateur * other.numerateur
        den = self.denominateur * other.denominateur
        return Fraction(num, den)._simplify()

    def __truediv__(self, other: 'Fraction') -> 'Fraction':
        """
        Effectue la division de deux fractions.

        Pre: Fraction, le diviseur
        Post: Fraction, le quotient des deux fractions
        Raises: le diviseur ne peut pas etre egale à 0
        """
        self._validate_fraction(other)
        num = self.numerateur * other.denominateur
        den = self.denominateur * other.numerateur
        if den == 0:
            raise ValueError("Division par zéro.")
        return Fraction(num, den)._simplify()

    def _simplify(self) -> 'Fraction':
        """
        Simplifie la fraction.
        """
        gcd_value = self._gcd(self.numerateur, self.denominateur)
        self.numerateur //= gcd_value
        self.denominateur //= gcd_value
        return self

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

    def _validate_fraction(self, other: 'Fraction'):
        """
        Valide une fraction.

         Pre: Fraction, la fraction à valider
        """
        if not isinstance(other, Fraction):
            raise TypeError("L'opérateur doit être une instance de Fraction.")
        if other.denominateur == 0:
            raise ValueError("Le dénominateur de la fraction ne peut pas être 0.")

    def __str__(self) -> str:
        """
        Affiche la fraction sous forme de chaîne de caractères.

        Post: str, représentation textuelle de la fraction
        """
        return f"{self.numerateur}/{self.denominateur}" if self.denominateur != 1 else str(self.numerateur)
