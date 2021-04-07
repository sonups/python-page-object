import yaml
import pytest
import demoauto.configuration.base_configuration as config
import sys

@pytest.fixture(scope='session')
def base_config(pytestconfig):
    if sys.platform == 'win32':
        with open(sys.path[0]+'\\config.yml') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            config.global_data.os = data['configuration']['os']
            config.global_data.browser = data['configuration']['browser']

    elif sys.platform == 'linux':
        with open(sys.path[0]+'/config.yml') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            config.global_data.os = data['configuration']['os']
            config.global_data.browser = data['configuration']['browser']

