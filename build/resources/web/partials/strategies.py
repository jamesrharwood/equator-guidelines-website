import os

def default(path) -> str:
    path = os.path.join('../..', path)
    return f"{{{{< include {path} >}}}}"

def custom(path) -> str:
    with open(path, 'r') as file_:
        string = file_.read()
    return string

def not_implemented(path) -> str:
    return f"No strategy implemented for {path}"