"""
Handterar artsobservasjonar lagra på fil

"""


def summer(streng):
    """
    Returnerar summen av alle tal i strengen streng
    :param streng:
    :return:
    """
    liste = streng.split()
    summen = 0
    for ordet in liste:
        if ordet.isdigit():
            summen += int(ordet)
    return summen


def lag_totaloversikt(obs_filnamn, tot_filnamn):
    """
    Les artsobservasjonar frå fila med namn obs_filnamn,
    skriv talet på observasjonar av kvar art på fila
    tot_filnamn
    :param obs_filnamn:
    :param tot_filnamn:
    :return:
    """
    with open(obs_filnamn, 'r') as lesefil:
        with open(tot_filnamn, 'w') as skrivefil:
            for streng in lesefil:
                total = summer(streng)
                art = streng.split()[0]
                skrivefil.write(art + ' ' + str(total) + '\n')


def main():
    lag_totaloversikt('fugl.txt', 'tot_fugl.txt')


main()