from random import choice


questoes = {
    "a)": "25%",
    "b)": "60%",
    "c)": "50%",
    "d)": "25%"
}
print(f"{' ' * 50} {choice(list(questoes.items()))}")