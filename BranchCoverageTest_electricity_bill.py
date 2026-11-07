
import pytest

from electricity_bill import energy_charge, late_fee, subsidy


# ENERGY CHARGE BRANCHES

def test_unknown_connection_branch():
    with pytest.raises(ValueError):
        energy_charge(50, "unknown")


def test_negative_units_branch():
    with pytest.raises(ValueError):
        energy_charge(-5, "domestic")


def test_units_100_or_less():
    assert energy_charge(100, "domestic") == 350


def test_units_between_101_and_300():
    assert energy_charge(200, "domestic") == 600


def test_units_above_300():
    assert energy_charge(400, "domestic") == 2100


def test_commercial_branch():
    assert energy_charge(100, "commercial") == 750


# LATE FEE BRANCHES

def test_days_late_zero():
    assert late_fee(500, 0) == 0


def test_days_late_10():
    assert late_fee(500, 10) == 50


def test_days_late_20_low_bill():
    assert late_fee(1000, 20) == 100


def test_days_late_20_high_bill():
    assert late_fee(3000, 20) == 250


# SUBSIDY BRANCHES

def test_senior_low_units():
    assert subsidy(100, True, False) == 50


def test_low_units_not_senior():
    assert subsidy(100, False, False) == 0


def test_units_above_100_senior():
    assert subsidy(200, True, False) == 0


def test_solar_units_below_300():
    assert subsidy(200, False, True) == 100


def test_solar_units_above_300():
    assert subsidy(400, False, True) == 0


def test_senior_and_solar():
    assert subsidy(100, True, True) == 150
