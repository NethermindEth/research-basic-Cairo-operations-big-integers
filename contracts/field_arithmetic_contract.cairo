// Declare this file as a StarkNet contract.
%lang starknet

from starkware.cairo.common.cairo_builtins import HashBuiltin, BitwiseBuiltin
// Import uint384 files (path may change in the future)
from lib.uint384 import uint384_lib, Uint384, Uint384_expand
from lib.uint384_extension import uint384_extension_lib, Uint768
from lib.field_arithmetic_new import field_arithmetic

// StarkNet contract implementing view calls to lib/fielf_arithmetic.cairo's functions

// Computes (a + b) modulo p
@view
func field_arithmetic_add{syscall_ptr: felt*, pedersen_ptr: HashBuiltin*, range_check_ptr}(
    a: Uint384, b: Uint384, p: Uint384_expand
) -> (res: Uint384) {
    let (res: Uint384) = field_arithmetic.add(a, b, p);
    return (res,);
}

// Computes (a - b) modulo p
@view
func field_arithmetic_sub{syscall_ptr: felt*, pedersen_ptr: HashBuiltin*, range_check_ptr}(
    a: Uint384, b: Uint384, p: Uint384_expand
) -> (res: Uint384) {
    let (res: Uint384) = field_arithmetic.sub_reduced_a_and_reduced_b(a, b, p);
    return (res,);
}

// Computes a * b modulo p
@view
func field_arithmetic_mul{syscall_ptr: felt*, pedersen_ptr: HashBuiltin*, range_check_ptr}(
    a: Uint384, b: Uint384, p: Uint384_expand
) -> (res: Uint384) {
    let (res: Uint384) = field_arithmetic.mul(a, b, p);
    return (res,);
}

@view
func uint384_expand{range_check_ptr}(a: Uint384) -> (e: Uint384_expand) {
    let (e: Uint384_expand) = uint384_lib.expand(a);
    return (e=e);
}


@view
func field_arithmetic_mul_expanded{syscall_ptr: felt*, pedersen_ptr: HashBuiltin*, range_check_ptr}(
    a: Uint384, b: Uint384_expand, p: Uint384_expand
) -> (res: Uint384) {
    let (res: Uint384) = field_arithmetic.mul_expanded(a, b, p);
    return (res,);
}

// Computes a ** 2 modulo p
@view
func field_arithmetic_square{syscall_ptr: felt*, pedersen_ptr: HashBuiltin*, range_check_ptr}(
    a: Uint384, p: Uint384_expand
) -> (res: Uint384) {
    let (res: Uint384) = field_arithmetic.square(a, p);
    return (res,);
}

// Computes a ** 3 modulo p
@view
func field_arithmetic_cube{syscall_ptr: felt*, pedersen_ptr: HashBuiltin*, range_check_ptr}(
    a: Uint384, p: Uint384_expand
) -> (res: Uint384) {
    let (res: Uint384) = field_arithmetic.cube(a, p);
    return (res,);
}

// Computes a * b^{-1} modulo p
@view
func field_arithmetic_div{syscall_ptr: felt*, pedersen_ptr: HashBuiltin*, range_check_ptr}(
    a: Uint384, b: Uint384, p: Uint384_expand
) -> (res: Uint384) {
    let (res: Uint384) = field_arithmetic.div(a, b, p);
    return (res,);
}

@view
func field_arithmetic_div_b{syscall_ptr: felt*, pedersen_ptr: HashBuiltin*, range_check_ptr}(
    a: Uint384, b: Uint384, p: Uint384_expand
) -> (res: Uint384) {
    let (res: Uint384) = field_arithmetic.div_b(a, b, p);
    return (res,);
}

// Computes (a**exp) % p
@view
func field_arithmetic_pow{syscall_ptr: felt*, pedersen_ptr: HashBuiltin*, range_check_ptr}(
    a: Uint384, exp: Uint384, p: Uint384_expand
) -> (res: Uint384) {
    let (res: Uint384) = field_arithmetic.pow(a, exp, p);
    return (res,);
}

// Computes (a**exp) % p
@view
func field_arithmetic_pow_b{syscall_ptr: felt*, pedersen_ptr: HashBuiltin*, range_check_ptr}(
    a: Uint384, exp: Uint384, p: Uint384_expand
) -> (res: Uint384) {
    let (res: Uint384) = field_arithmetic.pow_b(a, exp, p);
    return (res,);
}

// Computes (a**exp) % p
@view
func field_arithmetic_pow_c{syscall_ptr: felt*, pedersen_ptr: HashBuiltin*, range_check_ptr}(
    a: Uint384, exp: Uint384, p: Uint384_expand
) -> (res: Uint384) {
    let (res: Uint384) = field_arithmetic.pow_c(a, exp, p);
    return (res,);
}

// DEPRECATED
@view
func is_square_non_optimized{
    syscall_ptr: felt*, pedersen_ptr: HashBuiltin*, bitwise_ptr: BitwiseBuiltin*, range_check_ptr
}(x: Uint384, p: Uint384_expand, p_minus_one_div_2: Uint384) -> (bool: felt) {
    alloc_locals;

    let (bool) = field_arithmetic.is_square_non_optimized(x, p, p_minus_one_div_2);

    return (bool,);
}

// generator : generator of F_p
@view
func get_square_root{
    syscall_ptr: felt*, pedersen_ptr: HashBuiltin*, bitwise_ptr: BitwiseBuiltin*, range_check_ptr
}(x: Uint384, p: Uint384_expand, generator: Uint384) -> (bool: felt, res: Uint384) {
    alloc_locals;

    let (bool, res: Uint384) = field_arithmetic.get_square_root(x, p, generator);

    return (bool, res);
}
