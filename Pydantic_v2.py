import os
from pydantic import Field, AliasChoices
from pydantic_settings import BaseSettings, SettingsConfigDict, EnvSettingsSource 

# Set enviroment variables with the prefix

os.environ['PRODUCTION_AUTH_KEY'] = 'test_auth_key'
os.environ["PRODUCTION_MY_API_KEY"] = 'test'
os.environ['PRODUCTION_ENV1'] = 'https://mysuperurl.ru'
print(os.environ)

class Settings(BaseSettings):

    service_name: str = Field(default='default')
    auth_key: str 
    my_api_key: str = Field() # alias='my_key')
    # my_api_key: str 
    url: str = Field(validation_alias=AliasChoices('env1', 'env2'))
    
    model_config = SettingsConfigDict()
    # model_config['env_file'] = '.env'
    model_config['env_prefix'] = 'production_' 
    print(model_config)
    # model_config = SettingsConfigDict(env_prefix='production_', env_file='.env', case_sensitive=False)

print(Settings().model_dump())
