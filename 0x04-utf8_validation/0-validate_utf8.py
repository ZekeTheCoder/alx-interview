#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Function validates if a given data set represents a valid UTF-8 encoding.

    Args:
    data: List of integers representing bytes

    Returns:
    bool: True if data is a valid UTF-8 encoding, False otherwise
    """

    # Keeps track of the number of bytes in the current UTF-8 character.
    byte_count = 0
    # Bit masks for the most significant bit (MSB) in a byte
    msb_mask1 = 1 << 7  # 10000000
    msb_mask2 = 1 << 6  # 01000000

    for byte in data:
        #  used to check the leading bits of the byte.
        current_bit = 1 << 7

        # Determine how many bytes the UTF-8 character has
        if byte_count == 0:
            while byte & current_bit:
                byte_count += 1
                current_bit = current_bit >> 1

            # valid single-byte characters
            if byte_count == 0:
                continue

            # Invalid encoding
            if byte_count == 1 or byte_count > 4:
                return False
        else:
            # Check if the current byte is a valid continuation byte
            if not (byte & msb_mask1 and not (byte & msb_mask2)):
                return False

        # Decrement the byte_count after processing each byte
        byte_count -= 1

    # If byte_count is 0, all bytes were valid
    if byte_count == 0:
        return True

    return False
