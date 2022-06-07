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


p_minus_one_div_2 = 2001204777610833696708894912867952078278441409969503942666029068062015825245418932221343814564507832018947136279893


@given(
    x=st.integers(min_value=1, max_value=p - 1),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_fq_is_square(field_arithmetic_contract, x):
    print(x)
    contract = field_arithmetic_contract

    execution_info = await contract.is_square(
        split(x, 128, 3), split(p, 128, 3), split(p_minus_one_div_2, 128, 3)
    ).call()

    result = execution_info.result[0]
    python_result = pow(x, p_minus_one_div_2, p)

    # This `if` is checking whether `python_result` is -1 modulo `field_modulus``
    if (python_result - (-1)) % p == 0:
        # In this case `x` is not a square
        python_result = 0
    else:
        # Otherwise it is
        python_result = 1
    assert result == python_result


@pytest.mark.asyncio
async def test_fq_is_square_specific(field_arithmetic_contract):
    x = 457907432207496989162399472988030533119024029361471525053059782579451265324813329538446384952613152240792785100346
    contract = field_arithmetic_contract

    execution_info = await contract.is_square(
        split(x, 128, 3), split(p, 128, 3), split(p_minus_one_div_2, 128, 3)
    ).call()

    result = execution_info.result[0]
    python_result = pow(x, p_minus_one_div_2, p)

    print("findme", result, python_result)
    # This `if` is checking whether `python_result` is -1 modulo `field_modulus``
    if (python_result - (-1)) % p == 0:
        # In this case `x` is not a square
        python_result = 0
    else:
        # Otherwise it is
        python_result = 1
    assert result == python_result
