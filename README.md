# Robotic Code Representation Generator

The Robotic Code Representation Generator is a Python module that provides a class for encoding issued commands into Robotic Code Representations (RCR). RCR is a method for efficiently encoding commands issued to a robot.

## Algorithm Description

The core algorithm in this module generates RCR codes for a list of issued commands using a frequency-based encoding approach. Here's how it works:

1. The module defines a `Node` class to represent nodes in the encoding tree.

2. The `RoboticCodeRepresentationGenerator` class takes a list of issued commands as input and constructs an encoding tree based on the frequency of each command.

3. RCR codes are generated for each unique issued command based on their frequency of occurrence. More frequent commands receive shorter codes, while less frequent commands receive longer codes.

4. You can run the script by executing the following command in your terminal:

```bash
python main.py
