import os
import platform

class znprj:
    def WriteNewSaveFile(project_name):
        OS = platform.system()
        FILE_FORMAT="PROJECT_NAME="+project_name+"\nOS_TYPE="
        