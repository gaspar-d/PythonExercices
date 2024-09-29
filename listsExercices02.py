produtos01 = ["Notebook", "Mouse", "Teclado", "Mouse", "Monitor", "Mouse", "Teclado"]
produtos02 = [
    "Impressora",
    "Teclado",
    "Monitor",
    "Monitor",
    "Teclado",
    "Impressora",
    "Impressora",
]
produtos03 = ["Webcam", "Cama", "Headset", "Monitor", "Headset", "Headset"]


def produto_mais_vendido(produtos: list[str]) -> str | None:
    contagem: dict[str, int] = {}

    for produto in produtos:
        if produto in contagem:
            contagem[produto] += 1
        else:
            contagem[produto] = 1

    max_produto = None
    max_count = 0

    # max_produto = max(contagem, key=contagem.get) # This line is equivalent to the code below
    for produto, count in contagem.items():
        # Find the product with the highest count
        if count > max_count:
            max_produto = produto
            max_count = count

    return max_produto


def obter_entrada_produtos():
    # Read input from the user, assuming it's a single line of comma-separated product names
    entrada = input().strip()
    # Split the input string by commas and remove extra spaces around each product
    produtos = [item.strip() for item in entrada.split(",")]

    return produtos


# Main block
produtos = obter_entrada_produtos()
print(produto_mais_vendido(produtos))


"""Input data:
Notebook, Mouse, Teclado, Mouse, Monitor, Mouse, Teclado
Expected output:
Mouse
"""

"""Input data:
Impressora, Teclado, Monitor, Monitor, Teclado, Impressora, Impressora
Expected output:
Impressora
"""

"""Input data:
Webcam, Webcam, Headset, Monitor, Headset, Headset
Expected output:
Headset
"""
