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


def test_conjugate_real_part():
    complex_number = ComplexNumber(real_value=1, imaginary_value=2)
    complex_number.conjugate()
    assert complex_number.real_value == 1


def test_get_conjugate_complex_number():
    complex_number = ComplexNumber(real_value=1, imaginary_value=2)
    con = complex_number.conjugate()
    assert con.real_value == 1
    assert con.imaginary_value == -2


def test_add_real_part():
    c1 = ComplexNumber(1, 2)
    c2 = ComplexNumber(3, 4)

    c3 = c1 + c2

    assert c3.real_value == (c1.real_value + c2.real_value)


def test_add_img_value():
    c1 = ComplexNumber(1, 2)
    c2 = ComplexNumber(3, 4)

    c3 = c1 + c2

    assert c3.real_value == (c1.real_value + c2.real_value)
    assert c3.imaginary_value == (c1.imaginary_value + c2.imaginary_value)


def test_sub_real_part():
    c1 = ComplexNumber(1, 0)
    c2 = ComplexNumber(3, 0)

    c3 = c1 - c2

    assert c3.real_value == (c1.real_value - c2.real_value)


def test_sub_img_value():
    c1 = ComplexNumber(1, 2)
    c2 = ComplexNumber(3, 4)

    c3 = c1 - c2

    assert c3.real_value == (c1.real_value - c2.real_value)
    assert c3.imaginary_value == (c1.imaginary_value - c2.imaginary_value)


def test_mul_real_value():
    c1 = ComplexNumber(1, 0)
    c2 = ComplexNumber(3, 0)

    c3 = c1 * c2

    assert c3.real_value == 3


def test_mul_img_value():
    c1 = ComplexNumber(0, -1)
    c2 = ComplexNumber(0, 2)

    c3 = c1 * c2
    assert c3.imaginary_value == 0


def test_multiply_complex_numbers():
    c1 = ComplexNumber(1, 2)
    c2 = ComplexNumber(3, 4)
    c3 = c1 * c2

    assert c3.imaginary_value == 10
    assert c3.real_value == -5


def test_div_real_value():
    c1 = ComplexNumber(1, 0)
    c2 = ComplexNumber(3, 0)

    c3 = c1 / c2
    assert c3.real_value == 0.33

