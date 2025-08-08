def decode_message(secret_key, message):
    decoder = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    j = 0

    for i in secret_key:
        if i != " " and i not in decoder:
            decoder[i] = alphabet[j]
            j += 1
    decoded_message = ""
    for k in range(len(message)):
        if message[k] == " ":
            decoded_message += " "
        else:
            decoded_message += decoder[message[k]]
    print(decoded_message)

if __name__ == "__main__":
    secret_key = "the quick brown fox jumps over the lazy dog"
    message = "vkbs bs t suepuv"
    decode_message(secret_key, message)