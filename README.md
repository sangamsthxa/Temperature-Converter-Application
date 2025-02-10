# Temperature Converter Docker Application

This is a Python-based temperature converter that supports conversion between Celsius, Fahrenheit, and Kelvin, storing history using Docker volumes.

## Setup Instructions
1. Build the Docker image:
   ```
   docker build -t temp-converter .
   ```
2. Run the container with a mounted volume for persistence:
   ```
   docker run -it --rm -v $(pwd)/history.txt:/application/history.txt temp-coverter
   ```

## Features
- Convert temperature between Celsius, Fahrenheit, and Kelvin.
- View history stored in a mounted volume.

## Usage
- Follow on-screen instructions to perform conversions.
- View history by selecting the appropriate option.
- The conversion history is saved in `/history.txt` on your host machine.

## Docker Concepts Used
- **Base Image**: Uses `python:3.9` as the base image.
- **Volume Mounting**: Mounts `./application` directory for persistent history storage.
- **CMD Instruction**: Sets `python temperature_converter.py` as the default execution command.
```