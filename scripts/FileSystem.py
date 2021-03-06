
# SYSTEM IMPORTS
import os

# PYTHON PROJECT IMPORTS
import Utilities

ROOT = 1                    # the absolute path to the top level of the project
WORKING = 2                 # the absolute path to the build directory of the project
# the absolute path to the directory where all static scripts are kept
#   (a static script is abstract enough that it can be shared between
#    projects, this script is a good example)
SCRIPT_ROOT = 3

MANUAL_DIR = 5              # the absolute path to the documentation directory of the project
WORKSPACE_DIR = 6          # the absolute path to the top level directory of c++ source directories
TEST_REPORT_DIR = 7         # the absolute path to the directory containing test reports
CMAKE_BASE_DIR = 8          # the absolute path to the top level directory of CMAKE utilities

# the absolute path to the CMAKE toolchain directory
#   - toolchain files are used for certain platforms to separate
#     CMAKE functionality
CMAKE_TOOLCHAIN_DIR = 9
CMAKE_MODULE_DIR = 10       # the absolute path to the CMAKE modules directory
OUT_ROOT = 11               # the absolute path to the directory where built code goes
INSTALL_ROOT = 12           # the absolute path to the top level directory where all built code goes
INSTALL_DIR = 13            # the absolute path to the directory where public c++ headers go when built
LOG_DIR = 14                # the absolute path to the directory where all log files will be written

# the absolute path to the directory containing the file that the build system
# uses to determine which libraries depend on others. The build system
# will move these (project) libraries into the currently building project's
# workspace for linking.
GLOBAL_DEPENDENCIES = 15
BUILD_DEPENDENCIES = 16
PACKAGE = 17
IDE_ROOT = 18


# a method to get the absolute path to a directory within the project based
# on the FileSystemDirectory enums described above
def getDirectory(directoryEnum, configuration='', projectName=''):
    if directoryEnum == ROOT:
        return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    elif directoryEnum == WORKING:
        return os.path.join(getDirectory(ROOT), 'build', configuration, projectName)
    elif directoryEnum == SCRIPT_ROOT:
        return os.path.join(getDirectory(WORKING), 'scripts')
    elif directoryEnum == MANUAL_DIR:
        return os.path.join(getDirectory(ROOT), 'projects', 'manual')
    elif directoryEnum == WORKSPACE_DIR:
        return os.path.join(getDirectory(ROOT), 'workspace')
    elif directoryEnum == TEST_REPORT_DIR:
        return os.path.join(getDirectory(WORKING, configuration, projectName), 'testReports')
    elif directoryEnum == CMAKE_BASE_DIR:
        return os.path.join(getDirectory(WORKSPACE_DIR), projectName, 'cmake')
    elif directoryEnum == CMAKE_TOOLCHAIN_DIR:
        return os.path.join(getDirectory(CMAKE_BASE_DIR, projectName), 'toolchains')
    elif directoryEnum == CMAKE_MODULE_DIR:
        return os.path.join(getDirectory(CMAKE_BASE_DIR, projectName), 'modules')
    elif directoryEnum == OUT_ROOT:
        return os.path.join(getDirectory(WORKING, configuration, projectName), 'out')
    elif directoryEnum == INSTALL_ROOT:
        return os.path.join(getDirectory(OUT_ROOT, configuration, projectName), 'installRoot')
    elif directoryEnum == INSTALL_DIR:
        return os.path.join(getDirectory(OUT_ROOT, configuration, projectName), 'install')
    elif directoryEnum == LOG_DIR:
        return os.path.join(getDirectory(WORKING, configuration, projectName), 'logs')
    elif directoryEnum == GLOBAL_DEPENDENCIES:
        return os.path.join(getDirectory(WORKING), "globalPackageDependencies")
    elif directoryEnum == BUILD_DEPENDENCIES:
        return os.path.join(getDirectory(WORKING, configuration, projectName), "dependencies")
    elif directoryEnum == PACKAGE:
        return os.path.join(getDirectory(WORKING, configuration, projectName), "package")
    elif directoryEnum == IDE_ROOT:
        return os.path.join(getDirectory(OUT_ROOT, configuration, projectName), "IDE")
    else:
        Utilities.failExecution("Unknown directoryEnum: [%s]" % directoryEnum)
