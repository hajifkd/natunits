from hepunits import GeV, s, m, kg, kelvin, UnitNotMatchError
import pytest
from fractions import Fraction


def test_operations():
    assert 1 == pytest.approx(GeV / GeV)
    assert GeV == ((GeV * s) / s)
    assert GeV == ((GeV * s**Fraction(1, 2)) * s**Fraction(-1, 2))
    assert 2 * GeV == GeV + GeV
    assert 0 * GeV == GeV - GeV
    assert GeV / 0.5 == GeV(2.0)

    # Exception check for the operations b/w different units
    with pytest.raises(UnitNotMatchError):
        GeV < s
    
    with pytest.raises(UnitNotMatchError):
        GeV + s

    with pytest.raises(UnitNotMatchError):
        GeV == s


def test_unities():
    unity = 0.197 * GeV * 10**-15 * m
    assert 1 == pytest.approx(unity.in_GeV(), 5e-3)

    unity = 2.99 * 10**8 * m / s
    assert 1 == pytest.approx(unity.in_GeV(), 5e-3)

    # Avogadro number
    n_ab = 6 * 10**23
    assert 1 == pytest.approx(kg.in_GeV().coeff / n_ab / 1000, 0.1)

    # from Wikipedia
    k_eV = 0.862 * 10**-9 * 10**-4 * GeV
    assert 1 == pytest.approx(kelvin.in_GeV() / k_eV, 5e-3)

# test for conversion

# test for subunits