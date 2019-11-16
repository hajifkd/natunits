# from hepunits import GeV, s, m, kg, kelvin, UnitNotMatchError
from hepunits.prelude import *
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
    assert 1 == pytest.approx(unity.in_(GeV), 5e-3)

    unity = 2.99 * 10**8 * m / s
    assert 1 == pytest.approx(unity.in_(GeV), 5e-3)

    # Avogadro number
    n_ab = 6 * 10**23
    assert 1 == pytest.approx(kg.in_(GeV).coeff / n_ab / 1000, 0.1)

    # from Wikipedia
    k_eV = 0.862 * 10**-9 * 10**-4 * GeV
    assert 1 == pytest.approx(kelvin.in_(GeV) / k_eV, 5e-3)

    # Volt
    assert 1e-9 == pytest.approx(V.in_(GeV).coeff, 1e-5)



# test for conversion
# partially overwrapped with test_unities
def test_conversion():
    # same (zero) units
    assert 299792458. == pytest.approx(c.in_(m / s), 1e-5)

    # c is dimensionless
    with pytest.raises(UnitNotMatchError):
        GeV.in_(c)

    # conversion to composite units
    assert 1.602176634 * 10**-19 == pytest.approx(eV.in_(J).coeff, 1e-5)


# test for subunits