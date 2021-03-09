import unittest
from GetUserRepos import get_repo_commits


class TestGitUserRepos(unittest.TestCase):

    def testCorrectRepos(self):
        result = get_repo_commits('nicole894')
        self.assertEqual(len(result), 12)

    def testInValidRepos(self):
         result = get_repo_commits('nicole894')
         x =  result[1]
         self.assertEqual(x['Number of commits'], 3)
    #
    # def testCorrectCommits(self):
    #     result = get_repo_commits('nicole894')
    #     x = result[1]
    #     self.assertEqual(x['Number of commits'], 2)


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()