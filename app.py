import ast

def extract_code_metadata(file_path):
    with open(file_path, "r") as file:
        code = file.read()
    
    tree = ast.parse(code)
    functions = []
    classes = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions.append({
                "name": node.name,
                "args": [arg.arg for arg in node.args.args],
                "docstring": ast.get_docstring(node),
            })
        elif isinstance(node, ast.ClassDef):
            methods = [
                {
                    "name": n.name,
                    "docstring": ast.get_docstring(n),
                }
                for n in node.body if isinstance(n, ast.FunctionDef)
            ]
            classes.append({
                "name": node.name,
                "methods": methods,
                "docstring": ast.get_docstring(node),
            })

    return {"functions": functions, "classes": classes}
