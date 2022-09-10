import pytest
from hypothesis import given, strategies as st, settings
from utils import split, pack


#@given(
#    x=2**384 - 1,
#    y=2**384 - 1,
#)
#@settings(deadline=None)
@pytest.mark.asyncio
async def test_mul( uint384_contract):

    x=2**384 - 1
    y=2**384 - 1
    print(x, y)

    x_split = split(x, num_bits_shift=128, length=3)
    y_split = split(y, num_bits_shift=128, length=3)

    print("\n")
    print(
    "%20s" % "function",
    "|",
    "%20s" % "n_steps",
    "|",
    "%-10s" % "builtins",
    )

    execution_info = await uint384_contract.uint384_mul(x_split, y_split).call()

    print(  
    "%20s" % "mul",
    "|",
    "%20s" % execution_info.call_info.execution_resources.n_steps,
    "|",
    "%-10s" % execution_info.call_info.execution_resources.builtin_instance_counter,
    )

    result_split = execution_info.result
    low = pack(result_split[0], num_bits_shift=128)
    high = pack(result_split[1], num_bits_shift=128)
    result = low + 2**384 * high

    assert result == x * y
    
    execution_info = await uint384_contract.uint384_mul_b(x_split, y_split).call()

    print(  
    "%20s" % "mul b",
    "|",
    "%20s" % execution_info.call_info.execution_resources.n_steps,
    "|",
    "%-10s" % execution_info.call_info.execution_resources.builtin_instance_counter,
    )

    result_split = execution_info.result
    low = pack(result_split[0], num_bits_shift=128)
    high = pack(result_split[1], num_bits_shift=128)
    result = low + 2**384 * high

    assert result == x * y

    execution_info = await uint384_contract.uint384_mul_c(x_split, y_split).call()

    print(  
    "%20s" % "mul c",
    "|",
    "%20s" % execution_info.call_info.execution_resources.n_steps,
    "|",
    "%-10s" % execution_info.call_info.execution_resources.builtin_instance_counter,
    )

    result_split = execution_info.result
    low = pack(result_split[0], num_bits_shift=128)
    high = pack(result_split[1], num_bits_shift=128)
    result = low + 2**384 * high

    assert result == x * y

    execution_info = await uint384_contract.uint384_mul_Toom3(x_split, y_split).call()

    print(  
    "%20s" % "mul Toom3",
    "|",
    "%20s" % execution_info.call_info.execution_resources.n_steps,
    "|",
    "%-10s" % execution_info.call_info.execution_resources.builtin_instance_counter,
    )

    result_split = execution_info.result
    low = pack(result_split[0], num_bits_shift=128)
    high = pack(result_split[1], num_bits_shift=128)
    result = low + 2**384 * high

    assert result == x * y

    execution_info = await uint384_contract.uint384_mul_mont(x_split, y_split).call()

    print(  
    "%20s" % "mul mont",
    "|",
    "%20s" % execution_info.call_info.execution_resources.n_steps,
    "|",
    "%-10s" % execution_info.call_info.execution_resources.builtin_instance_counter,
    )

    result_split = execution_info.result
    low = pack(result_split[0], num_bits_shift=128)
    high = pack(result_split[1], num_bits_shift=128)
    result = low + 2**384 * high

    assert result == x * y

    execution_info = await uint384_contract.uint384_mul_s(x_split, y_split).call()

    print(  
    "%20s" % "mul s",
    "|",
    "%20s" % execution_info.call_info.execution_resources.n_steps,
    "|",
    "%-10s" % execution_info.call_info.execution_resources.builtin_instance_counter,
    )

    result_split = execution_info.result
    low = pack(result_split[0], num_bits_shift=128)
    high = pack(result_split[1], num_bits_shift=128)
    result = low + 2**384 * high

    assert result == x * y
