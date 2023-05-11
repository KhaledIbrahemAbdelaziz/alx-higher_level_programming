#!/usr/bin/python3

if __name__ == "__main__":
    """prints all the names defined by module hidden_4.pyc"""
    import hidden_4

    name = dir(hidden_4)
    for names in name:
        if names[:2] != "__":
            print(names)
