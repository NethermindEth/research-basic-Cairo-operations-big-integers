# 384-bit prime field arithmetic - Cairo

WARNING: The latest version of asyncio (>=0.19.0) is not supported. To downgrade do `pip install pytest-asyncio==0.18.3`


We  implement the following libraries:

### `field_arithmetic`
Cairo implementation of operations between elements of a prime field $\mathbb{F}_p$ (i.e. operations modulo a prime p) with p of up to 384 bits. (Note that Cairo's native "integer" is of 251 bits)

**NOTE**: Most hints were whitelisted on Cairo v0.9.1 (20 Jul 2022). It is possible that some subsequent repo updates use or will use hints which are not whitelisted.

The implemented operations are:

- addition and subtraction modulo p
- multiplication modulo p
- division (i.e.\ multiplication by the modular inverse) modulo p
- exponentiation modulo p


### `uint384`
This follows and extends `uint256` from Cairo's common library to 384 bits. The usage and logic is almost the same as in `uint256`. All operations from `uint256` are implemented here for 384 bits.

Specifically, a `Uint384` represents 384-bit integers with three 128-bit felts. It is important to never use felts larger than this as members of a `Uint384`.

### `uint384_extension` 

This implements some extra functions involving operations between 384-bit integers and 768-bit integers. These are needed in `field_arithmetic.cairo` (there's some more details below in the technical notes)

## Tests

Tests are provided for all functions.

## Technical notes

- The project is structured following Nile's framework.
- The exponentiation function follows the "[fast exponentiation algorithm](https://en.wikipedia.org/wiki/Exponentiation_by_squaring)" so as to perform `log(exponent)` of multiplications.
- As in the common library `uint256`, division operations are performed in python hints, and verified afterwards in Cairo using multiplication and addition operations.
- `uint384_extension` implements the function `unsigned_div_rem_uint768_by_uint384` which computes the quotient and remainder of dividing a 768-bit integer by a 384-bit integer. This allows to multiply two 384-bit integers (obtaining a 768-bit integer) and then reduce the result modulo a 384-bit integer by calling this function. This is a key component of this repository.

## Contributors

[0xNonCents](https://github.com/0xNonCents), [albert_g](https://github.com/albert-garreta)
