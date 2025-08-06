def decode_message(secret_key, message):
    decoder = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    j = 0
    print(len(secret_key))
    for i in range(len(secret_key)):
        if secret_key[i] != " ":
            if decoder.get(secret_key[i]) != secret_key[i]:
                print(decoder.get(secret_key[i]))
                decoder[secret_key[i]] = alphabet[1]

                j += 1
    print(decoder)
    print(j)

if __name__ == "__main__":
    secret_key = "the quick brown fox jumps over the lazy dog"
    message = "vkbs bs t suepuv"
    decode_message(secret_key, message)