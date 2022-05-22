
def getlist() -> tuple:
    with open("profanity_ptbr.txt") as f:
        words = tuple(map(lambda x: x.lower().replace('\n', ''), f.readlines()))
    return words

if __name__ == "__main__":
    words = getlist()
    print(words[:10])