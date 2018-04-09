# Improts the hahsing moduals
import hashlib as h
import sys


def Hash(String):
    System_Encoding = sys.getfilesystemencoding()
    m = h.sha256()
    m.update(bytes(str(String), encoding=System_Encoding))
    Hash = m.digest()
    return str(Hash)


if __name__ == "__main__":
    String = ""

    if String:
        print(Hash(""))
    else:
        print(Hash(input()))
