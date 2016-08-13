
class rot:

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self):
        return

    # main routine to execute
    def main(self, data):
        return

    # everything possible at once
    def all(self, data):
        rotData = []
        for key in range(len(self.alphabet)):
            output = self.rot(data["input"], key)
            rotData.append({
                "n": key,
                "output": output, 
            })
        return rotData

    # process only one
    def single(self, data):
        output = self.rot(data["input"], data["n"])
        return output

    # basic decrypt
    def rot(self, str="", n=13):
        rot_out = ''
        # rot each letter in the input ciphertext
        for symbol in str:
            if symbol.capitalize() in self.alphabet:
                num = self.alphabet.find(symbol.capitalize())
                # rot n
                num = num + n
                # correct wrap-around
                if num > 25:
                    num = num - 26
                # add to output string
                rot_out = rot_out + self.alphabet[num]
            else:
                rot_out = rot_out + symbol
        return rot_out
        

