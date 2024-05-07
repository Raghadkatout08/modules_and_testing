from factorial_module.factorial_module import factorial_iterative, factorial_recursion, clumsy

#factorial_iterative

def test_factorial_iterative1 ():
    actual = factorial_iterative(0)
    excepted = 1
    assert actual == excepted

def test_factorial_iterative2 ():
    actual = factorial_iterative(1)
    excepted = 1
    assert actual == excepted

def test_factorial_iterative3 ():
    actual = factorial_iterative(5)
    excepted = 120
    assert actual == excepted

#factorial_recursion

def test_factorial_recursion1 ():
    actual = factorial_recursion(0)
    excepted = 1
    assert actual == excepted

def test_factorial_recursion2 ():
    actual = factorial_recursion(1)
    excepted = 1
    assert actual == excepted

def test_factorial_recursion3 ():
    actual = factorial_recursion(5)
    excepted = 120
    assert actual == excepted

#clumsy

def test_clumsy1():
    actual = clumsy(0)
    excepted = 0
    assert actual == excepted
def test_clumsy2():
    actual = clumsy(1)
    excepted = 1
    assert actual == excepted
def test_clumsy3():
    actual = clumsy(5)
    excepted = 7
    assert actual == excepted
def test_clumsy4():
    actual = clumsy(10)
    excepted = 12
    assert actual == excepted
def test_clumsy5():
    actual = clumsy(15)
    excepted = 14
    assert actual == excepted