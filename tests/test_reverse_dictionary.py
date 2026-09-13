#!/usr/bin/env python3

import unittest

from src.reverse_dictionary import reverse_dictionary


class TestReverseDictionary(unittest.TestCase):

    def test_worked_example(self):
        d = {"move": ["liikuttaa"], "hide": ["piilottaa", "salata"]}
        result = reverse_dictionary(d)
        self.assertIsInstance(
            result, dict,
            msg=f"reverse_dictionary should return a dictionary. Got {type(result)}.")
        self.assertEqual(
            result["liikuttaa"], ["move"],
            msg="Incorrect translation of 'liikuttaa' for dict %s!" % d)
        self.assertEqual(
            result["piilottaa"], ["hide"],
            msg="Incorrect translation of 'piilottaa' for dict %s!" % d)
        self.assertEqual(
            result["salata"], ["hide"],
            msg="Incorrect translation of 'salata' for dict %s!" % d)
        self.assertEqual(
            len(result), 3,
            msg="Incorrect number of elements in result for dict %s!" % d)

    def test_shared_translation_lists_both_source_words(self):
        d = {"move": ["liikuttaa"], "hide": ["piilottaa", "salata"],
             "six": ["kuusi"], "fir": ["kuusi"]}
        result = reverse_dictionary(d)
        self.assertEqual(
            result["liikuttaa"], ["move"],
            msg="Incorrect translation of 'liikuttaa' for dict %s!" % d)
        self.assertEqual(
            result["piilottaa"], ["hide"],
            msg="Incorrect translation of 'piilottaa' for dict %s!" % d)
        self.assertEqual(
            result["salata"], ["hide"],
            msg="Incorrect translation of 'salata' for dict %s!" % d)
        self.assertEqual(
            set(result["kuusi"]), {"fir", "six"},
            msg="Incorrect translation of 'kuusi' for dict %s! Both 'six' "
            "and 'fir' translate to 'kuusi', so 'kuusi' should map back to "
            "both, not just the first one found." % d)
        self.assertEqual(
            len(result), 4,
            msg="Incorrect number of elements in result for dict %s!" % d)

    def test_empty_dictionary(self):
        result = reverse_dictionary({})
        self.assertEqual(
            result, {},
            msg="reverse_dictionary({}) should return an empty dictionary, "
            "since there are no translations to reverse.")


if __name__ == '__main__':
    unittest.main()
