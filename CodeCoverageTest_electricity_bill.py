
import pytest

from electricity_bill import energy_charge, late_fee, subsidy


# ENERGY CHARGE TESTS

def test_domestic_low_usage():
    assert energy_charge(50, "domestic") == 200


def test_domestic_medium_usage():
    assert energy_charge(200, "domestic") == 600


def test_domestic_high_usage():
    assert energy_charge(400, "domestic") == 2100


def test_commercial_connection():
    assert energy_charge(50, "commercial") == 450


def test_unknown_connection():
    with pytest.raises(ValueError):
        energy_charge(100, "invalid")


def test_negative_units():
    with pytest.raises(ValueError):
        energy_charge(-10, "domestic")


# LATE FEE TESTS

def test_no_late_fee():
    assert late_fee(500, 0) == 0


def test_late_fee_15_days():
    assert late_fee(500, 15) == 50


def test_late_fee_more_than_15_days():
    assert late_fee(500, 20) == 100


def test_late_fee_high_bill():
    assert late_fee(3000, 20) == 250


# SUBSIDY TESTS

def test_senior_citizen_low_usage():
    assert subsidy(80, True, False) == 50


def test_solar_subsidy():
    assert subsidy(200, False, True) == 100


def test_senior_and_solar():
    assert subsidy(80, True, True) == 150


def test_solar_high_usage():
    assert subsidy(400, False, True) == 0


def test_no_subsidy():
    assert subsidy(200, False, False) == 0
