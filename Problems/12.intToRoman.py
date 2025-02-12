class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 1:
            return ''

        # create a dictionary to store the roman numeral values
        roman_numerals = [
            ('M', 1000),
            ('CM', 900),
            ('D', 500),
            ('CD', 400),
            ('C', 100),
            ('XC', 90),
            ('L', 50),
            ('XL', 40),
            ('X', 10),
            ('IX', 9),
            ('V', 5),
            ('IV', 4),
            ('I', 1)
        ]

        roman_literal = ''

        for (key, value) in roman_numerals:
            if num == 0:
                break
            if num < value:
                continue

            count = num // value
            roman_literal += key * count
            num -= value * count

        return roman_literal


if __name__ == '__main__':
    num = 3
    print(Solution().intToRoman(num)) # "III"

    num = 4
    print(Solution().intToRoman(num)) # "IV"

    num = 9
    print(Solution().intToRoman(num)) # "IX"

    num = 58
    print(Solution().intToRoman(num)) # "LVIII"

    num = 1994
    print(Solution().intToRoman(num)) # "MCMXCIV"

    num = 3749
    print(Solution().intToRoman(num)) # "MMMDCCXLIX"