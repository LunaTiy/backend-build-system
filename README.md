# Backend Build System

     ____             _                  _ 
    | __ )  __ _  ___| | _____ _ __   __| |
    |  _ \ / _` |/ __| |/ / _ \ '_ \ / _` |
    | |_) | (_| | (__|   <  __/ | | | (_| |
    |____/ \__,_|\___|_|\_\___|_| |_|\__,_|
     ____        _ _     _     ___
    | __ ) _   _(_) | __| |  / ___| _   _ ___| |_ ___ _ __ ___                              
    |  _ \| | | | | |/ _` |  \___ \| | | / __| __/ _ \ '_ ` _ \                             
    | |_) | |_| | | | (_| |  ___) | |_| \__ \ ||  __/ | | | | |                            
    |____/ \__,_|_|_|\__,_| |____/ \__, |___/\__\___|_| |_| |_|
                                    |___/
## Table of Contents

- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)

## Getting Started

### Prerequisites

    - Python >=v3.11 (https://www.python.org/downloads/)
    - Any other specific software or libraries

### Installation

    1. Download and install python v3.11 (https://www.python.org/downloads/)
    2. Install pdm to your os (or use another dependencies manage tool)
        2.1. Install pdm:
            - (Invoke-WebRequest -Uri https://pdm-project.org/install-pdm.py -UseBasicParsing).Content | python -
            or
            - pip install pdm
    3. Install requirements from pyproject.toml
        pdm sync -v
    4. Activate project venv
    5. Enjoy
