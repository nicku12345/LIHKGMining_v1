'''
The main purpose of this file is to assemble all unit tests
'''

'''
MODEL TESTS
'''
from mining.tests.models_tests.UserModelTests import *
from mining.tests.models_tests.MessageModelTests import *
from mining.tests.models_tests.ThreadModelTests import *


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

'''
HELPERS TESTS
'''
from mining.tests.managers_tests.helpers_tests.LIHKGThreadsHelperTests import *
from mining.tests.managers_tests.helpers_tests.PlaywrightHelperTests import *

'''
WORKERS TESTS
'''
from mining.tests.background_workers_tests.LIHKGThreadsJobTests import *
from mining.tests.background_workers_tests.LIHKGThreadsWorkQueueTests import *