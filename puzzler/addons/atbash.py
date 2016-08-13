
import string

class atbash:

    def __init__(self):
        self.alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        return

    def main(self, data):
        rotData = []
        output = self.atbasher(data["input"])
        rotData.append({
            "output": output,
        })
        return rotData

    def atbasher(self, input):
        cipher = ""
        for word in input:
            if not word.upper() in self.alphabet:
                cipher += word
            else:
                if word in [x.lower() for x in self.alphabet]:
                    cipher += self.alphabet[len(self.alphabet) - self.alphabet.index(word.upper()) - 1 % len(self.alphabet)].lower()
                else:
                    cipher += self.alphabet[len(self.alphabet) - self.alphabet.index(word) - 1 % len(self.alphabet)]
        return cipher


