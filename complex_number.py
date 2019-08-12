class ComplexNumber:

    def __init__(self, real_value, imaginary_value):
        self.real_value = real_value
        self.imaginary_value = imaginary_value

    def __str__(self):

        if self.imaginary_value < 0:
            return str(self.real_value) + str(self.imaginary_value) + "i"
        else:
            return str(self.real_value) + "+" + \
                   str(self.imaginary_value) + "i"

    def conjugate(self):
        res_real_value = self.real_value
        res_img_value = self.imaginary_value * -1

        return ComplexNumber(res_real_value, res_img_value)

    def __add__(self, other):
        res_real_value = self.real_value + other.real_value
        res_img_value = self.imaginary_value + other.imaginary_value

        return ComplexNumber(res_real_value, res_img_value)

    def __sub__(self, other):
        res_real_value = self.real_value - other.real_value
        res_img_value = self.imaginary_value - other.imaginary_value

        return ComplexNumber(res_real_value, res_img_value)

    def __mul__(self, other):

        res_real_value = self.real_value * other.real_value + \
                         self.imaginary_value * (
                                 -1 * other.imaginary_value)

        res_imaginary_value = (self.imaginary_value * other.real_value) + \
                              (self.real_value * other.imaginary_value)

        return ComplexNumber(res_real_value, res_imaginary_value)

    def __truediv__(self, other):

        conjugate = other.conjugate()
        num = self * conjugate
        din = other * conjugate

        res_imaginary_value = round(num.imaginary_value / din.real_value,2)
        res_real_value = round(num.real_value / din.real_value,2)

        return ComplexNumber(res_real_value, res_imaginary_value)
