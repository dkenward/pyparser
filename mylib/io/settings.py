"""

"""
import os
import json
import platform

class SettingsModel:
    """
    A model for saving settings
    
    Attributes
    ----------
    variables: dict
        dictionary of variables and the associated schema
    
    Methods
    -------
    load()
        Loads a the config file if it exists, returns nothing if it doesn't
        
    Save()
        Saves a config file to the user's home directory named mylib_config.json
    
    Usage
    -----
    
    """
    
    config_dirs = {
        'Windows': os.environ.get('LOCALAPPDATA','~/AppData/Local'),
        'Linux': os.environ.get('$XDG_CONFIG_HOME', '~/config')}
    
    variables = {
        'database_host':{'type':'string','format':'uri','value':'localhost'},
        'database_port':{'type':'integer','maximum':65535,'value': 27017}
        }
    
    def __init__(self,filename='mylib_config.json',path='~'):
        """determine the path to the config file"""
        
        #check for operating system variable for config files
        if path == '~':
            path = self.config_dirs.get(platform.system(),'~')
            
        self.path = os.path.join(
            os.path.expanduser(path),filename)
        
    def load(self):
        """Load the settings from the file"""
        # if the file doesn't exist, return
        if not os.path.exists(self.filepath):
            return
        
        # open the file and read in the raw values
        with open(self.filepath, 'r') as fh:
            raw_values = json.loads(fh.read())

        # don't implicitly trust the raw values, 
        # but only get known keys
        for key in self.variables:
            if key in raw_values and 'value' in raw_values[key]:
                raw_value = raw_values[key]['value']
                self.variables[key]['value'] = raw_value
    
    def save(self, settings=None):
        """ Save a settings file to the user's home directory """
        json_string = json.dumps(self.variables)
        with open(self.filepath, 'w') as fh:
            fh.write(json_string) 
            
    def set(self,key,value):
        """Set a config setting """
        if (
            key in self.variables and
            type(value).__name__ == self.variables[key]['type']
            ):
            self.variables[key]['value'] = value
        else:
            raise ValueError("Bad key or wrong variable type")