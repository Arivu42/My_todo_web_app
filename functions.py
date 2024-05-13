def get_todos(filepath='todos.txt'):
    """ Reads a text file and return the list of to_do items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath='todos.txt'):
    """ Write the to_do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)