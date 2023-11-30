class Simplifier:
    def check_erreur(self, fract: tuple, operateur: str) -> int:
        """
        Cette méthode renverra un int:
         - 0 si tout est OK
         - juste un raise si ERREUR
        Dans les 3/4 des cas possibles, votre opération initiale sera juste annulée !


        raise: Si le den = 0, Si le num et le den sont pas des int, Si le den = 1 et le num 0 et que l'operateur est dans [/]
        Pre : La fraction attendue doit être de type tuple, et le contenu des tuples doivent être des integers.
        Post: 0 si tout est passé au niveau des tests
        """
        # Dénominateur à 0
        if fract[1] == 0:
            raise ValueError("Attention, votre fraction ne peut pas contenir 0 en dénominateur !")

        # Si fraction contient des valeurs qui ne sont pas des chiffres
        if type(fract[0]) is int and type(fract[1]) is int:
            raise ValueError("Attention, vos fraction ne sont pas composées de nombres !")

        # Si den == 1 et num == 0 et que c'est des operateur * et /:
        if fract[1] == 1 and fract[0] == 0 and operateur in ["/"]:
            raise ValueError("Attention, vous ne pouvez pas faire de divisions avec 0 !")

        return 0

    def gcd(self, num: int, den: int) -> int:
        """
        gcd pour grand commun diviseur, fonctionne en complément de la méthode simplifier_values.
        La condition pour quitter le while est d'avoir un reste a 0.
        Dès lors que ce reste sera à 0, num et den aura alors son facteur le plus grand
        --
        Pre: Seul un integer est attendu
        Post: le facteur commun le plus grand entre le num et den
        """
        while den:
            num, den = den, num % den
        return num

    def simplifier_values(self, fraction: tuple) -> tuple:
        """
        Cette méthode permet de renvoyer un fraction sous forme de tuple la plus simplifié possible.
        Cette méthode est étroitement liée à gcd. En effet, c'est cette dernière qui fournit le facteur commun entre
        num et den.
        Pre: La fraction attendue doit être de type tuple, et le contenu des tuples doivent être des integers.
        Post: Renvoie la fraction sous forme de tuple. Garantie que la fraction est simplifiée a son maximum
        """
        num = fraction[0]
        den = fraction[1]
        facteur_com = self.gcd(num=num, den=den)
        num /= facteur_com
        den /= facteur_com
        return num, den
