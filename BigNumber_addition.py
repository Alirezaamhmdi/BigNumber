

class BigNumber:

    def __init__(self, value):
        self.sign = 1 if value >= 0 else -1
        self.digits = [int(digit) for digit in str(abs(value))]

    def __str__(self):
        sign_str = "-" if self.sign == -1 else ""
        return sign_str + ''.join(map(str, self.digits))

    def __add__(self, other):
        if self.sign == other.sign:
            # If both have the same sign, perform addition
            len_self, len_other = len(self.digits), len(other.digits)
            if len_self < len_other:
                self.digits = [0] * (len_other - len_self) + self.digits
            else:
                other.digits = [0] * (len_self - len_other) + other.digits

            result = []
            carry = 0
            for digit_self, digit_other in zip(reversed(self.digits), reversed(other.digits)):
                digit_sum = digit_self + digit_other + carry
                result.append(digit_sum % 10)
                carry = digit_sum // 10

            if carry:
                result.append(carry)

            result.reverse()

            return BigNumber(self.sign * int(''.join(map(str, result))))

        else:
            # If they have different signs, perform subtraction
            if self.sign == -1:
                return other - abs(self)
            else:
                return self - abs(other)

    def __sub__(self, other):
        if self.sign == other.sign:
            # If both have the same sign, perform subtraction
            if abs(self) >= abs(other):
                result = []
                borrow = 0
                for digit_self, digit_other in zip(reversed(self.digits), reversed(other.digits)):
                    digit_diff = digit_self - digit_other - borrow
                    if digit_diff < 0:
                        digit_diff += 10
                        borrow = 1
                    else:
                        borrow = 0
                    result.append(digit_diff)

                result.reverse()

                return BigNumber(self.sign * int(''.join(map(str, result))))
            else:
                return (other - self).negate()

        else:
            
            return self + abs(other)

    def negate(self):
        return BigNumber(-self.sign * int(''.join(map(str, self.digits))))



num1 = BigNumber(-161616161611)
num2 = BigNumber(-822992920546)

sum_result = num1 + num2
print("Sum:", sum_result)




