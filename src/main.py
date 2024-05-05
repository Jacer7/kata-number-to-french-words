from strategy_handler import FrenchNumberConverter


class HandleSingularPlural(FrenchNumberConverter):
    def mask_items(self, number):
        words = self.conversion_strategy(number).split(" ")
        while "cents" in words and words.index("cents") != len(words) - 1:
            index_cents = words.index("cents")
            words[index_cents] = "cent"
        while "milles" in words and words.index("milles") != len(words) - 1:
            index_milles = words.index("milles")
            words[index_milles] = "mille"
        return " ".join(words)


if __name__ == "__main__":
    converter = HandleSingularPlural()
    test_cases = [0, 1, 5, 10, 11, 15, 20, 21, 30, 35, 50, 51, 68, 70, 75, 99, 100, 101, 105, 111, 123, 168, 171, 175, 199, 200, 201, 555, 999, 1000, 1001, 1111, 1199, 1234, 1999, 2000, 2001, 2020, 2021, 2345, 9999, 10000, 11111, 12345, 123456, 654321, 999999]
    for number in test_cases:
        print(f"{number}: {converter.mask_items(number)}")
