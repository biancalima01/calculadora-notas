def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3


def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def main():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = calcular_media(nota1, nota2, nota3)
    situacao = verificar_situacao(media)

    print(f"\nMédia: {media:.2f}")
    print(f"Situação: {situacao}")


if __name__ == "__main__":
    main()