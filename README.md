# 384-bit prime field arithmetic - Cairo

Cairo implementation of operations between elements of a prime field $\mathbb{F}_p$ (i.e. operations modulo a prime p) with p of up to 384 bits. (Note that Cairo's native "integer" is of 251 bits)

The implemented operations are:

- addition and subtraction modulo p
- multiplication modulo p
- division (i.e.\ multiplication by the modular inverse) modulo p
- exponentiation modulo p

The library depends on the [uint384-cairo](https://github.com/NethermindEth/uint384-cairo) library. Specifically, it uses the struct `Uint384` to represent 384-bit integers, which consists of three 128-bit felts (as Cairo's common library struct `Uint256`). It is important to never use felts larger than this as members of a `Uint384`.

The auxiliary libray `uint384_extension` implements some extra functions involving operations between 384-bit integers and 768-bit integers. These are needed in `field_arithmetic.cairo` (there's some more details below in the technical notes)

The project is structured following Nile's framework.

Tests are provided for all functions.

## Technical notes

- The exponentiation function follows the "[fast exponentiation algorithm](https://en.wikipedia.org/wiki/Exponentiation_by_squaring)" so as to perform `log(exponent)` of multiplications.
- As in the common library `uint256`, division operations are performed in python hints, and verified afterwards in Cairo using multiplication and addition operations.
- `uint384_extension` implements the function `unsigned_div_rem_uint768_by_uint384` which computes the quotient and remainder of dividing a 768-bit integer by a 384-bit integer. This allows to multiply two 384-bit integers (obtaining a 768-bit integer) and then reduce the result modulo a 384-bit integer by calling this function. This is a key component of this repository.
