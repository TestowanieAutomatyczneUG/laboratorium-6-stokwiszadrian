def roman(n):
    result = ""
    n_roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    n_arabic = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    while n > 0:
        for i in range(len(n_arabic)):
            result += n_roman[i]*int((n/n_arabic[i]))
            n %= n_arabic[i]
    return result
