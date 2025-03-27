def jewels_and_stones(jewels, stones):
    jewels = list(jewels)
    stones = list(stones)
    jewel_count = {}
    match = 0
    for i in range(len(jewels)):
        if jewels[i] not in jewel_count:
            jewel_count[jewels[i]] = 0
    for i in range(len(stones)):
        if stones[i] in jewel_count:
            match += 1
    print("output: " + str(match))

if __name__ == "__main__":

    jewels = input("Jewels: ")
    stones = input("Stones: ")
    jewels_and_stones(jewels, stones)