import unittest
from main import main
import pandas as pd


class MyTestCase(unittest.TestCase):
    def test_something(self):
        df = pd.DataFrame(data={"A": [1, 2, 3, 4, 5], "B": [1, 2, 3, 4, 5]})
        pd.testing.assert_frame_equal(df, main())


if __name__ == '__main__':
    unittest.main()
