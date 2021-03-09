import unittest
from GetUserRepos import get_repo_commits


class TestGitUserRepos(unittest.TestCase):

    def testCorrectRepos(self):
        result = get_repo_commits('nicole894')
        self.assertEqual(len(result), 12)

    def testWrongRepos(self):
        result = get_repo_commits('nicole894')
        self.assertNotEqual(len(result), 8)

    def testInValidRepos(self):
          result = get_repo_commits('nicole8534394')
          self.assertEqual(result, "Not Found")

    def testNoRepos(self):
          result = get_repo_commits('ryandsa159')
          self.assertIsNone(result)

    def testCorrectCommits(self):
        result = get_repo_commits('nicole894')
        x = result[1]
        self.assertEqual(x['Number of commits'], 5)


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
