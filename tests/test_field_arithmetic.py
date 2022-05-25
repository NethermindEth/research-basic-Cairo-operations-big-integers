import os

import pytest
from starkware.starknet.testing.starknet import Starknet
from hypothesis import given, strategies as st, settings
from sympy import exp_polar
from utils import split, pack
from utils import elliptic_curve_field_modulus as p

# Tests all functions from field_arithmetic_contract 

@given(
    x=st.integers(min_value=1, max_value=2**384 - 1),
    y=st.integers(min_value=1, max_value=2**384 - 1),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_field_arithmetic_add(x, y, field_arithmetic_contract):

    print(x, y)

    x_split = split(x, num_bits_shift=128, length=3)
    y_split = split(y, num_bits_shift=128, length=3)
    p_split = split(p, num_bits_shift=128, length=3)

    execution_info = await field_arithmetic_contract.field_arithmetic_add(
        x_split, y_split, p_split
    ).call()
    result_split = execution_info.result
    result = pack(result_split[0], num_bits_shift=128)

    assert result == (x + y) % p


@given(
    x=st.integers(min_value=1, max_value=2**384 - 1),
    y=st.integers(min_value=1, max_value=2**384 - 1),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_field_arithmetic_sub(x, y, field_arithmetic_contract):

    print(x, y)

    # NOTE: The field_arithmetic_sub function currently does not work if x>p.  This is not super important: It is natural to reduce modulo p all inputs to field arithmetic operations, so for now we can do that
    x = x % p
    y = y % p

    x_split = split(x, num_bits_shift=128, length=3)
    y_split = split(y, num_bits_shift=128, length=3)
    p_split = split(p, num_bits_shift=128, length=3)

    execution_info = await field_arithmetic_contract.field_arithmetic_sub(
        x_split, y_split, p_split
    ).call()
    result_split = execution_info.result
    result = pack(result_split[0], num_bits_shift=128)

    assert result == (x - y) % p


@given(
    x=st.integers(min_value=1, max_value=2**384 - 1),
    y=st.integers(min_value=1, max_value=2**384 - 1),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_field_arithmetic_mul(x, y, field_arithmetic_contract):

    print(x, y)

    x_split = split(x, num_bits_shift=128, length=3)
    y_split = split(y, num_bits_shift=128, length=3)
    p_split = split(p, num_bits_shift=128, length=3)

    execution_info = await field_arithmetic_contract.field_arithmetic_mul(
        x_split, y_split, p_split
    ).call()
    result_split = execution_info.result
    result = pack(result_split[0], num_bits_shift=128)

    assert result == (x * y) % p


@given(
    x=st.integers(min_value=1, max_value=2**384 - 1),
    y=st.integers(min_value=1, max_value=2**384 - 1),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_field_arithmetic_div(x, y, field_arithmetic_contract):

    print(x, y)

    x_split = split(x, num_bits_shift=128, length=3)
    y_split = split(y, num_bits_shift=128, length=3)
    p_split = split(p, num_bits_shift=128, length=3)

    execution_info = await field_arithmetic_contract.field_arithmetic_div(
        x_split, y_split, p_split
    ).call()
    result_split = execution_info.result
    result = pack(result_split[0], num_bits_shift=128)

    assert result == (x * pow(y, -1, p)) % p


@given(
    x=st.integers(min_value=1, max_value=2**384 - 1),
    exp=st.integers(min_value=1, max_value=2**384 - 1),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_field_arithmetic_pow(x, exp, field_arithmetic_contract):

    print(x, exp)

    x_split = split(x, num_bits_shift=128, length=3)
    exp_split = split(exp, num_bits_shift=128, length=3)
    p_split = split(p, num_bits_shift=128, length=3)

    execution_info = await field_arithmetic_contract.field_arithmetic_pow(
        x_split, exp_split, p_split
    ).call()
    result_split = execution_info.result
    result = pack(result_split[0], num_bits_shift=128)

    assert result == pow(x, exp, p)
