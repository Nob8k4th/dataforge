from typing import Optional
from dataforge.field import Field
from dataforge.schema import Schema

class S(Schema):
    x=Field(int)
    nums=Field(list)
    maybe=Field(Optional[int])

def test_list_pass():
    assert S(x=1, nums=[1,2]).to_dict()['nums']==[1,2]

def test_optional_none_fail1():
    assert S.from_dict({'x':1,'nums':[],'maybe':None}).maybe is None

def test_optional_none_fail2():
    assert S.from_dict({'x':2,'nums':[1],'maybe':None}).to_dict()['maybe'] is None

def test_int_pass():
    assert S(x=1, nums=[]).x==1

def test_dict_pass():
    assert isinstance(S(x=1, nums=[]).to_dict(), dict)

def test_required_pass():
    assert S(x=1, nums=[]).validate()
