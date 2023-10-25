from IpInfoGetterv2TestCopy import case_1, case_2, case_3, case_4, case_5, inv_case
import pytest

def test_case1():
    assert case_1() == True

def test_case2():
    assert case_2() == True

def test_case3():
    assert case_3() == True

def test_case4():
    assert case_4() == True

def test_case5():
    assert case_5() == True

def test_defaultCase():
    assert inv_case() == True
