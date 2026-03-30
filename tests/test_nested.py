from dataforge.field import Field
from dataforge.schema import Schema

class Child(Schema):
    value=Field(int, required=True)

class Parent(Schema):
    child=Field(Child, required=True)

def test_nested_to_dict_fail():
    p=Parent(child=Child(value=1))
    assert p.to_dict()['child']=={'value':1}

def test_nested_non_fail_pass():
    assert Child(value=1).to_dict()['value']==1

def test_nested_validate_pass():
    assert Parent(child=Child(value=2)).validate()

def test_nested_type_pass():
    assert isinstance(Parent(child=Child(value=2)).child, Child)

def test_nested_dict_pass():
    assert isinstance(Parent(child=Child(value=3)).to_dict(), dict)
