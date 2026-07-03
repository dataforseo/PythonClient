import re
import importlib

def camel_to_snake(name):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()

def __getattr__(name):
    file_name = camel_to_snake(name)

    submodules_to_try = [
        f'dataforseo_client.{file_name}',
        f'dataforseo_client.api.{file_name}',
        f'dataforseo_client.models.{file_name}',
    ]

    for module_path in submodules_to_try:
        try:
            imported_module = importlib.import_module(module_path)
            if name == module_path.rsplit('.', 1)[-1]:
                obj = imported_module
            else:
                obj = getattr(imported_module, name)
            globals()[name] = obj
            return obj
        except (ImportError, ModuleNotFoundError, AttributeError):
            continue

    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
