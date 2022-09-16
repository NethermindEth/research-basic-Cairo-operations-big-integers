from re import A
import pytest
from hypothesis import given, strategies as st, settings
from utils import split, pack

# Tests all functions from uint384_extension_contract 


@given(
    a=st.integers(min_value=1, max_value=2**768 - 1),
    b=st.integers(min_value=1, max_value=2**384 - 1),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_add_uint768_and_uint384(a, b, uint384_extension_contract):

    print(a, b)

    a_split = split(a, num_bits_shift=128, length=6)
    b_split = split(b, num_bits_shift=128, length=3)

    execution_info = await uint384_extension_contract.uint384_add_uint768_and_uint384(a_split, b_split).call()
    result_no_carry, carry = execution_info.result
    result = pack(result_no_carry, num_bits_shift=128) + 2**768 * carry

    assert result == a + b



@given(
    x=st.integers(min_value=1, max_value=2**768 - 1),
    y=st.integers(min_value=1, max_value=2**384 - 1),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_mul_uint768_by_uint384(x, y, uint384_extension_contract):

    print(x, y)

    x_split = split(x, num_bits_shift=128, length=6)
    y_split = split(y, num_bits_shift=128, length=3)

    execution_info = await uint384_extension_contract.uint384_mul_uint768_by_uint384_d(x_split, y_split).call()
    result_split = execution_info.result
    low = pack(result_split[0], num_bits_shift=128)
    high = pack(result_split[1], num_bits_shift=128)
    result = low + 2**768 * high

    assert result == x * y


@given(
    x=st.integers(min_value=1, max_value=2**768 - 1),
    y=st.integers(min_value=1, max_value=2**384 - 1),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_uint384_unsigned_div_rem_uint768_by_uint384(x, y, uint384_extension_contract):

    print(x, y)

    x_split = split(x, num_bits_shift=128, length=6)
    y_split = split(y, num_bits_shift=128, length=3)

    execution_info = await uint384_extension_contract.uint384_unsigned_div_rem_uint768_by_uint384(
        x_split, y_split
    ).call()
    result_split = execution_info.result
    quotient = pack(result_split[0], num_bits_shift=128)
    reminder = pack(result_split[1], num_bits_shift=128)

    assert divmod(x, y) == (quotient, reminder)
