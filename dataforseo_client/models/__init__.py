import re
import importlib

def camel_to_snake(name):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()

def __getattr__(name):
    file_name = camel_to_snake(name)
    module = importlib.import_module(f'dataforseo_client.models.{file_name}')
    model = getattr(module, name)
    globals()[name] = model
    return model