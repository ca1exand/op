# 0-9,A-Z,a-z
def chars_are_valid(query):
    for c in query:
        if (c not in list(map(chr, range(48,57))) + list(map(chr, range(65,91)))+list(map(chr, range(97,123)))):
            return False
    return True
