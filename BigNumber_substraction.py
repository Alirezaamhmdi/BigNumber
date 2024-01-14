class BigNumber:
    def __init__(self, number_str):
        self.number = number_str

    def __repr__(self):
        return self.number

    def subtract(self, other):
        result = ""
        carry = 0

        # Ensure both numbers have the same length by padding with zeros
        max_len = max(len(self.number), len(other.number))
        self.number = self.number.zfill(max_len)
        other.number = other.number.zfill(max_len)

        for i in range(max_len - 1, -1, -1):
            digit_self = int(self.number[i])
            digit_other = int(other.number[i]) + carry

            if digit_self < digit_other:
                digit_self += 10
                carry = 1
            else:
                carry = 0

            result = str(digit_self - digit_other) + result

        # Remove leading zeros
        result = result.lstrip('0')

        return BigNumber(result)


# Example usage:
num1 = BigNumber("12345678901234567898")
num2 = BigNumber("98765432109876543214")

result = num1.subtract(num2)
print(f"Result of subtraction: {result}")

