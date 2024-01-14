class BigNumber:
    def __init__(self, number_str):
        self.number = number_str

    def __repr__(self):
        return self.number

    def multiply(self, other):
        result = "0"


        max_len = max(len(self.number), len(other.number))
        self.number = self.number.zfill(max_len)
        other.number = other.number.zfill(max_len)

        for i in range(max_len - 1, -1, -1):
            digit_other = int(other.number[i])


            temp_result = ""
            carry = 0
            for j in range(max_len - 1, -1, -1):
                digit_self = int(self.number[j])
                product = digit_self * digit_other + carry
                carry, digit = divmod(product, 10)
                temp_result = str(digit) + temp_result


            temp_result = temp_result + "0" * (max_len - i - 1)
            result = self._add(result, temp_result)


        result = result.lstrip('0')

        return BigNumber(result)

    def _add(self, num1, num2):
        result = ""
        carry = 0


        max_len = max(len(num1), len(num2))
        num1 = num1.zfill(max_len)
        num2 = num2.zfill(max_len)

        for i in range(max_len - 1, -1, -1):
            digit_sum = int(num1[i]) + int(num2[i]) + carry
            carry, digit = divmod(digit_sum, 10)
            result = str(digit) + result

        if carry:
            result = str(carry) + result

        return result.lstrip('0')



num1 = BigNumber("363737272727")
num2 = BigNumber("77766662")

result = num1.multiply(num2)
print(f"Result of multiplication: {result}")