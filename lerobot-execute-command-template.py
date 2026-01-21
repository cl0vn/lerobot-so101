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


def load_config(config_path):
    """
    Load configuration from YAML file.
    
    Args:
        config_path (str): Path to the configuration file
        
    Returns:
        dict: Configuration data
    """
    
    ### Pseudo code
    ## config_path = Path(config_path)
    
    ## with open(config_path, 'r') as file:
        

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
    if 'teleop' in config:
        teleop = config['teleop']
        if 'type' in teleop:
            args.append(f"--teleop.type={teleop['type']}")
        if 'port' in teleop:
            args.append(f"--teleop.port={teleop['port']}")
        if 'id' in teleop:
            args.append(f"--teleop.id={teleop['id']}")
    
    
    return args


def execute_command(args):
    """
    Execute the command or show what would be executed.
    
    Args:
        args (list): Command line arguments
    """

    ### Pseudo code 
    command = ' '.join(args)
    print(f"Command to execute:\n{command}\n")
    
    print("🚀 Executing command...")
    try:
        # Execute the command
        result = subprocess.run(...)
        print("✅ Command executed successfully!")
        print(f"Output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Command failed with return code {e.returncode}")
        print(f"Error: {e.stderr}")


def main():
    """Main function to demonstrate config file usage."""
    
    ### Set up the parsing of the command line aruments
    ### For exampple, if in terminal I execute: python lerobot-execute-command-template.py my_config.yaml 

    ### Pseudo code example
    parser = argparse.ArgumentParser(...)
    parser.add_argument(..)
    parser.add_argument(..)    

    ### Try to read the configuration file and execute the command
    try:
        ## Load configuration
        print(f"📁 Loading configuration from: {args.config}")
        config = load_config(...)
        
        ## Build command arguments
        ## print("🔧 Building command arguments...")
        command_args = build_command_args(config)        
        # Execute or show command
        execute_command(command_args)
        
    except Exception as e:
        print(f"❌ Error: {e}")

### Main default function
if __name__ == '__main__':
    main()