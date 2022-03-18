def concatenate(*args):
    result = ''.join([word for word in args])
    return result



print(concatenate("Soft", "Uni", "Is", "Great", "!"))