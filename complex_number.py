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
