FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Read text from a file and return a list"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write todos list into a file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
    return


if __name__ == "__main__":
    print("Hi there")
