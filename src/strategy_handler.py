class FrenchNumberConverter:
    def __init__(self):
        self.strategies = {
            0: "zéro",
            1: "un",
            2: "deux",
            3: "trois",
            4: "quatre",
            5: "cinq",
            6: "six",
            7: "sept",
            8: "huit",
            9: "neuf",
            10: "dix",
            11: "onze",
            12: "douze",
            13: "treize",
            14: "quatorze",
            15: "quinze",
            16: "seize",
            20: "vingt",
            30: "trente",
            40: "quarante",
            50: "cinquante",
            60: "soixante",
            70: "soixante-dix",
            80: "quatre-vingt",
            90: "quatre-vingt-dix",
            100: "cent",
            1000: "mille",
            1000000: "million",
        }

    def conversion_strategy(self, number):
        """_summary_

        Args:
            number (_type_): _description_

        Returns:
            _type_: _description_
        """

        if number in self.strategies:
            return self.strategies[number]
        if number < 20:
            return self.handle_less_20(number)
        if number < 100:
            return self._convert_less_than_hundreds(number)
        if number < 1000:
            return self._convert_less_than_thousands(number)
        if number < 1000000:
            return self._convert_thousands_less_than_millions(number)

    def handle_less_20(self, number):
        if number in self.strategies:
            return self.strategies[number]
        tens = number // 10 * 10
        ones = number % 10
        final_digits = f"{self.strategies[tens]}-{self.strategies[ones]}"
        return final_digits

    def _convert_less_than_hundreds(self, number):
        if number in [21, 41, 51, 61]:
            tens = number // 10 * 10
            ones = number % 10
            if ones == 1:
                return f"{self.strategies[tens]}-et-{self.strategies[ones]}"
        if number < 70 or (80 <= number < 90):
            tens = number // 10 * 10
            ones = number % 10
            if ones == 0:
                return self.strategies[number]
            return f"{self.strategies[tens]}-{self.strategies[ones]}"
        elif number < 80:  # 70-79
            remainder = number - 70
            if remainder == 1:
                res = "soixante-et-" + self.strategies[10 + remainder]
            else:
                res = "soixante-" + self.strategies[10 + remainder]
            return res
        elif number < 99 or (90 < number <= 99):  # 90-99
            new_number = number - 80
            return f"{self.strategies[80]}-{self.handle_less_20(new_number)}"

    def _convert_less_than_thousands(self, number):
        hundreds = number // 100
        remainder = number % 100

        if hundreds == 1:
            hundred_text = "cent"
        else:
            hundred_text = f"{self.conversion_strategy(hundreds)} cents"
        if remainder == 0:
            return hundred_text
        else:
            return f"{hundred_text} {self.conversion_strategy(remainder)}"

    def _convert_thousands_less_than_millions(self, number):
        thousands = number // 1000
        remainder = number % 1000
        if thousands == 1:
            thousand_text = "mille"
        else:
            thousand_text = f"{self.conversion_strategy(thousands)} milles"
        if remainder == 0:
            return thousand_text
        else:
            return f"{thousand_text} {self.conversion_strategy(remainder)}"
