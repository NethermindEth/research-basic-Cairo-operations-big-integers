// Declare this file as a StarkNet contract.
%lang starknet

from starkware.cairo.common.cairo_builtins import HashBuiltin, BitwiseBuiltin
from starkware.cairo.common.uint256 import(
    Uint256,
    uint256_mul,
    uint256_sub,
    uint256_unsigned_div_rem,
    uint256_sqrt
)
from lib.uint256_improvements import(
    uint256_mul as uint256_mul_new,
    uint256_square,
    uint256_sub as uint256_sub_new,
    uint256_unsigned_div_rem as uint256_unsigned_div_rem_new,
    uint256_sqrt as uint256_sqrt_new,
    Uint256_expand,
    uint256_expand,
    uint256_mul_expanded,
    uint256_unsigned_div_rem_expanded
)

@view
func uint256_mul_c{range_check_ptr}(a: Uint256, b: Uint256) -> (low: Uint256, high: Uint256) {
    let (low: Uint256, high: Uint256) = uint256_mul(a, b);
    return (low, high);
}

@view
func uint256_mul_new_c{range_check_ptr}(a: Uint256, b: Uint256) -> (low: Uint256, high: Uint256) {
    let (low: Uint256, high: Uint256) = uint256_mul_new(a, b);
    return (low, high);
}

@view
func uint256_square_c{range_check_ptr}(a: Uint256) -> (low: Uint256, high: Uint256) {
    let (low: Uint256, high: Uint256) = uint256_square(a);
    return (low, high);
}

@view
func uint256_sub_c{range_check_ptr}(a: Uint256, b: Uint256) -> (res: Uint256) {
    let (res: Uint256) = uint256_sub(a, b);
    return (res,);
}

@view
func uint256_sub_new_c{range_check_ptr}(a: Uint256, b: Uint256) -> (res: Uint256, sign: felt) {
  let (res: Uint256, sign: felt) = uint256_sub_new(a, b);
    return (res, sign);
}

@view
func uint256_sqrt_c{range_check_ptr}(a: Uint256) -> (res: Uint256) {
    let (res: Uint256) = uint256_sqrt(a);
    return (res,);
}

@view
func uint256_sqrt_new_c{range_check_ptr}(a: Uint256) -> (res: Uint256) {
    let (res: Uint256) = uint256_sqrt_new(a);
    return (res,);
}

// Unsigned integer division between two integers. Returns the quotient and the remainder.
// Conforms to EVM specifications: division by 0 yields 0.
@view
func uint256_unsigned_div_rem_c{range_check_ptr}(a: Uint256, div: Uint256) -> (
    quotient: Uint256, remainder: Uint256
) {
    let (quotient: Uint256, remainder: Uint256) = uint256_unsigned_div_rem(a, div);
    return (quotient, remainder);
}

@view
func uint256_unsigned_div_rem_new_c{range_check_ptr}(a: Uint256, div: Uint256) -> (
    quotient: Uint256, remainder: Uint256
) {
    let (quotient: Uint256, remainder: Uint256) = uint256_unsigned_div_rem_new(a, div);
    return (quotient, remainder);
}

@view
func uint256_expand_c{range_check_ptr}(a: Uint256) -> (e: Uint256_expand) {
    let (e: Uint256_expand) = uint256_expand(a);
    return (e=e);
}

@view
func uint256_mul_expanded_c{range_check_ptr}(a: Uint256, b: Uint256_expand) -> (low: Uint256, high: Uint256) {
    let (low: Uint256, high: Uint256) = uint256_mul_expanded(a, b);
    return (low, high);
}

@view
func uint256_unsigned_div_rem_expanded_c{range_check_ptr}(a: Uint256, div: Uint256_expand) -> (
    quotient: Uint256, remainder: Uint256
) {
    let (quotient: Uint256, remainder: Uint256) = uint256_unsigned_div_rem_expanded(a, div);
    return (quotient, remainder);
}
