class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
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

        int = 0

        for (key, value) in roman_numerals:
            while s.startswith(key):
                int += value
                s = s[len(key):]

        return int
        

if __name__ == '__main__':
    s = "III"
    print(Solution().romanToInt(s)) # 3

    s = "IV"
    print(Solution().romanToInt(s)) # 4

    s = "IX"
    print(Solution().romanToInt(s)) # 9

    s = "LVIII"
    print(Solution().romanToInt(s)) # 58

    s = "MCMXCIV"
    print(Solution().romanToInt(s)) # 1994

    s = "MMMDCCXLIX"
    print(Solution().romanToInt(s)) # 3749