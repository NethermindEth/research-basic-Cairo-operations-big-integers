from typing import List, Tuple

# Takes an integer `num`, a number of bits `n_b`, and a length l, and returns a tuple (d0, ..., d_{l-1})
# such that num = d_0 + d_1 * 2**(n_b) + d_2 * 2**(2n_b) + ... + d_{l-1}*2**((l-1)*n_b)
# Each d_i is a positive integer of less than n_b bits
def split(num: int, num_bits_shift: int = 128, length: int=3) -> List[int]:
    a = []
    for _ in range(length):
        a.append( num & ((1 << num_bits_shift) - 1) )
        num = num >> num_bits_shift 
    return tuple(a)

# The inverse operation of `split`: takes a tuple z of integers (d0, ..., d_{l-1}) and returns
# d_0 + d_1 * 2**(n_b) + d_2 * 2**(2n_b) + ... + d_{l-1}*2**((l-1)*n_b)
# Note that d_i can be larger than 2**128 here (but in this repo d_i is always less than 2**128)
def pack(z: Tuple[int], num_bits_shift: int = 128) -> int:
    limbs = (limb for limb in z)
    return sum(limb << (num_bits_shift * i) for i, limb in enumerate(limbs))

# Prime p with which to test the field arithmetic functions
elliptic_curve_field_modulus = 4002409555221667393417789825735904156556882819939007885332058136124031650490837864442687629129015664037894272559787
