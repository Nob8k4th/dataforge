import pytest
from dataforge.field import Field
from dataforge.schema import Schema
from dataforge.exceptions import ValidationError

class User(Schema):
    name=Field(str, required=True)
    age=Field(int, default=0)

def test_required_pass():
    with pytest.raises(ValidationError):
        User(age=1).validate()

def test_default_pass():
    assert User(name='a').age==0

def test_to_dict_pass():
    assert User(name='a').to_dict()['name']=='a'

def test_validate_fail_collect1():
    class S(Schema):
        a=Field(int, required=True)
        b=Field(int, required=True)
    with pytest.raises(ValidationError) as e:
        S().validate()
    assert 'a' in str(e.value) and 'b' in str(e.value)

def test_validate_fail_collect_three_fields():
    class S(Schema):
        x = Field(int, required=True)
        y = Field(int, required=True)
        z = Field(int, required=True)
    with pytest.raises(ValidationError) as e:
        S().validate()
    errors_str = str(e.value)
    assert 'x' in errors_str and 'y' in errors_str and 'z' in errors_str

def test_type_pass():
    assert User(name='a', age=1).validate()
