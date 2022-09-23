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

    execution_info = await uint384_contract.uint384_mul_d(x_split, y_split).call()

    print(  
    "%20s" % "mul d",
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

    execution_info = await uint384_contract.uint384_mul_kar(x_split, y_split).call()

    print(  
    "%20s" % "mul kar",
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

    execution_info = await uint384_contract.uint384_square_c(x_split).call()

    print(  
    "%20s" % "square c",
    "|",
    "%20s" % execution_info.call_info.execution_resources.n_steps,
    "|",
    "%-10s" % execution_info.call_info.execution_resources.builtin_instance_counter,
    )

    result_split = execution_info.result
    low = pack(result_split[0], num_bits_shift=128)
    high = pack(result_split[1], num_bits_shift=128)
    result = low + 2**384 * high

    assert result == x * x
    
    execution_info = await uint384_contract.uint384_square_d(x_split).call()

    print(  
    "%20s" % "square d",
    "|",
    "%20s" % execution_info.call_info.execution_resources.n_steps,
    "|",
    "%-10s" % execution_info.call_info.execution_resources.builtin_instance_counter,
    )

    result_split = execution_info.result
    low = pack(result_split[0], num_bits_shift=128)
    high = pack(result_split[1], num_bits_shift=128)
    result = low + 2**384 * high

    assert result == x * x
    
    execution_info = await uint384_contract.uint384_square_e(x_split).call()

    print(  
    "%20s" % "square e",
    "|",
    "%20s" % execution_info.call_info.execution_resources.n_steps,
    "|",
    "%-10s" % execution_info.call_info.execution_resources.builtin_instance_counter,
    )

    result_split = execution_info.result
    low = pack(result_split[0], num_bits_shift=128)
    high = pack(result_split[1], num_bits_shift=128)
    result = low + 2**384 * high

    assert result == x * x


@pytest.mark.asyncio
async def test_ext_mul( uint384_extension_contract):

    x=2**768 - 1
    y=2**384 - 1
    print(x, y)

    x_split = split(x, num_bits_shift=128, length=6)
    y_split = split(y, num_bits_shift=128, length=3)

    print("\n")
    print(
    "%20s" % "function",
    "|",
    "%20s" % "n_steps",
    "|",
    "%-10s" % "builtins",
    )

    execution_info = await uint384_extension_contract.uint384_mul_uint768_by_uint384(x_split, y_split).call()

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
    result = low + 2**768 * high

    assert result == x * y

    execution_info = await uint384_extension_contract.uint384_mul_uint768_by_uint384_c(x_split, y_split).call()

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
    result = low + 2**768 * high

    assert result == x * y

    execution_info = await uint384_extension_contract.uint384_mul_uint768_by_uint384_d(x_split, y_split).call()

    print(  
    "%20s" % "mul d",
    "|",
    "%20s" % execution_info.call_info.execution_resources.n_steps,
    "|",
    "%-10s" % execution_info.call_info.execution_resources.builtin_instance_counter,
    )

    result_split = execution_info.result
    low = pack(result_split[0], num_bits_shift=128)
    high = pack(result_split[1], num_bits_shift=128)
    result = low + 2**768 * high

    assert result == x * y

    execution_info = await uint384_extension_contract.uint384_mul_uint768_by_uint384_kar(x_split, y_split).call()

    print(  
    "%20s" % "mul kar",
    "|",
    "%20s" % execution_info.call_info.execution_resources.n_steps,
    "|",
    "%-10s" % execution_info.call_info.execution_resources.builtin_instance_counter,
    )

    result_split = execution_info.result
    low = pack(result_split[0], num_bits_shift=128)
    high = pack(result_split[1], num_bits_shift=128)
    result = low + 2**768 * high

    assert result == x * y

    execution_info = await uint384_extension_contract.uint384_mul_uint768_by_uint384_kar_d(x_split, y_split).call()

    print(  
    "%20s" % "mul kar d",
    "|",
    "%20s" % execution_info.call_info.execution_resources.n_steps,
    "|",
    "%-10s" % execution_info.call_info.execution_resources.builtin_instance_counter,
    )

    result_split = execution_info.result
    low = pack(result_split[0], num_bits_shift=128)
    high = pack(result_split[1], num_bits_shift=128)
    result = low + 2**768 * high

    assert result == x * y

    execution_info = await uint384_extension_contract.uint384_mul_uint768_by_uint384_Toom25(x_split, y_split).call()

    print(  
    "%20s" % "mul Toom 2.5",
    "|",
    "%20s" % execution_info.call_info.execution_resources.n_steps,
    "|",
    "%-10s" % execution_info.call_info.execution_resources.builtin_instance_counter,
    )
    
    result_split = execution_info.result
    low = pack(result_split[0], num_bits_shift=128)
    high = pack(result_split[1], num_bits_shift=128)
    result = low + 2**768 * high

    assert result == x * y
