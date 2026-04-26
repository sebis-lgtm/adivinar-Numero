import pytest
from frontend import generate_number, iteration, finish_game

# -------------------------
# Tests para generate_number
# -------------------------

def test_generate_number_easy(monkeypatch):
    # Forzamos el valor de random
    monkeypatch.setattr("random.randint", lambda a, b: 5)
    assert generate_number("1") == 5


def test_generate_number_medium(monkeypatch):
    monkeypatch.setattr("random.randint", lambda a, b: 25)
    assert generate_number("2") == 25


def test_generate_number_hard(monkeypatch):
    monkeypatch.setattr("random.randint", lambda a, b: 77)
    assert generate_number("3") == 77


def test_generate_number_invalid_level(monkeypatch):
    monkeypatch.setattr("random.randint", lambda a, b: 3)
    assert generate_number("999") == 3


# -------------------------
# Tests para finish_game
# -------------------------

def test_finish_game_win(capsys):
    finish_game(True, 10)
    captured = capsys.readouterr()
    assert "GANASTE" in captured.out


def test_finish_game_lose(capsys):
    finish_game(False, 10)
    captured = capsys.readouterr()
    assert "FALLASTE" in captured.out
    assert "10" in captured.out


# -------------------------
# Tests para iteration
# -------------------------

def test_iteration_win(monkeypatch, capsys):
    inputs = iter(["1"])  # acierta en el primer intento

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    iteration(1)

    captured = capsys.readouterr()
    assert "GANASTE" in captured.out


def test_iteration_lose(monkeypatch, capsys):
    inputs = iter(["5", "6", "7"])  # falla todos

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    iteration(1)

    captured = capsys.readouterr()
    assert "FALLASTE" in captured.out


def test_iteration_hint_lower(monkeypatch, capsys):
    inputs = iter(["5", "1"])  # primero mayor, luego acierta

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    iteration(1)

    captured = capsys.readouterr()
    assert "menor" in captured.out


def test_iteration_hint_higher(monkeypatch, capsys):
    inputs = iter(["0", "1"])  # primero menor, luego acierta

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    iteration(1)

    captured = capsys.readouterr()
    assert "mayor" in captured.out