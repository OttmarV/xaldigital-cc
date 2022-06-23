import unittest
import pandas as pd
import os

RAW_DATA = os.getenv("RAW_DATA")


class TestState(unittest.TestCase):
    def setUp(self) -> None:
        self.df = pd.read_csv(RAW_DATA, usecols=["state"])

    def test_state_length(self):
        length_test = (
            self.df["state"].apply(lambda x: True if len(x) == 2 else False).all()
        )
        self.assertEqual(
            length_test,
            True,
            "Column State cannot contain records with value length, less than or greater than 2",
        )

    def test_state_isalpha(self):
        isalpha_test = (
            self.df["state"].apply(lambda x: True if x.isalpha() else False).all()
        )
        self.assertEqual(
            isalpha_test,
            True,
            "Column State cannot contain records with numbers",
        )


unittest.main(argv=[""], verbosity=2, exit=True)
