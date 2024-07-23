import os
import subprocess
from pathlib import Path

from dotenv import load_dotenv

def load_env_vars(env_file=".devcontainer/.env.devcontainer", 
        profile="~/.bashrc"
    ):
    # Set variables for later use
    found = False
    # Check if env_file exists
    if Path(env_file).exists():
        found = True
        print("Environment settings file found, continue processing.")
    else:
        print("Environment settings file was not found, unable to set variables.")
        
    if found:
        print("Start setting environment variables...")
        load_dotenv(env_file, override=True)

        # Set environment variables
        env_vars = {
            "DB_NAME": os.environ["DBNAME"],
        }

        bash_profile = os.path.expanduser(profile)

        for key, value in env_vars.items():
    	    subprocess.run(
                f'echo "export {key}={value}" >> {bash_profile}', shell=True, check=True
            )

        subprocess.run(f". {bash_profile}", shell=True, check=True)
        print("Environment variables set successfully.")
    
    
if __name__ == '__main__':
    print("Starting file...")
    load_env_vars()
    print("File complete.")
