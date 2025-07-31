def pozdrav(jmeno):
    return f"Ahoj, {jmeno}!"

if __name__ == "__main__":
    j = input("Zadej jméno: ")
    print(pozdrav(j))
import requests
print("Requests verze:", requests.__version__)