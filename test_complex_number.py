from complex_number import ComplexNumber


def test_attributes_class_complex_number():
    complex_number = ComplexNumber(real_value=0, imaginary_value=0)
    complex_number.real_value == 0
    complex_number.imaginary_value == 0
