import unittest


def get_tuples(similar_ids):
    if not isinstance(similar_ids, dict):
        raise ValueError("error: input must be a dictionary")

    result = set()

    for key, values in similar_ids.items():
        if not isinstance(key, (int, float)) or not isinstance(values, list):
            raise ValueError(
                "error: keys mus be itegers or floats and values must be lists")

        filtered_values = [value for value in values if isinstance(
            value, (int, float)) and value > key]

        for value in filtered_values:
            result.add((key, value))

    return result


# Tests cases, In this test 3 cases must fail because the input is not a dictionary, the keys are not integers
# or floats and the values are not lists


class TestGetTuples(unittest.TestCase):
    def test_normal_case(self):
        similar_ids = {
            123: [458, 812, 765],
            458: [123, 812, 765],
            812: [123, 458],
            765: [123, 458],
            999: [100],
            100: [999]
        }
        self.assertEqual(get_tuples(similar_ids), {
            (123, 458), (123, 812), (123, 765), (458, 812), (458, 765), (100, 999)})

    def test_empty_dict(self):
        self.assertEqual(get_tuples({}), set())

    def test_single_pair(self):
        self.assertEqual(get_tuples({1: [2]}), {(1, 2)})

    def test_float_values(self):
        similar_ids = {1.5: [2.5, 3.5], 2.5: [1.5, 3.5]}
        self.assertEqual(get_tuples(similar_ids), {
            (1.5, 2.5), (1.5, 3.5), (2.5, 3.5)})

    def test_no_values(self):
        self.assertEqual(get_tuples({1: []}), set())

    def test_values_no_keys(self):
        similar_ids = {1: [2, 3], 3: [4]}
        self.assertEqual(get_tuples(similar_ids), {(1, 2), (1, 3)})

    def test_negative_values(self):
        similar_ids = {1: [-2], -3: [-4, -5]}
        self.assertEqual(get_tuples(similar_ids), {(-3, -4), (-3, -5)})

    def test_string_value(self):
        with self.assertRaises(ValueError):
            get_tuples({1: ["2"]})

    def test_string_key(self):
        with self.assertRaises(ValueError):
            get_tuples({"1": [2]})

    def test_non_dictionary_input(self):
        with self.assertRaises(ValueError):
            get_tuples("test")


if __name__ == "__main__":
    unittest.main()
