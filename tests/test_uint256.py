import pytest
from hypothesis import given, strategies as st, settings
from utils import split, pack

# Tests all functions from uint256_contract 

@given(
    x=st.integers(min_value=1, max_value=2**256 - 1),
    y=st.integers(min_value=1, max_value=2**256 - 1),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_sub(x, y, uint256_contract):

    x_split = split(x, num_bits_shift=128, length=2)
    y_split = split(y, num_bits_shift=128, length=2)

    execution_info = await uint256_contract.uint256_sub_new_c(x_split, y_split).call()
    result_no_carry = execution_info.result[0]
    sign = execution_info.result[1]
    result = pack(result_no_carry, num_bits_shift=128)

    if y > x:
        temp = result - 2**256
        print(temp)
        assert temp == x - y
        assert sign == 0
    else:
        assert result == x - y
        assert sign == 1


@given(
    x=st.integers(min_value=1, max_value=2**256 - 1),
    y=st.integers(min_value=1, max_value=2**256 - 1),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_mul(x, y, uint256_contract):

    print(x, y)

    x_split = split(x, num_bits_shift=128, length=2)
    y_split = split(y, num_bits_shift=128, length=2)

    execution_info = await uint256_contract.uint256_mul_new_c(x_split, y_split).call()
    result_split = execution_info.result
    low = pack(result_split[0], num_bits_shift=128)
    high = pack(result_split[1], num_bits_shift=128)
    result = low + 2**256 * high

    assert result == x * y


@given(
    x=st.integers(min_value=1, max_value=2**256 - 1),
    y=st.integers(min_value=1, max_value=2**256 - 1),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_mul_expanded(x, y, uint256_contract):

    print(x, y)

    x_split = split(x, num_bits_shift=128, length=2)
    y_split = split(y, num_bits_shift=128, length=2)

    execution_info = await uint256_contract.uint256_expand_c(y_split).call()
    y_exp = execution_info.result[0]
    execution_info = await uint256_contract.uint256_mul_expanded_c(x_split, y_exp).call()
    result_split = execution_info.result
    low = pack(result_split[0], num_bits_shift=128)
    high = pack(result_split[1], num_bits_shift=128)
    result = low + 2**256 * high

    assert result == x * y


@given(
    x=st.integers(min_value=1, max_value=2**256 - 1),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_square(x, uint256_contract):

    print(x)

    x_split = split(x, num_bits_shift=128, length=2)

    execution_info = await uint256_contract.uint256_square_c(x_split).call()
    result_split = execution_info.result
    low = pack(result_split[0], num_bits_shift=128)
    high = pack(result_split[1], num_bits_shift=128)
    result = low + 2**256 * high

    assert result == x * x


@given(
    x=st.integers(min_value=1, max_value=2**256 - 1),
    y=st.integers(min_value=1, max_value=2**256 - 1),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_unsigned_div_rem(x, y, uint256_contract):

    print(x, y)

    x_split = split(x, num_bits_shift=128, length=2)
    y_split = split(y, num_bits_shift=128, length=2)

    execution_info = await uint256_contract.uint256_unsigned_div_rem_new_c(
        x_split, y_split
    ).call()
    result_split = execution_info.result
    quotient = pack(result_split[0], num_bits_shift=128)
    reminder = pack(result_split[1], num_bits_shift=128)

    assert divmod(x, y) == (quotient, reminder)


@given(
    x=st.integers(min_value=1, max_value=2**256 - 1),
    y=st.integers(min_value=1, max_value=2**256 - 1),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_unsigned_div_rem_expanded(x, y, uint256_contract):

    print(x, y)

    x_split = split(x, num_bits_shift=128, length=2)
    y_split = split(y, num_bits_shift=128, length=2)

    execution_info = await uint256_contract.uint256_expand_c(y_split).call()
    y_exp = execution_info.result[0]
    execution_info = await uint256_contract.uint256_unsigned_div_rem_expanded_c(x_split, y_exp).call()
    result_split = execution_info.result
    quotient = pack(result_split[0], num_bits_shift=128)
    reminder = pack(result_split[1], num_bits_shift=128)

    assert divmod(x, y) == (quotient, reminder)


from starkware.python.math_utils import isqrt


@given(
    a=st.integers(min_value=1, max_value=2**256 - 1),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_sqrt(a, uint256_contract):

    print(a)
    a_split = split(a, num_bits_shift=128, length=2)

    execution_info = await uint256_contract.uint256_sqrt_new_c(a_split).call()
    result_split = execution_info.result
    result = pack(result_split[0], num_bits_shift=128)
    assert result == isqrt(a)
