# Advanced task
def get_rome_number(n:int) -> str:
    if isinstance(n, int) and n<5000:
        one = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        ten = [x.replace('X','C').replace('V','L').replace('I', 'X') for x in one]
        hund = [x.replace('X','M').replace('V','D').replace('I', 'C') for x in one]
        thous = ['M'*i for i in range(5)]
        return ''.join([
            thous[n // 1000],
            hund[n // 100 % 10],
            ten[n // 10 % 10],
            one[n % 10]
            ])
