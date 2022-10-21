import pytest
from utils import split, split2

@pytest.mark.asyncio
async def test_benchmark_uin256(uint256_contract):
    
    print("\n")
    print("uint256 benchmarks")
    print(
    "%20s" % "function",
    "|",
    "%20s" % "n_steps",
    "|",
    "%-10s" % "builtins",
    )


    x = 2 ** 250
    y = 2 ** 250

    x_split = split(x, num_bits_shift=128, length=2)
    y_split = split(y, num_bits_shift=128, length=2)

    execution_info = await uint256_contract.uint256_mul_c(x_split, y_split).call()
    
    print(
    "%20s" % "mul old",
    "|",
    "%20s" % execution_info.call_info.execution_resources.n_steps,
    "|",
    "%-10s" % execution_info.call_info.execution_resources.builtin_instance_counter,
    )

    execution_info = await uint256_contract.uint256_mul_new_c(x_split, y_split).call()
    
    print(
    "%20s" % "mul new",
    "|",
    "%20s" % execution_info.call_info.execution_resources.n_steps,
    "|",
    "%-10s" % execution_info.call_info.execution_resources.builtin_instance_counter,
    )
    
    execution_info = await uint256_contract.uint256_square_c(x_split).call()
    
    print(
    "%20s" % "square",
    "|",
    "%20s" % execution_info.call_info.execution_resources.n_steps,
    "|",
    "%-10s" % execution_info.call_info.execution_resources.builtin_instance_counter,
    )

    execution_info = await uint256_contract.uint256_unsigned_div_rem_c(x_split, y_split).call()
    
    print(
    "%20s" % "unsigned_div_rem old",
    "|",
    "%20s" % execution_info.call_info.execution_resources.n_steps,
    "|",
    "%-10s" % execution_info.call_info.execution_resources.builtin_instance_counter,
    )

    execution_info = await uint256_contract.uint256_unsigned_div_rem_new_c(x_split, y_split).call()
    
    print(
    "%20s" % "unsigned_div_rem new",
    "|",
    "%20s" % execution_info.call_info.execution_resources.n_steps,
    "|",
    "%-10s" % execution_info.call_info.execution_resources.builtin_instance_counter,
    )
    
    execution_info = await uint256_contract.uint256_sub_c(x_split, y_split).call()
    
    print(
    "%20s" % "sub old",
    "|",
    "%20s" % execution_info.call_info.execution_resources.n_steps,
    "|",
    "%-10s" % execution_info.call_info.execution_resources.builtin_instance_counter,
    )

    execution_info = await uint256_contract.uint256_sub_new_c(x_split, y_split).call()
    
    print(
    "%20s" % "sub new",
    "|",
    "%20s" % execution_info.call_info.execution_resources.n_steps,
    "|",
    "%-10s" % execution_info.call_info.execution_resources.builtin_instance_counter,
    )
    
    execution_info = await uint256_contract.uint256_sqrt_c(x_split).call()
    
    print(
    "%20s" % "sqrt old",
    "|",
    "%20s" % execution_info.call_info.execution_resources.n_steps,
    "|",
    "%-10s" % execution_info.call_info.execution_resources.builtin_instance_counter,
    )

    execution_info = await uint256_contract.uint256_sqrt_new_c(x_split).call()
    
    print(
    "%20s" % "sqrt new",
    "|",
    "%20s" % execution_info.call_info.execution_resources.n_steps,
    "|",
    "%-10s" % execution_info.call_info.execution_resources.builtin_instance_counter,
    )
