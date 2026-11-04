class Sensore:
    def __init__(self, codice: str, grandezza: str, unita: str, soglia_massima: float):
        self.codice = codice
        self.grandezza = grandezza
        self.unita = unita
        self.soglia_massima = soglia_massima
    
    def __str__(self) -> str:
        return f"Codice: {self.codice}, grandezza: {self.grandezza}, unita: {self.unita}, soglia massima: {self.soglia_massima}"
    