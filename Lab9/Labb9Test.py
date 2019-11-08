import Labb9 as x
import unittest

class Test(unittest.TestCase):

    def test1(self):
        inputs = []
        with open("correct_indatasample") as correct:
            for row in correct:
                row = row.strip()
                if row is "#":
                    break
                inputs.append(row)

        outputs = []
        with open("correct_outdatasample") as correct_answers:
            for row in correct_answers:
                row = row.strip()
                if row is "#":
                    break
                inputs.append(row)

        for i, j in enumerate(outputs):
            self.assertEqual(x.main(inputs[i]), j)

    def test2(self):
        inputs = []
        with open("incorrect_indatasample") as incorrect:
            for row in incorrect:
                row = row.strip()
                if row is "#":
                    break
                inputs.append(row)

        outputs = []
        with open("incorrect_outdatasample") as incorrect_answers:
            for row in incorrect_answers:
                row = row.strip()
                if row is "#":
                    break
                inputs.append(row)

        for i, j in enumerate(outputs):
            self.assertEqual(x.main(inputs[i]), j)


if __name__ == '__main__':
    unittest.main()