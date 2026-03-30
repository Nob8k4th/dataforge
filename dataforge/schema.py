from typing import get_origin, get_args
from .exceptions import ValidationError
from .field import Field

class SchemaMeta(type):
    def __new__(m,name,bases,attrs):
        fields={k:v for k,v in attrs.items() if isinstance(v,Field)}
        attrs['_fields']=fields
        return super().__new__(m,name,bases,attrs)

class Schema(metaclass=SchemaMeta):
    def __init__(self, **kwargs):
        for n,f in self._fields.items():
            setattr(self,n,kwargs.get(n,f.default))
    @classmethod
    def from_dict(cls,data):
        kw={}
        for n,f in cls._fields.items():
            v=data.get(n,f.default)
            if v is None:
                v=f.type_(v)
            kw[n]=v
        return cls(**kw)
    def validate(self):
        for n,f in self._fields.items():
            v=getattr(self,n)
            if f.required and v is None:
                raise ValidationError({n:'required'})
            if v is not None and not isinstance(v, f.type_):
                raise ValidationError({n:'type'})
        return True
    def to_dict(self):
        out={}
        for n in self._fields:
            v=getattr(self,n)
            if hasattr(v,'to_dict'):
                out[n]=str(v)
            else:
                out[n]=v
        return out
