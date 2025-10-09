class Libro:
    def __init__(self, titolo, autore, anno, numPagine, sezione):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.numPagine = numPagine
        self.sezione = sezione

    def __str__(self):
        return f"{self.titolo}, {self.autore}, {self.anno}, {self.numPagine}"