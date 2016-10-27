from wtforms.validators import ValidationError

class RecordExists():
    def __init__(self, model, field, message=None):
        self.model = model
        self.field = field
        if not message:
            message = '{record} with given {field} doesn\'t exist'.format(record=model.__name__, field=field)
        self.message = message

    def __call__(self, form, field):
        record = self.model.query.filter_by(**{self.field: field.data}).first()
        if not record:
            raise ValidationError(self.message)
