class Hamming:
    def distance(self, a, b):
        result = 0
        if len(a) != len(b):
            raise ValueError("Podane genotypy maja rozne dlugosci")
        else:
            for i in range(0, len(a)):
                if a[i] != b[i]:
                    result += 1
            return result