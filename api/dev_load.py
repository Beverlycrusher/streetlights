import os
import models
FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))
test_file_path = os.path.join(FOLDER_PATH,"mock.csv")

print(test_file_path)
poles = open(test_file_path,'r')
print(models)
for pole in poles:
    pass