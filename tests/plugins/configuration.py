import yaml
import pytest
import demoauto.configuration.base_configuration as config

@pytest.fixture(scope='session')
def base_config(pytestconfig):
    with open('config.yml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        config.global_data.os = data['configuration']['os']
        config.global_data.browser = data['configuration']['browser']

