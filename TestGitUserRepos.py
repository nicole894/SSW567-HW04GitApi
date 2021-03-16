import unittest
from unittest import mock
from unittest.mock import Mock

from requests.cookies import MockResponse

from GetUserRepos import get_repo_commits


class TestGitUserRepos(unittest.TestCase):

    @mock.patch('requests.get')
    def testCorrectRepos(self, mockedReq):
        mockedReq.return_value = MockResponse([{'Repo': 'CasinoSlotMachine', 'Number of commits': 3},
                                               {'Repo': 'CS570-DataStructures', 'Number of commits': 5},
                                               {'Repo': 'GEDCOM-Parser-Project---CS-555', 'Number of commits': 30},
                                               {'Repo': 'German-English-Laguage-Translator', 'Number of commits': 2},
                                               {'Repo': 'helloworld', 'Number of commits': 2},
                                               {'Repo': 'kg_nicole894_2021', 'Number of commits': 3},
                                               {'Repo': 'Multiplayer-tic-tac-toe', 'Number of commits': 4},
                                               {'Repo': 'NicoleAnnikaGonsalves_Projects_Python',
                                                'Number of commits': 2},
                                               {'Repo': 'PythonHackerRankChallenges', 'Number of commits': 3},
                                               {'Repo': 'SSW-567-HW02a', 'Number of commits': 13},
                                               {'Repo': 'SSW567-HW01', 'Number of commits': 2},
                                               {'Repo': 'SSW567-HW04GitApi', 'Number of commits': 10}])

        result = get_repo_commits('nicole894')
        self.assertEqual(len(result), 12)

    @mock.patch('requests.get')
    def testWrongRepos(self, mockedReq):
        mockedReq.return_value = MockResponse([{'Repo': 'CasinoSlotMachine', 'Number of commits': 3},
                                               {'Repo': 'CS570-DataStructures', 'Number of commits': 5},
                                               {'Repo': 'GEDCOM-Parser-Project---CS-555', 'Number of commits': 30},
                                               {'Repo': 'German-English-Laguage-Translator', 'Number of commits': 2},
                                               {'Repo': 'helloworld', 'Number of commits': 2},
                                               {'Repo': 'kg_nicole894_2021', 'Number of commits': 3},
                                               {'Repo': 'Multiplayer-tic-tac-toe', 'Number of commits': 4},
                                               {'Repo': 'NicoleAnnikaGonsalves_Projects_Python',
                                                'Number of commits': 2},
                                               {'Repo': 'PythonHackerRankChallenges', 'Number of commits': 3},
                                               {'Repo': 'SSW-567-HW02a', 'Number of commits': 13},
                                               {'Repo': 'SSW567-HW01', 'Number of commits': 2},
                                               {'Repo': 'SSW567-HW04GitApi', 'Number of commits': 10}])

        result = get_repo_commits('nicole894')
        self.assertNotEqual(len(result), 8)

    @mock.patch('requests.get')
    def testInValidRepos(self, mockedReq):
        mockedReq.return_value = MockResponse({"message": "Not Found",
                                               "documentation_url": "https://docs.github.com/rest/reference/repos#list-repositories-for-a-user"
                                               })
        result = get_repo_commits('nicole8534394')
        self.assertEqual(result, "Not Found")

    @mock.patch('requests.get')
    def testNoRepos(self, mockedReq):
        mockedReq.return_value = MockResponse([])
        result = get_repo_commits('ryandsa159')
        self.assertIsNone(result)

    @mock.patch('requests.get')
    def testCorrectCommits(self, mockedReq):
        mockedReq.return_value = MockResponse([{'Repo': 'CasinoSlotMachine', 'Number of commits': 3},
                                               {'Repo': 'CS570-DataStructures', 'Number of commits': 5},
                                               {'Repo': 'GEDCOM-Parser-Project---CS-555', 'Number of commits': 30},
                                               {'Repo': 'German-English-Laguage-Translator', 'Number of commits': 2},
                                               {'Repo': 'helloworld', 'Number of commits': 2},
                                               {'Repo': 'kg_nicole894_2021', 'Number of commits': 3},
                                               {'Repo': 'Multiplayer-tic-tac-toe', 'Number of commits': 4},
                                               {'Repo': 'NicoleAnnikaGonsalves_Projects_Python',
                                                'Number of commits': 2},
                                               {'Repo': 'PythonHackerRankChallenges', 'Number of commits': 3},
                                               {'Repo': 'SSW-567-HW02a', 'Number of commits': 13},
                                               {'Repo': 'SSW567-HW01', 'Number of commits': 2},
                                               {'Repo': 'SSW567-HW04GitApi', 'Number of commits': 10}])

        result = get_repo_commits('nicole894')
        x = result[1]
        self.assertEqual(x['Number of commits'], 5)


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
