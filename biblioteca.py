from csv import DictReader

def main ():

    biblio, n = leggiBiblio("biblioteca.csv")
    nSezioni = int(n)
    scelta = menu()
    while scelta != "5":
        if scelta == "1":
            for libro in biblio :
                for parametro in libro :
                    print(libro[parametro], end = " ")
                print(";")
            print()
        if scelta == "2":
            aggiungiLibro(biblio, nSezioni, "biblioteca.csv")
        if scelta == "3":
            cerca = cercaLibro(biblio)
            for parametro in cerca :
                print(cerca[parametro], end = " ")
            print(";")
            print()
        if scelta == "4":
            lista = elencoSezione(biblio, nSezioni)
            alfabetico = sorted(lista, key=lambda libro: libro["titolo"].lower())
            for libro in alfabetico:
                print(libro["titolo"], end = " ")
                print(";")
            print()
        scelta = menu()

def elencoSezione(biblio, nSezioni):
    sezione = input(f"Inserire sezione tra le {nSezioni} presenti: ")
    lista = []
    if sezione.isdigit():
        intSezione =int(sezione)
    else :
        print("sezione non numerica")
        print()
        return None
    if int(sezione)<1 or int(sezione)>nSezioni:
        print(f"sezione {sezione} non esistente")
        print()
        return None
    for libro in biblio:
        if int(libro["sezione"]) == intSezione:
            lista.append(libro)
    return lista

def cercaLibro(biblio):
    cerca = input("Inserire il titolo del libro da cercare: ")
    for libro in biblio:
        if libro["titolo"].strip().lower() == cerca.lower():
            return libro
    return None

def aggiungiLibro(biblio, nSezioni, filename):
    titolo = input("Inserire il titolo del libro da aggiungere: ")
    for libro in biblio:
        if libro["titolo"].strip().lower() == titolo.lower():
            print(f"{titolo} già presente")
            print()
            return None
        else:
            autore = input("Inserire autore: ")
            anno = input("Inserire anno: ")
            pagine = input("Inserire pagine: ") 
            sezione = input("Inserire sezione: ")
            if sezione.isdigit():
                if int(sezione)<1 or int(sezione)>nSezioni:
                    print(f"sezione {sezione} non esistente")
                    print()
                    return None
                else :
                    print(f"libro {titolo} aggiunto correttamente")
                    print()
                    biblio.append({'titolo':titolo,'autore':autore,'anno':anno,'pagine':pagine,'sezione':sezione})
                    try :
                        f = open(filename, "a", encoding = "utf-8")
                    except OSError :
                        print("file non trovato")
                        print()
                        return None
                    f.write(f"{titolo},{autore},{anno},{pagine},{sezione}")
                    f.close()
                    return biblio
            else :
                print("la sezione inserita non è un carattere numerico")
                print()
                return None

def menu():
    print("1. Carica biblioteca da file")
    print("2. Aggiungi un nuovo libro")
    print("3. Cerca un libro per titolo")
    print("4. Ordina titoli di una sezione")
    print("5. Esci")
    scelta = input("Scegli un'opzione (scrivere 1,2,3,4 o 5)>> ")
    print()
    return scelta

def leggiBiblio(filename):
    try :
        fileIn = open(filename, "r", encoding = "utf-8")
    except FileNotFoundError :
        return None
    nSezioni = fileIn.readline().strip()
    biblio = []
    reader = DictReader(fileIn,fieldnames=["titolo","autore","anno", "pagine", "sezione"])
    for record in reader :
        biblio.append(record)
    fileIn.close()
    return biblio, nSezioni

main()

if __name__ == "__main__":
    main()


