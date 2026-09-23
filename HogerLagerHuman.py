MIN = 0
MAX = 100 
guesses = 0

def setup():
    # een beetje uitleg over het spel
    print(f"Denk aan een getal van {MIN} tot {MAX}")
    print(f"Je zal vragen krijgen over je getal. Antwoord met hoger/h of lager/l of correct/c.")
    print("")

def ask(num):
    global guesses
    guesses += 1
    ans = input(f"Is je getal hoger of lager dan {num}? ")

    if ans == "correct" or ans == "c":
        print(f"Het programma heeft geraden in {guesses} gokken.")
        return "correct"
    elif ans == "hoger" or ans == "h":
        return "hoger"
    elif ans == "lager" or ans == "l":
        return "lager"
    else:
        return ask(num) # foute input: opnieuw vragen
    

setup()
ask(40)
ask(60)
ask(80)