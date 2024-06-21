from natunits.prelude import *
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
    assert 1 == pytest.approx(unity >> GeV, 5e-3)

    unity = 2.99 * 10**8 * m / s
    assert 1 == pytest.approx(unity.in_(GeV), 5e-3)

    # Avogadro number
    n_ab = 6 * 10**23
    assert 1 == pytest.approx(kg.in_(GeV).coeff / n_ab / 1000, 0.1)

    # from Wikipedia
    k_eV = 0.862 * 10**-9 * 10**-4 * GeV
    assert 1 == pytest.approx(kelvin.in_(GeV) / k_eV, 5e-3)

    # electric constant
    assert 1 == pytest.approx((4 * pi * 8.854 * 10**-12 * m**-3 * kg**-1 * s**4 * A**2).in_(GeV), 1e-3)


# test for conversion
# partially overwrapped with test_unities
def test_conversion():
    # same (zero) units
    with pytest.raises(UnitNotMatchError):
        assert 299792458. == pytest.approx(c.in_(m / s), 1e-5)
    assert 299792458. == pytest.approx(c.in_(m / s).coeff, 1e-5)

    # c is dimensionless
    with pytest.raises(UnitNotMatchError):
        GeV.in_(c)

    # conversion to composite units
    assert 1.602176634 * 10**-19 == pytest.approx(eV.in_(J).coeff, 1e-5)


# test for str expression
def test_str():
    assert '1.00e+00 GeV' == str(GeV)
    assert '3.00e+08 s^-1 m' == str(c) or '3.00e+08 m s^-1' == str(c)
    assert '1.16e+04 kelvin' == str(eV.in_(kelvin))
    assert '1.60e-19 coulomb' == str(e)

# test for subunits
def test_subunit():
    assert 1e-3 == pytest.approx(MeV.coeff, 1e-3)
    assert 0.197 == pytest.approx(hbarc.in_(eV * um).coefficient(), 1e-2)
    assert '1.00e-01 b^1/2' == str(fm.in_(b))

    # Avogadro number
    n_ab = 6.02214 * 10**23
    assert n_ab == pytest.approx((1.0078 * g).in_(GeV) / (938.27 * MeV + 511 * keV), 1e-3)

    assert 0.001 == g / kg
    assert 0.01 == cm.coeff
    assert 1 == cm.coefficient()
