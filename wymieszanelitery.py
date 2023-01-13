# Gra wymieszane litery
# Komputer wybiera losowo słowo z listy, a potem miesza w nim litery
# Gracz powinien odgadnąć co to za słowo
# Za poprawne odgadnięcie słowa dostaje 10 punktów
# Użytkownik po pierwszej nieudanej próbie może prosić o pomoc
# Wyświetlenie wskazówki kosztuje 5 punktów


import random

# Tworzę sekwencje słów do wyboru
WORDS = ("kot",
        "kubek",
        "teatr",
        "chodnik",
        "jabłko",
        "konewka")
HINTS = ("Zwierzę domowe o miękkiej sierści, długim ogonie, długich wąsach i łapach zakończonych pazurami", 
        "Nieduże naczynie do picia z niego napojów", 
        "Instytucja zajmująca się wystawianiem utworów scenicznych",
        "Część ulicy przeznaczona dla ruchu pieszego.",
        "Owoc jabłoni",
        "Naczynie do podlewania roślin.")

score = 0

# Komputer wybiera losowo jedno słowo z sekwencji
word = random.choice(WORDS)
index = WORDS.index(word)
# print("Słowo to", word, "Indeks to", index)

# Tworzę zmienną, by później użyć jej do sprawdzenia, czy odpowiedź jest poprawna
correct = word

# Tworzę "pomieszaną" wersję słowa
pomieszane = ""

while word:
    position = random.randrange(len(word))
    pomieszane += word[position]
    word = word[:position] + word[(position + 1):]

# Rozpoczynam grę 
print(
    """"
    Witaj w grze 'Wymieszane litery'!
    Uporządkuj litery, aby odtworzyć prawidłowe słowo."""
)
print("Zgadnij jakie to słowo", pomieszane)

guess = input("\nTwoja odpowiedź to:")
while guess != correct and guess != "":
    print("\nNiestety, to nie to słowo. Spróbuj jeszcze raz.")
    hint = input("Czy chcesz dostać podpowiedź? TAK/NIE\n")
    hint = hint.upper()
    
    if hint == "TAK":
        score -= 5
        print("\nTwoja podpowiedź to:", HINTS[index])
        guess = input("Twoja nowa odpowiedź to:")

    else:    
        guess = input("Twoja nowa odpowiedź to:")

else:
    score +=10
    print("\nBrawo! Zgadza się. Poprawna odpowiedź to:", correct)
    print("Zdobyłaś/eś", score, "punktów.")

print("Dziękuję za udział w grze.")
