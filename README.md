# Opencv

## Installation Guide

### Creating a Virtual Environment

Open your terminal or command prompt.

Run the following command to create a virtual environment:

    python -m venv <virtual_env_name>

Replace <virtual_env_name> with your desired environment name, e.g., opencv_env.

Example:

    python -m venv opencv_env

### Activating the Virtual Environment

On Windows:

    <virtual_env_name>\Scripts\activate

Example:

    opencv_env\Scripts\activate

On Mac/Linux:

    source <virtual_env_name>/bin/activate

Example:

    source opencv_enb/bin/activate

Once activated, your terminal prompt will change to include the virtual environment name, e.g., (opencv_env).

### Requirements

    opencv-python: For computer vision tasks.
    asyncio: For asynchronous I/O operations.
    numpy: For numerical computations.
    pynput: For controlling and monitoring input devices.

### Installation Steps

Install opencv-python:

    pip install opencv-python

Install asyncio:

    pip install asyncio

Install numpy:

    pip install numpy

Install pynput:

    pip install pynput

### Run

    python3 main.py
