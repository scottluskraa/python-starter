"""
Test module for main.py.
This demonstrates basic pytest usage.
"""

import sys
import os

# Add parent directory to path to import main module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import main

def test_main_runs_without_error(capsys):
    """Test that main function runs without error and prints expected output."""
    main()
    captured = capsys.readouterr()
    assert "Hello, World!" in captured.out

def test_main_returns_none():
    """Test that main function returns None."""
    result = main()
    assert result is None
