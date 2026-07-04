import pytest
from logging import debug , info

def test_if_tests_are_found():
    assert True
    
def test_log_file():
    debug("test if this message is write")
    assert True

@pytest.mark.forceError
def test_erro_message():
    assert False
    
def test_logs():
    info("Iniciando logs e tests")
    assert True
   