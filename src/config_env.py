from dotenv import dotenv_values

def config_env():
    return dotenv_values('.env')