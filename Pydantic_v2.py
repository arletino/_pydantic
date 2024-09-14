import os
from pydantic import Field, AliasChoices
from pydantic_settings import BaseSettings, SettingsConfigDict, EnvSettingsSource 

# Set enviroment variables with the prefix

os.environ['PRODUCTION_AUTH_KEY'] = 'test_auth_key'
os.environ["PRODUCTION_MY_API_KEY"] = 'test'
os.environ['PRODUCTION_ENV2'] = 'https://mysuperurl.ru'
#print(os.environ)

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='PRODUCTION_', env_file='.env')

    service_name: str = Field(default='default')
    auth_key: str 
    key: str = Field(alias='my_api_key')
    url: str = Field(validation_alias=AliasChoices('env1', 'env2'))

print(Settings().model_dump())