import importlib.util

class Card():
    def __init__(self, filepath):
        self.filename = filepath.split("/")[-1]
        spec = importlib.util.spec_from_file_location(f"module.{self.filename}", filepath)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        self.subject = getattr(module, 'subject', None)
        self.prompt = getattr(module, 'prompt', None)
        self.solution = getattr(module, 'solution', None)
        self.notes = getattr(module, 'notes', None)
