fahrkosten_mini = [
    [0, 6, 2, 4],
    [6, 0, 9, 7],
    [2, 9, 0, 5],
    [4, 7, 5, 0]
]


import re

def schreibe_Liste_in_Textdatei(liste, dateiname = 'route.txt'):
    '''
    Uberführt eine einfache Liste von Werten in eine Textdatei.
    Der Dateiname kann frei gewaehlt werden (Standard: weg.txt)
    '''
    datei = open(dateiname, 'w', encoding='utf-8')
    text = ''
    for element in liste:
        text = text + str(element) + ' '
    datei.write(text)
    datei.close()
    print('Datei', dateiname, 'geschrieben.')
    return 


def pruefe():

    # Rundreise lesen
    
    filename = input("Result file: ")
    f = open(filename,"r")
    tour = []
    for line in f:
        tour += re.findall(r'\d+', line)
    f.close()

    fahrkosten = fahrkosten1000

    # Minimalbeispiel zum Testen
    #tour = [0, 2, 3, 1]
    #fahrkosten = fahrkosten_mini

    # Rundreise prüfen
    
    #    Länge der Rundreise
    if len(tour) != len(fahrkosten):
        print("Tour ist ", len(tour), "lang und nicht", len(fahrkosten))
        return

    #   Duplikatfreiheit und Range der Rundreise
    kommtvor = []
    for i in range(len(fahrkosten)):
        kommtvor.append(False)
        tour[i] = int(tour[i])
    for i in range(len(fahrkosten)):
        stadt = tour[i]
        if stadt < 0 or stadt >= len(fahrkosten):
            print("Tour enthält eine Nichtstadt", stadt)
            return
        if kommtvor[stadt]:
            print("Stadt wird doppelt besucht: ", stadt)
            return
        kommtvor[stadt] = True

    print("Wir haben eine Rundreise!")

    # Kosten berechnen

    kosten = 0
    for i in range(len(fahrkosten)-1):
        kosten += fahrkosten[tour[i]][tour[i+1]]
    kosten+= fahrkosten[tour[-1]][tour[0]]
    print("Diese Rundreise kostet ", kosten, "pangalaktische Antimonschnecken")

        
