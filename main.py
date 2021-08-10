from tries import *

if __name__ == "__main__":
    print("Interview ALgorithms")
    words = ["sc", "s", "sccc", "aloha"]
    tries = Tries()
    for word in words:
        tries.insert(word)

    for word in words:
        print(tries.search(word))