#!/usr/bin/python3
"""
alternative ways to import:

    import importlib.util

    spec = importlib.util.spec_from_file_location("hidden", "hidden_4.pyc")
    hidden = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden)
or:
    hidden = __import__('hidden')
"""
if __name__ == '__main__':
    import hidden_4 as hidden
    for attributes in dir(hidden):
        if not attributes.startswith('__'):
            print(attributes)
