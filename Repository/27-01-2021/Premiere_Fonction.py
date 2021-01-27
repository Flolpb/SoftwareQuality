def historique(annee):
    if annee == '1492':
        return "Découverte de l'Amérique"
    elif annee == '1515':
        return "Bataille de Marignan"
    else:
        return "Ne correspond à rien"


def main():
    inp = input('Rentrez une année')
    historique(inp)


if __name__ == '__main__':
    main()