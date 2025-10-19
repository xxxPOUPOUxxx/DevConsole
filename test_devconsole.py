# test_devconsole.py
"""
Tests for DevConsole module.
"""

import unittest
from devconsole import DevConsole

class TestDevConsole(unittest.TestCase):
    """Test cases for DevConsole class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DevConsole()
        self.assertIsInstance(instance, DevConsole)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DevConsole()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
