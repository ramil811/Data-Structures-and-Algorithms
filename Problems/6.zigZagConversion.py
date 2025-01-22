from pprint import pprint

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # check if the number of rows is greater than or equal to the length of the string
        if numRows >= len(s) or numRows == 1:
            return s
        
        # create a list to store the rows
        rows = [''] * numRows

        # initialize the current row and direction
        currentRow = 0
        direction = 1

        # iterate through the string
        for char in s:
            print(currentRow, direction)
            # add the character to the current row
            rows[currentRow] += char

            # update the current row
            currentRow += direction

            # check if the current row is at the top or bottom
            if currentRow == 0 or currentRow == numRows - 1:
                # change the direction
                direction *= -1
            
            print(rows)

        return ''.join(rows)


if __name__ == '__main__':
    # create the string
    s = "PAYPALISHIRING"
    numRows = 3
    print(Solution().convert(s, numRows))

    numRows = 4
    print(Solution().convert(s, numRows))