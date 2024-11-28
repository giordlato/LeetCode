class Solution:
    def romanToInt(self, s: str) -> int:
        traduzione = 0
        i = 0
        while(i < len(s)):
            a = s[i]
            if i < len(s)-1:
                b = s[i+1]
            else:
                b = 'Tiè'
            if a == 'I':
                if b == 'V':
                    traduzione = traduzione + 4
                    i += 1
                elif b == 'X':
                    traduzione = traduzione + 9
                    i += 1
                else:
                    traduzione = traduzione + 1
            elif a == 'V':
                traduzione = traduzione + 5
            elif a == 'X':
                if b == 'L':
                    traduzione = traduzione + 40
                    i += 1
                elif b == 'C':
                    traduzione = traduzione + 90
                    i += 1
                else:
                    traduzione = traduzione + 10
            elif a == 'L':
                traduzione = traduzione + 50
            elif a == 'C':
                if b == 'D':
                    traduzione = traduzione + 400
                    i += 1
                elif b == 'M':
                    traduzione = traduzione + 900
                    i += 1
                else:
                   traduzione = traduzione + 100
            elif a == 'D':
                traduzione = traduzione + 500
            elif a == 'M':
                traduzione = traduzione + 1000
            i += 1
        return traduzione