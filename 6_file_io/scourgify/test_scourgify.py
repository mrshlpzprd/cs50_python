import pytest
import sys
import csv
from unittest.mock import patch, mock_open
from scourgify import main

# Test 1: Too few command-line arguments
def test_too_few_cl():
    with patch.object(sys, 'argv', ['scourgify.py']):
        with pytest.raises(SystemExit):
            main()

# Test 2: Too many command-line arguments
def test_too_many_cl():
    with patch.object(sys, 'argv', ['scourgify.py', '1.csv', '2.csv', '3.csv']):
        with pytest.raises(SystemExit):
            main()

# Test 3: Valid CSV
def test_valid_csv():
    mock_input_csv = 'name,house\n"Abbott, Hannah",Hufflepuff\n"Bell, Katie",Gryffindor\n'
    expected_output = 'first,last,house\nHannah,Abbott,Hufflepuff\nKatie,Bell,Gryffindor\n'
    with patch('builtins.open', mock_open(read_data=mock_input_csv)) as mock_file:
        with patch.object(sys, 'argv', ['scourgify.py', 'before.csv', 'after.csv']):
            main()
        written_content = mock_file().write.call_args_list
        actual_output = ''.join([call[0][0] for call in written_content])
        actual_output = actual_output.replace('\r\n', '\n')
        expected_output = expected_output.replace('\r\n', '\n')
        print("Actual Output:")
        print(actual_output)
        assert actual_output == expected_output, f"Expected: {expected_output}, but got: {actual_output}"

# Test 4: Could not read file
def test_file_not_read():
    with patch.object(sys, 'argv', ['scourgify.py', 'invalid_file.csv', 'output.csv']):
        with pytest.raises(SystemExit):
            main()
