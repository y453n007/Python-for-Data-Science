def NULL_not_found(object: any) -> int:
    if object.__class__.__name__ == "str":
        if not object:
            print(f"Empty: <class '{object.__class__.__name__}'>")
        else:
            print("Type not found")
    else:
        print(f"{object.__class__.__name__.title()}: {object} <class '{object.__class__.__name__}'>")
    return 1