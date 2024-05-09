from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import time
import datetime

# Known information
known_plaintext = bytes.fromhex("255044462d312e350a25d0d4c5d80a34")
known_ciphertext = bytes.fromhex("d06bf9d0dab8e8ef880660d2af65aa82")
known_iv = bytes.fromhex("09080706050403020100A2B2C2D2E2F2")

output_file ="text.txt"

with open(output_file, 'r') as file:
    for line in file:
        timestamp_key, timestamp = line.split(",")
        timestamp_key = bytes.fromhex(timestamp_key)

        cipher = AES.new(timestamp_key, AES.MODE_CBC, known_iv)
        generated_ciphertext = cipher.encrypt(known_plaintext)

        # print(generated_ciphertext.hex(), known_ciphertext.hex())
        if generated_ciphertext == known_ciphertext:
            print("Key found!")
            normal_date = datetime.datetime.utcfromtimestamp(int(timestamp))
            print("Timestamp:", normal_date)
            print("Key:", timestamp_key.hex())
            break
    else:
        print("Key not found within the specified time window.")



