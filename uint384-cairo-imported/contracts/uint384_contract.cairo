# Declare this file as a StarkNet contract.
%lang starknet

from starkware.cairo.common.cairo_builtins import HashBuiltin, BitwiseBuiltin
from starkware.cairo.common.uint256 import Uint256, uint256_sqrt
from lib.uint384 import uint384_lib, Uint384

# StarkNet contract implementing view calls to lib/uint384.cairo's functions

# Adds two integers. Returns the result as a 384-bit integer and the (1-bit) carry.
@view
func uint384_add{range_check_ptr}(a : Uint384, b : Uint384) -> (res : Uint384, carry : felt):
    let (res : Uint384, carry : felt) = uint384_lib.add(a, b)
    return (res, carry)
end

# Multiplies two integers. Returns the result as two 384-bit integers (low and high parts).
@view
func uint384_mul{range_check_ptr}(a : Uint384, b : Uint384) -> (low : Uint384, high : Uint384):
    let (low : Uint384, high : Uint384) = uint384_lib.mul(a, b)
    return (low, high)
end

# Returns the floor value of the square root of a Uint384 integer.
@view
func uint384_sqrt{range_check_ptr}(a : Uint384) -> (res : Uint384):
    let (res) = uint384_lib.sqrt(a)
    return (res)
end

# Returns 1 if the first unsigned integer is less than the second signed integer
@view
func uint384_lt{range_check_ptr}(a : Uint384, b : Uint384) -> (res):
    let (res) = uint384_lib.lt(a, b)
    return (res)
end

# Returns 1 if the first signed integer is less than the second signed integer
@view
func uint384_signed_lt{range_check_ptr}(a : Uint384, b : Uint384) -> (res):
    let (res) = uint384_lib.signed_lt(a, b)
    return (res)
end

# Returns 1 if the first unsigned integer is less than or equal to the second signed integer.
@view
func uint384_le{range_check_ptr}(a : Uint384, b : Uint384) -> (res):
    let (res) = uint384_lib.le(a, b)
    return (res)
end

# Returns 1 if the first signed integer is less than or equal to the second signed integer.
@view
func uint384_signed_le{range_check_ptr}(a : Uint384, b : Uint384) -> (res):
    let (res) = uint384_lib.signed_le(a, b)
    return (res)
end

# Returns 1 if the signed integer is nonnegative.
@view
func uint384_signed_nn{range_check_ptr}(a : Uint384) -> (res):
    let (res) = uint384_lib.signed_nn(a)
    return (res)
end

# Returns 1 if the first signed integer is less than or equal to the second signed integer
# and is greater than or equal to zero.
@view
func uint384_signed_nn_le{range_check_ptr}(a : Uint384, b : Uint384) -> (res):
    let (res) = uint384_lib.signed_nn_le(a, b)
    return (res)
end

# Unsigned integer division between two integers. Returns the quotient and the remainder.
# Conforms to EVM specifications: division by 0 yields 0.
@view
func uint384_unsigned_div_rem{range_check_ptr}(a : Uint384, div : Uint384) -> (
    quotient : Uint384, remainder : Uint384
):
    let (quotient : Uint384, remainder : Uint384) = uint384_lib.unsigned_div_rem(a, div)
    return (quotient, remainder)
end

# Signed integer division between two integers. Returns the quotient and the remainder.
@view
func uint384_signed_div_rem{range_check_ptr}(a : Uint384, div : Uint384) -> (
    quot : Uint384, rem : Uint384
):
    let (quot, rem) = uint384_lib.signed_div_rem(a, div)
    return (quot, rem)
end

# Subtracts one integer from another. Returns the result as a 384-bit integer.
@view
func uint384_sub{range_check_ptr}(a : Uint384, b : Uint384) -> (res : Uint384):
    let (res : Uint384) = uint384_lib.sub(a, b)
    return (res)
end

# Subtracts one integer from another. Returns the result as a felt (0 false, 1 true).
@view
func uint384_eq{range_check_ptr}(a : Uint384, b : Uint384) -> (res : felt):
    let (res : felt) = uint384_lib.eq(a, b)
    return (res)
end

# Computes the bitwise XOR of 2 uint384 integers.
@view
func uint384_xor{bitwise_ptr : BitwiseBuiltin*, range_check_ptr}(a : Uint384, b : Uint384) -> (
    res : Uint384
):
    let (res) = uint384_lib.xor(a, b)
    return (res)
end

# Computes the bitwise AND of 2 uint384 integers.
@view
func uint384_and{bitwise_ptr : BitwiseBuiltin*, range_check_ptr}(a : Uint384, b : Uint384) -> (
    res : Uint384
):
    let (res) = uint384_lib.and(a, b)
    return (res)
end

# Computes the bitwise OR of 2 uint384 integers.
@view
func uint384_or{bitwise_ptr : BitwiseBuiltin*, range_check_ptr}(a : Uint384, b : Uint384) -> (
    res : Uint384
):
    let (res) = uint384_lib.or(a, b)
    return (res)
end

# Computes 2**exp % 2**384 as a uint384 integer.
@view
func uint384_pow2{range_check_ptr}(exp : Uint384) -> (res : Uint384):
    let (res) = uint384_lib.pow2(exp)
    return (res)
end

# Computes the bitwise left shift of 2 uint384 integers.
@view
func uint384_shl{bitwise_ptr : BitwiseBuiltin*, range_check_ptr}(a : Uint384, b : Uint384) -> (
    res : Uint384
):
    let (res) = uint384_lib.shl(a, b)
    return (res)
end

# Computes the bitwise right shift of 2 uint384 integers.
@view
func uint384_shr{bitwise_ptr : BitwiseBuiltin*, range_check_ptr}(a : Uint384, b : Uint384) -> (
    res : Uint384
):
    let (res) = uint384_lib.shr(a, b)
    return (res)
end

# Reverses byte endianness of a uint384 integer.
@view
func uint384_reverse_endian{bitwise_ptr : BitwiseBuiltin*, range_check_ptr}(num : Uint384) -> (
    res : Uint384
):
    let (res) = uint384_lib.reverse_endian(num)
    return (res)
end
