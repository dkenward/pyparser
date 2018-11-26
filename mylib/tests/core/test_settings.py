"""
Test that the settings module creates a config file and can take new settings
"""

import unittest
from mylib.core.settings import SettingsModel

class SettingsModelTest(unittest.TestCase):
    
    def test_init(self):
        #default settings
        settings=SettingsModel()
        #Test that a settings file was created in the right directory and that the settings parameters are appropriate
        

    
    
if __name__ == "__main__":
    unittest.main()