from TestDemo import multiply
import pytest
import sys

def test_mul():
    assert multiply(2,4) == 8

@pytest.mark.skipif(sys.version_info > (3, 7), reason="Checking skip if") 
def test_mul1():
    assert multiply(2,5) == 10   

@pytest.mark.skip(reason="Skip It")
def test_mul_with_zero():
    assert multiply(0,4) == 0

def test_mul_with_string():
    assert multiply("hello",2) == 'hellohello' 

def test_mul_with_list():
    assert multiply([1,2,3],2) == [1,2,3,1,2,3]

def test_mul_with_negativeValue():
    assert multiply(-6,-2) == 12    

@pytest.mark.xfail(reason="Don't want to fail")
def test_mul2():
    assert multiply(2,5) == 11


@pytest.fixture
def element1():
    return 3

@pytest.fixture
def element2():
    return 2

def test_multiply(element1,element2):
    assert multiply(element1,element2) == 6    

@pytest.mark.parametrize(
    "element1,element2,expected",
    [
        (5,3,15),
        ("hi",3,'hihihi'),
        ([5,2],2,[5,2,5,2])
        ]
)
def test_mul_with_parameters(element1,element2,expected):
   assert multiply(element1,element2) == expected

def test_assert():
    dic={}
    with pytest.raises(KeyError):
        print(dic[0])