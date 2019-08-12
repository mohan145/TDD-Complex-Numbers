from complex_number import ComplexNumber


def test_class_complex_number():
    complex_number = ComplexNumber(real_value=0, imaginary_value=0)
    complex_number.real_value == 0
    complex_number.imaginary_value == 0


def test_complex_number_attributes():
    complex_number = ComplexNumber(real_value=2, imaginary_value=3)
    assert complex_number.real_value == 2
    assert complex_number.imaginary_value == 3


def test_instantiation_complex_number():
    complex_number = ComplexNumber(real_value=1, imaginary_value=2)
    assert str(complex_number) == '1+2i'
