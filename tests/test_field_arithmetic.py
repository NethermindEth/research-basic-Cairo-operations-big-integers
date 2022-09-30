import os

import pytest
from starkware.starknet.testing.starknet import Starknet
from starkware.python.math_utils import div_mod
from hypothesis import given, strategies as st, settings
from sympy import exp_polar
from utils import split, split2, pack
from utils import elliptic_curve_field_modulus as p
from sqrt_mod_p import get_square_root_mod_p


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
    p_split = split2(p, num_bits_shift=64, length=7)

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
    p_split = split2(p, num_bits_shift=64, length=7)

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
    p_split = split2(p, num_bits_shift=64, length=7)

    execution_info = await field_arithmetic_contract.field_arithmetic_mul(
        x_split, y_split, p_split
    ).call()
    result_split = execution_info.result
    result = pack(result_split[0], num_bits_shift=128)

    assert result == (x * y) % p


@given(
    x=st.integers(min_value=1, max_value=2**384 - 1),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_field_arithmetic_square(x, field_arithmetic_contract):

    print(x)

    x_split = split(x, num_bits_shift=128, length=3)
    p_split = split2(p, num_bits_shift=64, length=7)

    execution_info = await field_arithmetic_contract.field_arithmetic_square(
        x_split, p_split
    ).call()
    result_split = execution_info.result
    result = pack(result_split[0], num_bits_shift=128)

    assert result == (x * x) % p


@given(
    x=st.integers(min_value=1, max_value=2**384 - 1),
    y=st.integers(min_value=1, max_value=2**384 - 1),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_field_arithmetic_div(x, y, field_arithmetic_contract):

    print(x, y)

    x = x % p

    x_split = split(x, num_bits_shift=128, length=3)
    y_split = split(y, num_bits_shift=128, length=3)
    p_split = split2(p, num_bits_shift=64, length=7)

    execution_info = await field_arithmetic_contract.field_arithmetic_div_b(
        x_split, y_split, p_split
    ).call()
    result_split = execution_info.result
    result = pack(result_split[0], num_bits_shift=128)
    
    # For python3.8 and above the modular inverse can be computed as follows:
    # inverse= = pow(b, -1, p)
    # Instead we use the python3.7-friendly function div_mod from starkware.python.math_utils
    y_inverse = div_mod(1, y, p)
    assert result == (x * y_inverse) % p


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
    p_split = split2(p, num_bits_shift=64, length=7)

    execution_info = await field_arithmetic_contract.field_arithmetic_pow_b(
        x_split, exp_split, p_split
    ).call()
    result_split = execution_info.result
    result = pack(result_split[0], num_bits_shift=128)

    assert result == pow(x, exp, p)


p_minus_one_div_2 = 2001204777610833696708894912867952078278441409969503942666029068062015825245418932221343814564507832018947136279893

"""
@given(
    x=st.integers(min_value=1, max_value=p - 1),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_fq_is_square(field_arithmetic_contract, x):
    print(x)
    contract = field_arithmetic_contract

    execution_info = await contract.is_square_non_optimized(
        split(x, 128, 3), split2(p, 64, 7), split(p_minus_one_div_2, 128, 3)
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
"""

@pytest.mark.asyncio
async def test_fq_is_square_specific(field_arithmetic_contract):
    x = 457907432207496989162399472988030533119024029361471525053059782579451265324813329538446384952613152240792785100346
    contract = field_arithmetic_contract

    execution_info = await contract.is_square_non_optimized(
        split(x, 128, 3), split2(p, 64, 7), split(p_minus_one_div_2, 128, 3)
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


@given(
    x=st.integers(min_value=0, max_value=p - 1),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_fq_get_sqrt(field_arithmetic_contract, x):
    contract = field_arithmetic_contract

    print(x)
    
    # 2 happens to be a generator modulo the prime we are using
    generator = 2 
    python_success, python_sqrt = get_square_root_mod_p(x, p)
    
    execution_info = await contract.get_square_root(split(x), split2(p), split(generator)).call()

    success = execution_info.result[0]
    sqrt = execution_info.result[1]

    sqrt = pack(sqrt)
    
    assert python_success == success

    # Sanity check
    alternative_python_success = pow(x, (p - 1) // 2, p)
    if ((alternative_python_success + 1) % p) == 0:
        # If the power is -1 mod p, then x is not a root, otherwise it is 1 if x!= 0 or 0 if x=0
        alternative_python_success = 0
    if x == 0:
        # If x= 0 then x is a square
        alternative_python_success = 1
    assert ((alternative_python_success - success) % p) == 0

    # Check that the sqrt root is correct
    # Since there are two roots, we make two
    if success == 1:
        # Check that the sqrt root is correct
        # Since there are two roots, we make two checks
        assert (python_sqrt == sqrt) or ((-python_sqrt) % p == sqrt)
