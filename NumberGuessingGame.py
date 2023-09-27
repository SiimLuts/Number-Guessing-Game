import random

def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Numbri mäng")
    print("Proovi arvata number 1-100 vahemikus.")

    while True:
        try:
            guess = int(input("Number: "))
            attempts += 1

            if 1 <= guess <= 100:  
                if guess < secret_number:
                    print("Number on suurem")
                elif guess > secret_number:
                    print("Number on väiksem")
                else:
                    print(f"Jõudsid õige numbrini {secret_number} proovides {attempts} korda.")
                    break
            else:
                print("Palun sisesta täisarv 1-100 vahemikus")
        except ValueError:
            print("Palun sisesta täisarv 1-100 vahemikus")

if __name__ == "__main__":
    guess_number()
