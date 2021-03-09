import unittest

from GetUserRepos import get_repo_commits

class TestGitUserRepos(unittest.TestCase):

    def testCorrectRepos(self):
        result = self.get_repo_commits('nicole84')
        self.assertEqual(len(result), 12)