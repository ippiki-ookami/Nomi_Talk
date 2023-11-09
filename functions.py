import os
import json
from pathlib import Path

config_path = 'nt_config.json'

# Makes cookies usable for Selenium
def clean_cookies(cookie_path):
   if os.path.exists(cookie_path):
      with open(cookie_path, 'r') as cookie_file:
         cookies = json.load(cookie_file)
         for cookie in cookies:
            for key in list(cookie.keys()):
               if cookie[key] == 'false':
                  cookie[key] = False
               if cookie[key] == 'true':
                  cookie[key] = True
            if 'sameSite' in cookie:
               if cookie['sameSite'] == 'lax':
                  cookie['sameSite'] = 'Lax'
               elif cookie['sameSite'] == 'strict':
                  cookie['sameSite'] = 'Strict'
               else:
                  cookie['sameSite'] = 'None'
            if 'partitionKey' in cookie:
               del cookie[key]
   return cookies
            


# Loads or creates config file
def load_config():
   
   if os.path.exists(config_path):
      with open(config_path, 'r') as config_file:
         config_data = json.load(config_file)
         return config_data
      
   else:
      config_data = {
         'record_sound': None,
         'nomis': [],
         'default_nomi': None,
         'key_shortcut': None,
         'input': None,
         'cookies': '', 
         'ff_profile_url': '',
         'cloud_credentials': '',
         'eleven_api': ''
      }
      with open(config_path, 'w') as config_file:
         json.dump(config_data, config_file, indent=4)
         return config_data
         

def truncate_string(input_string, max_length):
   if input_string:
      if len(input_string) > max_length:
         return input_string[:max_length-3] + "..."
      else:
         return input_string
         
# Udpates config file         
def update_config(config_data):
   with open(config_path, 'w') as config_file:
      json.dump(config_data, config_file, indent=4)
         

# Writes settings to config
def update_settings(config_data, **kwargs):
   for key, value in kwargs.items():
      if value:
         config_data[key] = value
   update_config(config_data)
   
# Creates and adds Nomi to config
def create_nomi(config_data, details):
   if not config_data['default_nomi']:
      config_data['default_nomi'] = details
   config_data['nomis'].append(details)   
   update_config(config_data)
   
   
   
   
   
