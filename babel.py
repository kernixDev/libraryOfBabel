import random

chars = list("abcdefghijklmnopqrstuvwxyz .,;-?!")

def generate_page(page):
    rng = random.Random(page)

    for _ in range(40):
        line = ""

        for _ in range(80):
            line += rng.choice(chars)

        print(line)

generate_page(int(input("Seed: ")))