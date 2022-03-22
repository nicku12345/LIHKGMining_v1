'''
The main purpose of this file is to assemble all unit tests
'''

'''
MODEL TESTS
'''
from mining.tests.models_tests.UserModelTests import *


'''
REPOSITORIES TESTS
'''
from mining.tests.repositories_tests.UsersRepositoryTests import *
from mining.tests.repositories_tests.ThreadsRepositoryTests import *


'''
MANAGERS TESTS
'''
from mining.tests.managers_tests.UsersManagerTests import *
from mining.tests.managers_tests.ThreadsManagerTests import *