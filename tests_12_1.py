import unittest
import runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        run1 = runner.Runner('Max')
        for _ in range(10):
            run1.walk()
        self.assertEqual(run1.distance, 50, f'{run1.name} ran {run1.distance}m, but should have done 50m')

    def test_run(self):
        run2 = runner.Runner('Dan')
        for _ in range(10):
            run2.run()
        self.assertEqual(run2.distance, 100, f'{run2.name} ran {run2.distance}m, but should have done 100m')

    def test_challenge(self):
        run1 = runner.Runner('Max')
        run2 = runner.Runner('Dan')
        for _ in range(10):
            run1.run()
            run2.walk()
        self.assertNotEqual(run1.distance, run2.distance)
