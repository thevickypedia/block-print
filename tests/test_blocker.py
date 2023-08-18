import sys
import unittest
from io import StringIO
from typing import Callable, NoReturn
from unittest.mock import patch

from blockstdout import BlockPrint


def printer():
    """Test print statement."""
    print('hello')


def capture_output(function: Callable) -> NoReturn:
    """Captures the output of a function that uses print.

    Args:
        function: Test function that needs to be called.
    """
    old_stdout = sys.stdout
    captured_output = StringIO()
    sys.stdout = captured_output

    function()

    sys.stdout = old_stdout
    captured_output.seek(0)
    return captured_output.read()


class TestBlockPrint(unittest.TestCase):
    """Test object.

    >>> unittest.TestCase

    """

    def test_print_blocked(self) -> NoReturn:
        """Test that the BlockPrint context manager correctly blocks print statements."""
        with BlockPrint():
            with patch('builtins.print') as mock_print:
                printer()  # Print should be called but not displayed
                mock_print.assert_called_once_with('hello')

        # After exiting the block, print should work normally
        captured_output = capture_output(printer)
        self.assertEqual(captured_output.strip(), 'hello')


if __name__ == '__main__':
    unittest.main()
