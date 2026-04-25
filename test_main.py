from main import calcular_promedio, es_primo, es_palindromo
def test_calcular_promedio():
    assert calcular_promedio([10, 20, 30]) == 20.0
    assert calcular_promedio([]) == 0

def test_es_primo():
    assert es_primo(7) is True
    assert es_primo(4) is False
    assert es_primo(1) is False

def test_es_palindromo():
    assert es_palindromo("Ana") is True
    assert es_palindromo("Hola") is False
    assert es_palindromo("radar") is True
    assert es_palindromo("12321") is True