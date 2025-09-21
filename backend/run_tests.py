import sys
import os

# Ensure project root is on sys.path so imports like `analyzer` work
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from backend import test_analyzer as ta


def main():
    try:
        ta.test_size_bias_reduced()
        print('test_size_bias_reduced passed')
    except AssertionError as e:
        print('test_size_bias_reduced failed:', e)
        raise

    try:
        ta.test_ignore_size_flag()
        print('test_ignore_size_flag passed')
    except AssertionError as e:
        print('test_ignore_size_flag failed:', e)
        raise

    print('All tests passed')

if __name__ == '__main__':
    main()
