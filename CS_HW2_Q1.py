import datetime

# CRC Generation Polynomial: x^5 + x^2 + 1 (CRC-CCITT)

# Step 1: Define the CRC polynomial
POLYNOMIAL = '10101'


# Step 2: Define the encoding function
def encode(original_data):
    # Ensure original_data has the correct length (4 bits)
    original_data = original_data.zfill(4)

    # Append zeros for CRC (3 zeros for a 3-bit CRC)
    data_with_zeros = original_data + '000'

    # Perform polynomial division to calculate CRC
    crc = calculate_crc(data_with_zeros)

    # Combine the original data and CRC to create the encoded message
    encoded_message = original_data + crc
    return encoded_message


# Step 3: Define the decoding function
def decode(received_message):
    # Perform polynomial division to verify CRC
    is_error = verify_crc(received_message)

    if is_error:
        return "Error: CRC check failed"
    else:
        return "No error: CRC check passed"


# Step 4: Calculate CRC
def calculate_crc(data_with_zeros):
    # Perform XOR operation for each bit
    for i in range(4):
        if data_with_zeros[i] == '1':
            for j in range(5):
                if (i + j) < len(data_with_zeros):
                    data_with_zeros = data_with_zeros[:i + j] + str(
                        int(data_with_zeros[i + j]) ^ int(POLYNOMIAL[j])) + data_with_zeros[i + j + 1:]
    # The last 3 bits represent the CRC
    crc = data_with_zeros[-3:]
    return crc


# Step 5: Verify CRC
def verify_crc(received_message):
    # Perform polynomial division to verify CRC
    received_crc = received_message[-3:]
    data_with_zeros = received_message[:-3] + '000'
    calculated_crc = calculate_crc(data_with_zeros)

    return received_crc == calculated_crc


# Rest of the code remains the same...

# Example 1: Original Data - No Error
original_data_no_error = '1010'
encoded_message_no_error = encode(original_data_no_error)
print("Example 1:")
print("Original Data:", original_data_no_error)
print("Encoded message:", encoded_message_no_error)
print("Decoding result:", decode(encoded_message_no_error))
print()

# Example 2: Original Data - Error
original_data_error = '1100'
encoded_message_error = encode(original_data_error)
# Simulate an error by flipping a bit
encoded_message_error_with_error = encoded_message_error[:-3] + '011'
print("Example 2:")
print("Original Data:", original_data_error)
print("Encoded message with error:", encoded_message_error_with_error)
print("Decoding result:", decode(encoded_message_error_with_error))
current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f"Current date and time: {current_datetime}")
