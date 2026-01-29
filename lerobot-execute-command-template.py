#!/usr/bin/env python3
"""
Config File Example for High School Students
===========================================

This script demonstrates how to use configuration files (YAML) 
to manage complex command-line arguments in Python.

Instead of typing long commands with many parameters, we can:
1. Store all settings in a config file
2. Load the config in Python
3. Build and execute the command programmatically
"""

import json
import yaml
import subprocess
import argparse
from pathlib import Path

def execute_command(args):
    """
    Execute the command or show what would be executed.
    
    Args:
        args (list): Command line arguments
    """

    ### Pseudo code 
    
    print("🚀 Executing command...")
    try:
        # Execute the command
        ### MODIFY: Modify the next line to run the command
        result = subprocess.run(...)
        print("✅ Command executed successfully!")
        print(f"Output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Command failed with return code {e.returncode}")
        print(f"Error: {e.stderr}")


def build_command_args(config):
    """
    Convert configuration dictionary to command line arguments.
    
    Args:
        config (dict): Configuration data
        
    Returns:
        list: Command line arguments as a list
    """

    ### Pseudo code example
    args = ['lerobot-calibrate']  # Base command for example
    
     
    # Teleop configuration
    ### MODIFY: Complete the following. Append to 'args' all necessary parameters as with teleop.type
    ### We want to append a text/string as if we would write it in the terminal
    if 'teleop' in config:
        teleop = config['teleop']
        if 'type' in teleop:
            args.append(f"--teleop.type={teleop['type']}")
        
        for key, value in teleop.items():
            if key != 'type':
                args.append(f"--teleop.{key}={value}")
    
    
    ### MODIFY: Print the variable args here to see if everything is correct
    print(f"DEBUG: Final command arguments list: {args}")

    return args


def load_config(config_path):
    """
    Load configuration from YAML file.
    
    Args:
        config_path (str): Path to the configuration file
        
    Returns:
        dict: Configuration data
    """
    
    config_path = Path(config_path)
    
    ### MODIFY: Complete the following to read a YAML file
    ### Search which python command reads a YAML file
    with open(config_path, 'r') as file:
        print("I'm here")
        return yaml.safe_load(file)

    
def main():
    """Main function to demonstrate config file usage."""
    
    ### Set up the parsing of the command line aruments
    ### For exampple, if in terminal I execute: python lerobot-execute-command-template.py my_config.yaml 

    parser = argparse.ArgumentParser(description='Run command from config file')

    ### MODIFY: change the following line to read 'config'
    parser.add_argument('config')


    args = parser.parse_args()

    ### NOTE: After the previous command, "arg.config" is the variable that has the path to the config file

    ### Try to read the configuration file and execute the command
    try:
        ## Load configuration
        print(f"📁 Loading configuration from: {args.config}")

        ### MODIFY: Pass the argument needed, which variable? has the path to the config file
        ### NOTE: This function is above, and needs the path to the config file
        config = load_config(args.config)

        ### MODIFY: go the function build_command_args and complete it based on the comments
        command_args = build_command_args(config)

        
        print(f"🚀 Ready to run: {' '.join(command_args)}")

        ### NEW -- The following function will now execute the command in terminal
        # Execute or show command
        execute_command(command_args)


    except Exception as e:
        print(f"❌ Error: {e}")

### Main default function
if __name__ == '__main__':
    main()
