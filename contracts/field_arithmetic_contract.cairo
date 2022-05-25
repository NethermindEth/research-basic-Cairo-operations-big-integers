# Declare this file as a StarkNet contract.
%lang starknet

from starkware.cairo.common.cairo_builtins import HashBuiltin
from lib.uint384 import uint384_lib, Uint384
from lib.uint384_extension import uint384_extension_lib, Uint768
from lib.field_arithmetic import field_arithmetic

# StarkNet contract implementing view calls to lib/fielf_arithmetic.cairo's functions

# Computes (a + b) modulo p
@view
func field_arithmetic_add{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    a : Uint384, b : Uint384, p : Uint384
) -> (res : Uint384):
    let (res : Uint384) = field_arithmetic.add(a, b, p)
    return (res)
end

# Computes (a - b) modulo p
@view
func field_arithmetic_sub{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    a : Uint384, b : Uint384, p : Uint384
) -> (res : Uint384):
    let (res : Uint384) = field_arithmetic.sub_reduced_a_and_reduced_b(a, b, p)
    return (res)
end

# Computes a * b modulo p
@view
func field_arithmetic_mul{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    a : Uint384, b : Uint384, p : Uint384
) -> (res : Uint384):
    let (res : Uint384) = field_arithmetic.mul(a, b, p)
    return (res)
end

# Computes a * b^{-1} modulo p
@view
func field_arithmetic_div{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    a : Uint384, b : Uint384, p : Uint384
) -> (res : Uint384):
    let (res : Uint384) = field_arithmetic.div(a, b, p)
    return (res)
end

# Computes (a**exp) % p
@view
func field_arithmetic_pow{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    a : Uint384, exp : Uint384, p : Uint384
) -> (res : Uint384):
    let (res : Uint384) = field_arithmetic.pow(a, exp, p)
    return (res)
end