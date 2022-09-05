import pytest
from hypothesis import given, strategies as st, settings
from utils import split, pack

# Tests all functions from uint384_contract 

@given(
    x=st.integers(min_value=1, max_value=2**384 - 1),
    y=st.integers(min_value=1, max_value=2**384 - 1),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_eq(x, y, uint384_contract):

    print(x, y)

    x_split = split(x, num_bits_shift=128, length=3)
    y_split = split(y, num_bits_shift=128, length=3)

    execution_info = await uint384_contract.uint384_eq(x_split, y_split).call()
    result = execution_info.result[0]

    is_eq = x == y
    assert result == is_eq


@given(
    x=st.integers(min_value=1, max_value=2**384 - 1),
    y=st.integers(min_value=1, max_value=2**384 - 1),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_add(x, y, uint384_contract):

    print(x, y)

    x_split = split(x, num_bits_shift=128, length=3)
    y_split = split(y, num_bits_shift=128, length=3)

    execution_info = await uint384_contract.uint384_add(x_split, y_split).call()
    result_no_carry, carry = execution_info.result
    result = pack(result_no_carry, num_bits_shift=128) + 2**384 * carry

    assert result == x + y


@given(
    x=st.integers(min_value=1, max_value=2**384 - 1),
    y=st.integers(min_value=1, max_value=2**384 - 1),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_sub(x, y, uint384_contract):

    x_split = split(x, num_bits_shift=128, length=3)
    y_split = split(y, num_bits_shift=128, length=3)

    execution_info = await uint384_contract.uint384_sub(x_split, y_split).call()
    result_no_carry = execution_info.result[0]
    result = pack(result_no_carry, num_bits_shift=128)

    if y > x:
        temp = result - 2**384
        print(temp)
        assert temp == x - y
    else:
        assert result == x - y


@given(
    x=st.integers(min_value=1, max_value=2**384 - 1),
    y=st.integers(min_value=1, max_value=2**384 - 1),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_mul(x, y, uint384_contract):

    print(x, y)

    x_split = split(x, num_bits_shift=128, length=3)
    y_split = split(y, num_bits_shift=128, length=3)

    execution_info = await uint384_contract.uint384_mul_c(x_split, y_split).call()
    result_split = execution_info.result
    low = pack(result_split[0], num_bits_shift=128)
    high = pack(result_split[1], num_bits_shift=128)
    result = low + 2**384 * high

    assert result == x * y


@given(
    x=st.integers(min_value=1, max_value=2**384 - 1),
    y=st.integers(min_value=1, max_value=2**384 - 1),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_unsigned_div_rem(x, y, uint384_contract):

    print(x, y)

    x_split = split(x, num_bits_shift=128, length=3)
    y_split = split(y, num_bits_shift=128, length=3)

    execution_info = await uint384_contract.uint384_unsigned_div_rem(
        x_split, y_split
    ).call()
    result_split = execution_info.result
    quotient = pack(result_split[0], num_bits_shift=128)
    reminder = pack(result_split[1], num_bits_shift=128)

    assert divmod(x, y) == (quotient, reminder)


@given(
    x=st.integers(min_value=1, max_value=2**384 - 1),
    y=st.integers(min_value=1, max_value=2**384 - 1),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_bitwise_xor_and_or(x, y, uint384_contract):

    print(x, y)

    x_split = split(x, num_bits_shift=128, length=3)
    y_split = split(y, num_bits_shift=128, length=3)

    # xor test
    execution_info = await uint384_contract.uint384_xor(x_split, y_split).call()
    result_split = execution_info.result
    result = pack(result_split[0], num_bits_shift=128)
    assert result == x ^ y

    # and test
    execution_info = await uint384_contract.uint384_and(x_split, y_split).call()
    result_split = execution_info.result
    result = pack(result_split[0], num_bits_shift=128)
    assert result == x & y

    # or test
    execution_info = await uint384_contract.uint384_or(x_split, y_split).call()
    result_split = execution_info.result
    result = pack(result_split[0], num_bits_shift=128)
    assert result == x | y


@given(
    x=st.integers(min_value=1, max_value=2**384 - 1),
    y=st.integers(min_value=1, max_value=2**384 - 1),
)
@settings(deadline=None)
# TODO: redo this test
# @pytest.mark.skip
@pytest.mark.asyncio
async def test_left_and_right_bitwise_shift(x, y, uint384_contract):

    print(x, y)

    x_split = split(x, num_bits_shift=128, length=3)
    y_split = split(y, num_bits_shift=128, length=3)

    # shl test
    execution_info = await uint384_contract.uint384_shl(x_split, y_split).call()
    result_split = execution_info.result
    result = pack(result_split[0], num_bits_shift=128)
    # Note that any y not less than 384 will result in a 0 after reducing modulo 2**384, so we can clip y (else python overflows)
    assert result == (x << min(384,y)) % 2**384

    # sht test
    execution_info = await uint384_contract.uint384_shr(x_split, y_split).call()
    result_split = execution_info.result
    result = pack(result_split[0], num_bits_shift=128)
    assert result == (x >> min(384,y)) % 2**384


# Auxiliary function used in the test above
def modular_multiplication(a, b, mod):
    res = 0
    a = a % mod
    while b != 0:
        print(b)
        if b % 2 == 1:
            res = (res + a) % mod
        a = (2 * a) % mod
        b >>= 1
    return res

@given(
    exp=st.integers(min_value=1, max_value=2**100),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_pow2(exp, uint384_contract):

    print(exp)
    exp_split = split(exp, num_bits_shift=128, length=3)

    execution_info = await uint384_contract.uint384_pow2(exp_split).call()
    result_split = execution_info.result
    result = pack(result_split[0], num_bits_shift=128)
    assert result == pow(2, exp, 2**384)


from starkware.python.math_utils import isqrt


@given(
    a=st.integers(min_value=1, max_value=2**384 - 1),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_sqrt(a, uint384_contract):

    print(a)
    a_split = split(a, num_bits_shift=128, length=3)

    execution_info = await uint384_contract.uint384_sqrt(a_split).call()
    result_split = execution_info.result
    result = pack(result_split[0], num_bits_shift=128)
    assert result == isqrt(a)


@given(
    a=st.integers(min_value=1, max_value=2**384 - 1),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_reverse_endian(a, uint384_contract):

    print(a)
    a_split = split(a, num_bits_shift=128, length=3)

    execution_info = await uint384_contract.uint384_reverse_endian(a_split).call()
    result = pack(execution_info.result[0], num_bits_shift=128)
    a_reversed = int.from_bytes(
        a.to_bytes(48, byteorder="little"), byteorder="big", signed=False
    )
    assert result == a_reversed


@given(
    a=st.integers(min_value=1, max_value=2**384 - 1),
    b=st.integers(min_value=1, max_value=2**384 - 1),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_unsigned_comparison_functions(a, b, uint384_contract):

    print(a, b)
    a_split = split(a, num_bits_shift=128, length=3)
    b_split = split(b, num_bits_shift=128, length=3)

    execution_info = await uint384_contract.uint384_lt(a_split, b_split).call()
    result = bool(execution_info.result[0])
    assert result == (a < b)

    execution_info = await uint384_contract.uint384_le(a_split, b_split).call()
    result = bool(execution_info.result[0])
    assert result == (a <= b)


@given(
    a=st.integers(min_value=1, max_value=2**384 - 1),
    b=st.integers(min_value=1, max_value=2**384 - 1),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_signed_comparison_functions(a, b, uint384_contract):

    print(a, b)
    a_split = split(a, num_bits_shift=128, length=3)
    b_split = split(b, num_bits_shift=128, length=3)

    signed_a = get_signed_int(a)
    signed_b = get_signed_int(b)

    print(signed_a, signed_b)
    print()

    execution_info = await uint384_contract.uint384_signed_lt(a_split, b_split).call()
    result = bool(execution_info.result[0])
    assert result == (signed_a < signed_b)

    execution_info = await uint384_contract.uint384_signed_le(a_split, b_split).call()
    result = bool(execution_info.result[0])
    assert result == (signed_a <= signed_b)

    execution_info = await uint384_contract.uint384_signed_nn(a_split).call()
    result = bool(execution_info.result[0])
    assert result == (signed_a >= 0)

    execution_info = await uint384_contract.uint384_signed_nn_le(
        a_split, b_split
    ).call()
    result = bool(execution_info.result[0])
    assert result == ((signed_a >= 0) and (signed_a <= signed_b))


def get_signed_int(num):
    if num < 2**383:
        return num
    else:
        return num - 2**384


def get_unsigned_int(num):
    if num >= 0:
        return num
    else:
        return num + 2**384


# Signed integer division between two integers x,y. Returns the quotient and the remainder.
# NOTE: This function tests that, (y*quotient + remainder) % 2**383 == x, where
# (quotient, remainder) is the result of calling signed_div_rem on x and y
@given(
    x=st.integers(min_value=1, max_value=2**384 - 1),
    y=st.integers(min_value=1, max_value=2**384 - 1),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_signed_div_rem(x, y, uint384_contract):

    print(x, y)

    x_split = split(x, num_bits_shift=128, length=3)
    y_split = split(y, num_bits_shift=128, length=3)

    execution_info = await uint384_contract.uint384_signed_div_rem(
        x_split, y_split
    ).call()
    result_split = execution_info.result
    quotient = pack(result_split[0], num_bits_shift=128)
    reminder = pack(result_split[1], num_bits_shift=128)

    res = (y * quotient + reminder) % (2**384)
    assert x == res
