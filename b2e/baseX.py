class BaseX:
    def encode(self, num):
        """ Encode a positive number in Base X

        Arguments:
            num(int): The number to encode
        """
        if num == 0:
            return self.base_character[0]
        base_string = []
        base = len(self.base_character)
        while num:
            num, rem = divmod(num, base)
            base_string.append(self.base_character[rem])
        return ''.join(base_string[::-1])

    def decode(self, base_string):
        """ Decode a Base X encoded string into the number

        Arguments:
            base_string(str): The encoded string
        """
        base = len(self.base_character)
        strlen = len(base_string)
        num = 0

        for idx, char in enumerate(base_string):
            power = (strlen - (idx + 1))
            num += self.base_character.index(char) * (base ** power)

        return num

class Base62(BaseX):
    base_character = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

