from Lab3use import Bintree

lista_för_barn = [] #lista för att skriva ut barnen

def makechildren(start_ordet):
    svenska = Bintree()
    gamla = Bintree()

    with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()
            counter = 0

            for i in range(len(start_ordet)):
                if ordet[i] != start_ordet[i]: #Om det finns mer än EN missmatchad bokstav
                    counter += 1
                if counter > 1: #större än EN missmatchning, breaks, mer än två bokstäver som ej matchar
                    break

            if counter == 1: #när maximalt EN bokstav är missmatchad
                barn = ordet
                print("En bokstav missmatched jämfört med vårt startord - " + start_ordet + " <-> " +ordet)

                if barn not in svenska:
                    svenska.put(barn)
                if barn not in gamla:
                    gamla.put(barn)
                    lista_för_barn.append(barn) #för att skriva ut på snyggt sätt alla barnen

    print("Barnen för " + str(start_ordet) + " blir: " + "\n" +str(lista_för_barn))

makechildren(start_ordet="söt")

