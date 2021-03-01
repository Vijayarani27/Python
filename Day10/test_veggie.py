import pytest
from vegetable import app

def test_create_get_200():
    test = app.test_client()
    response = test.get('/vegetables')
    status=response.status_code
    assert status == 200

def test_create_post_200():
    test = app.test_client()
    response = test.post('/vegetables',json={"vegname":"veg_name","qty":3})
    status=response.status_code
    assert status == 200   

def test_create_getOne_400():
    test = app.test_client()
    response = test.get('/vegetables/drumstick')
    status=response.status_code
    assert status == 400   

def test_create_delete_400():
    test = app.test_client()
    response = test.delete('/vegetables/drumstick')
    status=response.status_code
    assert status == 400   

def test_create_put_400():
    test = app.test_client()
    response = test.put('/vegetables/drumstick')
    status=response.status_code
    assert status == 400  

def test_schema_validate_400():
    test = app.test_client()
    response = test.post('/vegetables',json={"vegname":"veg","qty":3})
    status=response.status_code
    assert status == 400  
