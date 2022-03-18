def get_info(**kwargs):
    result = f"This is {kwargs.get('name')} from {kwargs.get('town')} and he is {kwargs.get('age')} years old"
    return result



print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))