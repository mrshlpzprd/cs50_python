import sys
import pytest
from unittest.mock import mock_open, patch

# Test 1: Too few command-line arguments
def test_too_few_cl_arg(monkeypatch, capsys):
    monkeypatch.setattr(sys, 'argv', ['lines.py'])
    with pytest.raises(SystemExit) as excinfo:
        import lines
    assert str(excinfo.value) == "Too few command-line arguments"

# Test 2: Too many command-line arguments
def test_too_many_cl_arg(monkeypatch, capsys):
    monkeypatch.setattr(sys, 'argv', ['lines.py', 'hello.py', 'goodbye.py'])
    with pytest.raises(SystemExit) as excinfo:
        import lines
    assert str(excinfo.value) == "Too many command-line arguments"

# Test 3: Not a Python file
def test_not_py_file(monkeypatch, capsys):
    monkeypatch.setattr(sys, 'argv', ['script.py', 'names.txt'])
    with pytest.raises(SystemExit) as excinfo:
        import lines
    assert str(excinfo.value) == "Not a Python file"

# Test 4: Python file (output qty lines)
def test_py_file(monkeypatch, capsys):
    mock_file = mock_open(read_data=
    """
    # This is a comment
print("Hello World") # This is an inline comment
# Another comment
def some_function():
    pass
""")
    monkeypatch.setattr(sys, 'argv', ['lines.py', 'file.py'])
    with patch('builtins.open', mock_file):
        import lines
    captured = capsys.readouterr()
    assert captured.out == "3\n"

# Test 5: File does not exist
def test_file_not_found(monkeypatch, capsys):
    monkeypatch.setattr(sys, 'argv', ['lines.py', 'non_existent_file.py'])
    with patch('builtins.open', side_effect=FileNotFoundError):
        try:
            import lines  # This will execute the script
        except SystemExit as e:
            print(f"Caught SystemExit: {e}")  # Debugging output
            raise e  # Re-raise the exception for pytest to catch
