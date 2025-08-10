def to_lowercase(message):
    lowered = ""
    for i in message:
        lowered += i.lower()
    print(lowered)
if __name__ == "__main__":
    message = "HELLO"
    to_lowercase(message)