import pytest
from unittest.mock import mock_open
import sys
import pizza

# Test 1: CSV file (print table)
def test_successful_csv_read(mocker, capsys):
    mock_csv_content = "Regular Pizza,Small,Large\nCheese,$13.50,$18.95\n1 topping,$14.75,$20.95\n"
    mocker.patch("sys.argv", ["pizza.py", "regular.csv"])
    mocker.patch("builtins.open", mock_open(read_data=mock_csv_content))
    pizza.main()
    captured = capsys.readouterr()
    expected_output = """+-----------------+---------+---------+
| Regular Pizza   | Small   | Large   |
+=================+=========+=========+
| Cheese          | $13.50  | $18.95  |
+-----------------+---------+---------+
| 1 topping       | $14.75  | $20.95  |
+-----------------+---------+---------+
"""
    assert captured.out == expected_output

# Test 2: Too few command-line arguments
def test_too_few_arguments(mocker):
    mocker.patch("sys.argv", ["pizza.py"])
    with pytest.raises(SystemExit) as exc_info:
        pizza.main()
    assert str(exc_info.value) == "Too few command-line arguments"

# Test 3: Too many command-line arguments
def test_too_many_arguments(mocker):
    mocker.patch("sys.argv", ["pizza.py", "foo", "bar"])
    with pytest.raises(SystemExit) as exc_info:
        pizza.main()
    assert str(exc_info.value) == "Too many command-line arguments"

# Test 4: Not a CSV file
def test_not_a_csv_file(mocker):
    mocker.patch("sys.argv", ["pizza.py", "sicilian.txt"])
    with pytest.raises(SystemExit) as exc_info:
        pizza.main()
    assert str(exc_info.value) == "Not a CSV file"

# Test 5: File does not exist
def test_file_not_found(mocker):
    mocker.patch("sys.argv", ["pizza.py", "invalid_file.csv"])
    mocker.patch("builtins.open", side_effect=FileNotFoundError)
    with pytest.raises(SystemExit) as exc_info:
        pizza.main()
    assert str(exc_info.value) == "File does not exist"
