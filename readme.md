# 🐸 Frogger Turtle Graphics 🐸

This repository hosts a Python-based version of the classic arcade game, Frogger, recreated using Turtle graphics.

## Table of Contents
- [Introduction](#introduction)
- [Technical Highlights](#technical-highlights)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## 🎮 Introduction
Frogger is a popular arcade game developed by Konami in 1981. This project aims to replicate Frogger's gameplay using Python and Turtle graphics. The game revolves around a frog that the player guides across a busy road and a river full of logs to get to safety.

## 💡 Technical Highlights
This project offers a practical example of Object-Oriented Programming (OOP) principles. It includes the use of classes like `CarManager`, `LogManager`, and `Player`, which encapsulate related data and behavior, providing a high level of abstraction. The `Player` class notably showcases inheritance by extending from the `Turtle` class. Modularity is highlighted with distinct Python files for each class, improving readability and maintainability.

## 🌟 Features
* Navigation through the game world using keyboard controls (Up, Down, Right, Left keys).
* Dynamic obstacles in the form of cars and logs.
* Gradually increasing difficulty by increasing game speed after each level.
* Option to replay the game after game over or after beating the game.

## 🔧 Installation

1. Make sure Python is installed on your system. If not, you can download it [here](https://www.python.org/downloads/).

2. Make sure Git is installed on your system. If not, you can download it [here](https://git-scm.com/downloads).

3. Open your system's command line interface, and clone the repository using the following command:
   ```
   git clone https://github.com/DanielVenette/Day-23_TurtleCrossing-Frogger.git
   ```

4. Change to the directory of the cloned repository:
   ```
   cd Day-23_TurtleCrossing-Frogger
   ```

## 🎯 Usage
Simply run the `main.py` script with Python to start the game:
```
python main.py
```
Here are the controls for the game:
- Use the "Up" arrow key to move the frog up.
- Use the "Down" arrow key to move the frog down.
- Use the "Right" arrow key to move the frog right.
- Use the "Left" arrow key to move the frog left.
- Use the "r" key to reset the frog to the starting position.

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
