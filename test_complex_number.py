import pytest

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


def test_div_img_value():
    c1 = ComplexNumber(1, 2)
    c2 = ComplexNumber(3, 4)

    c3 = c1 / c2
    assert c3.imaginary_value == 0.08


def test_division_of_complex_number():
    c1 = ComplexNumber(1, 2)
    c2 = ComplexNumber(3, 4)
    c3 = c1 / c2
    assert c3.imaginary_value == 0.08
    assert c3.real_value == 0.44


def test_phase_real_part():
    c1 = ComplexNumber(1, 0)
    result = c1.phase()

    assert result == 0.00


def test_phase_img_part_zero_division_error():
    c1 = ComplexNumber(0, 1)
    with pytest.raises(ZeroDivisionError):
        c1.phase()


def test_phase_complex_number():
    c1 = ComplexNumber(1, 2)
    result = c1.phase()

    assert result == 1.11


def test_absolute_real_part():
    c1 = ComplexNumber(1, 0)

    result = c1.absolute()
    assert result == 0.00


def test_absolute_img_part_zero_division_error():
    c1 = ComplexNumber(0, 1)
    with pytest.raises(ZeroDivisionError):
        c1.absolute()


def test_absolute_complex_number():
    c1 = ComplexNumber(1, 2)

    result = c1.absolute()
    assert result == 63.435


def test_polar_real_part():
    c1 = ComplexNumber(1, 0)
    result = c1.polar()

    assert result == (0.00, 0.00)


def test_polar_img_part_zero_division_error():
    c1 = ComplexNumber(0, 1)
    with pytest.raises(ZeroDivisionError):
        c1.polar()


def test_polar_complex_number():
    c1 = ComplexNumber(1, 2)
    result = c1.polar()
    assert result == (1.11, 63.435)


def test_absolute_v2_definition():
    c1 = ComplexNumber(0, 0)
    result = c1.absolute_v2()
    assert result == 0


def test_absolute_v2_real_part():
    c1 = ComplexNumber(3, 0)
    result = c1.absolute_v2()
    assert result == 3


def test_absolute_v2_complex_number():
    c1 = ComplexNumber(3, 4)
    result = c1.absolute_v2()
    assert result == 5.00
