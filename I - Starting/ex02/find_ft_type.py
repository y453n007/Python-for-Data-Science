def all_thing_is_obj(object: any) -> int:
    if object.__class__.__name__ == "int":
        print("Type not found")
    elif object.__class__.__name__ == "str":
         print(f"{object} is in the kitchen : <class '{object.__class__.__name__}'>")
    else:
        print(f"{object.__class__.__name__.title()} : <class '{object.__class__.__name__}'>")
    return 42
