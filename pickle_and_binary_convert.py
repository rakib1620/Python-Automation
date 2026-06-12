# ==============================================================================
# Script Name: 08_pickle_string.py
# Purpose: Demonstrates how to pack (serialize) a plain text string into binary
#          and release (deserialize) it back using the pickle module.
# Author: Rakib Hossain
# ==============================================================================

import pickle

# 1. A simple string data (Human-readable text)
my_string = "Server_Status:_Active"

# ==============================================================================
# PART 1: Packing (Serializing) the string into a binary file
# ==============================================================================
with open("string_data.bin", "wb") as file:
    # pickle.dump converts the string into binary bytes and saves it
    pickle.dump(my_string, file)

print("Success: String has been packed into 'string_data.bin'!")


# ==============================================================================
# PART 2: Releasing (Deserializing) the string from the binary file
# ==============================================================================
with open("string_data.bin", "rb") as file:
    # pickle.load releases the binary bytes back into the original string object
    released_string = pickle.load(file)

print("\n--- Released Data From Binary File ---")
print(f"Output: {released_string}")
print(f"Data Type: {type(released_string)}")