# uint384

Implementation of basic operations between unsigned 384-bit integers. Some operations are also supported for signed 384-bit integers.  (Note that Cairo's native "integer" is of 251 bits)

**NOTE**: Hints are currently in revision by StarkWare for whitelisting

The library follows and extends Cairo's common library `uint256`. The usage and logic is almost the same as in `uint256`. All operations from `uint256` are implemented here for 384 bits. 

Recall that in `uint256`, 256-bit integers are represented by the struct:

    # Represents an integer in the range [0, 2^384)
    struct Uint256:
        # The low 128 bits of the value.
        member low : felt
        # The high 128 bits of the value.
        member high : felt
    end

We extend this to 384 bits by defining the struct

    # Represents an integer in the range [0, 2^384)
    struct Uint384:
        # The low 128 bits of the value.
        member d0 : felt
        # The middle 128 bits of the value.
        member d1 : felt    
        # The high 128 bits of the value.
        member d1 : felt
    end

**NOTE**: All operations here expect each member of `Uint384` to be a felt smaller than 2**128. Similarly, all the returned instances of `Uint384` satisfy this condition. Using this library without meeting this requirement can result in unexpected behavior.

## Namespace

We use a namespace so that all library functions can be imported at once with `from <directory>.uint384.cairo import uint384` and functions can be called with the syntax `uint384.<function_name>` (this differs from the original `uint256`)

## Testing

We include a simple StarkNet contract and a pytest test for every library function (except some auxiliary functions that are used within other functions). The project is structured following Nile's framework.
