class Field:
    def __init__(self, type_, default=None, required=False, validator=None):
        self.type_=type_
        self.default=default
        self.required=required
        self.validator=validator
