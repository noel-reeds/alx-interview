#!/usr/bin/python3

def validUTF8(data):
        # Number of bytes in the current UTF-8 character
        n_bytes = 0
 
        # Mask to check if the most significant bit (8th bit from the left) is set or not
        mask1 = 1 << 7
 
        # Mask to check if the second most significant bit is set or not
        mask2 = 1 << 6
        for num in data:
 
            # Get the number of set most significant bits in the byte if
            # this is the starting byte of an UTF-8 character.
            mask = 1 << 7
            if n_bytes == 0:
                while mask & num:
                    n_bytes += 1
                    mask >>= 1
 
                # 1 byte characters
                if n_bytes == 0:
                    continue
 
                # Invalid scenarios according to the rules of the problem.
                if n_bytes == 1 or n_bytes > 4:
                    return False
            else:
 
                # If this byte is a part of an existing UTF-8 character, then we
                # simply have to look at the second most significant bit and we
                # make use of the masks we defined before to do so. If it is
                # valid, then simply reduce the number of bytes to process by 1.
                if not (num & mask1 and not (num & mask2)):
                    return False
                n_bytes -= 1
 
        # This is for the case where we might not have the complete data for
        # a particular UTF-8 character.
        return n_bytes == 0
