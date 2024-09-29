vendas01 = [120, 150, 170, 130, 200, 250, 180, 220, 210, 160, 140, 190]
vendas02 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
vendas03 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]


# The param type and return are just for pylance STFU
def analise_vendas(vendas: list[int]) -> str:
    total_vendas = sum(vendas)
    media_vendas = total_vendas / len(vendas)

    return f"{total_vendas}, {media_vendas:.2f}"


def obter_entrada_vendas():
    entrada = input()
    input_str = entrada.strip("[]")
    vendas = list(map(int, input_str.split(",")))

    return vendas


vendas = obter_entrada_vendas()
print(analise_vendas(vendas))


""" TEST 01
Input data:
    120, 150, 170, 130, 200, 250, 180, 220, 210, 160, 140, 190
Expected output:
    2120, 176.67
Your Output:
    Message: NameError
"""

""" TEST 02
Input data:
    10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120
Expected output:
    780, 65.00
Your Output:
    Message: NameError
"""

""" TEST 03
Input data:
    5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60
Expected output:
    390, 32.50
Your Output:
    Message: NameError
"""
