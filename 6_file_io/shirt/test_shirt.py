import shirt
import pytest
import sys
import os
from PIL import Image


def test_too_few_cl():
    sys.argv = ["shirt.py", "input.jpg"]
    with pytest.raises(SystemExit) as e:
        shirt.main()
    assert str(e.value) == "Too few command-line arguments"


def test_too_many_cl():
    sys.argv = ["shirt.py", "before1.jpg", "before2.jpg", "before3.jpg"]
    with pytest.raises(SystemExit) as e:
        shirt.main()
    assert str(e.value) == "Too many command-line arguments"


def test_invalid_input():
    sys.argv = ["shirt.py", "invalid_format.bmp", "after1.jpg"]
    with pytest.raises(SystemExit) as e:
        shirt.main()
    assert str(e.value) == "Invalid input"


def test_invalid_output():
    sys.argv = ["shirt.py", "before1.jpg", "invalid_format.bmp"]
    with pytest.raises(SystemExit) as e:
        shirt.main()
    assert str(e.value) == "Invalid output"


def test_different_extensions():
    sys.argv = ["shirt.py", "before1.jpg", "after1.png"]
    with pytest.raises(SystemExit) as e:
        shirt.main()
    assert str(e.value) == "Input and output have different extensions"


def test_file_not_found():
    sys.argv = ["shirt.py", "non_existent_image.jpg", "after1.jpg"]
    with pytest.raises(SystemExit) as e:
        shirt.main()
    assert str(e.value) == "Input does not exist"


def test_cs50_p_shirt(tmp_path):
    test_input = "muppet_01.jpg"
    test_output = tmp_path / "output.jpg"

    sys.argv = ["shirt.py", test_input, str(test_output)]

    dummy_image = Image.new("RGB", (800, 800), color=(255, 0, 0))
    dummy_image.save(test_input)

    shirt.cs50_p_shirt()

    with Image.open(test_output) as img:
        assert img.size == (600, 600)
        assert img.format == "JPEG"

    os.remove(test_input)

