from GLC import GLC


def main():
    glc = GLC(9, 4, 0, 1)
    # Primer punto
    # glc.create_plot(1587)
    # Segundo punto
    glc.create_plot(10000)
    glc.create_plot(1000)
    glc.create_plot(100)
    glc_2 = GLC(9, 1, 1, 1)
    glc_2.create_plot(10000)
    glc_2.create_plot(1000)
    glc_2.create_plot(100)


main()
