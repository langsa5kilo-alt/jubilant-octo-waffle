import sys


def greet():
    return "siap"


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        assert greet() == "siap", greet()
        print("ok")
    else:
        print(greet())
