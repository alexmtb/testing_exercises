from functions.level_2.two_square_equation import solve_square_equation
import pytest


def test__solve_square_equation__correct_solving():
    test_square_coef = 2.4
    test_linear_coef = 9.7
    test_const_coef = 3.14

    equation_roots = solve_square_equation(
        square_coefficient=test_square_coef,
        linear_coefficient=test_linear_coef,
        const_coefficient=test_const_coef
    )

    assert equation_roots == (-3.686796726621967, -0.35486994004469996)


def test__solve_square_equation__null_square_coef():
    test_square_coef = 0
    test_linear_coef = 2.0
    test_const_coef = 5.0

    equation_roots = solve_square_equation(
        square_coefficient=test_square_coef,
        linear_coefficient=test_linear_coef,
        const_coefficient=test_const_coef
    )

    assert equation_roots == (-2.5, None)


def test__solve_square_equation__null_square_and_linear_coefs():
    test_square_coef = 0
    test_linear_coef = 0
    test_const_coef = 5.0

    equation_roots = solve_square_equation(
        square_coefficient=test_square_coef,
        linear_coefficient=test_linear_coef,
        const_coefficient=test_const_coef
    )

    assert equation_roots == (None, None)


def test__solve_square_equation__all_null_coefs():
    test_square_coef = 0
    test_linear_coef = 0
    test_const_coef = 0

    equation_roots = solve_square_equation(
        square_coefficient=test_square_coef,
        linear_coefficient=test_linear_coef,
        const_coefficient=test_const_coef
    )

    assert equation_roots == (None, None)


def test__solve_square_equation__discriminant_less_than_zero():
    test_square_coef = 5.0
    test_linear_coef = 2.0
    test_const_coef = 1.0

    equation_roots = solve_square_equation(
        square_coefficient=test_square_coef,
        linear_coefficient=test_linear_coef,
        const_coefficient=test_const_coef
    )

    assert equation_roots == (None, None)


def test__solve_square_equation__fails_on_none_input():
    test_square_coef = None
    test_linear_coef = 2.0
    test_const_coef = 1.0

    with pytest.raises(TypeError):
        solve_square_equation(
            square_coefficient=test_square_coef,
            linear_coefficient=test_linear_coef,
            const_coefficient=test_const_coef
    )


if __name__ == '__main__':
    # testing function run
    print(
        solve_square_equation(
            square_coefficient=None,
            linear_coefficient=2,
            const_coefficient=5
        )
    )