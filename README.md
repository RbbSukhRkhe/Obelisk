# Obelisk Shell

A custom command-line shell built in Python, designed to bring a fun and colorful twist to terminal interactions. Obelisk mimics classic shell functionality with commands like `ls`, `cd`, and `speak`, enhanced by `colorama` for vibrant output. Perfect for learning about CLI development or just playing around with a personalized shell!

## Features

- **Core Commands**:
  - `ls [path]`: Lists files in the specified or current directory.
  - `cd [path]`: Changes the working directory, with error handling for invalid paths.
  - `speak [text] [color]`: Prints text in a chosen color (e.g., blue, red, green) using `colorama`.
  - `whereami`: Displays the current working directory (like `pwd`).
  - `whoami`: Shows the current user’s login name.
  - `clear`: Clears the terminal screen.
- **Interactive Prompt**: Shows user, shell name, and current directory in a colorful format.
- **Error Handling**: Gracefully manages issues like missing files or permissions.
- **Exit Commands**: Use `exit` or `quit` to close the shell.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/RbbSukhRkhe/Obelisk.git
   cd Obelisk
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.6+ installed. Install `colorama` via pip:
   ```bash
   pip install colorama
   ```

3. **Run the Shell**:
   Execute the main script:
   ```bash
   python obelisk.py
   ```

## Usage

Once the shell starts, you’ll see a prompt like:
```
user@Obelisk:/current/path:
```

Try these commands:
- List files: `ls`
- Change directory: `cd Documents`
- Print colored text: `speak Hello blue`
- Check your location: `whereami`
- See your username: `whoami`
- Clear the screen: `clear`
- Exit: `exit`

Example:
```
user@Obelisk:~/Obelisk: ls
obelisk.py  README.md
user@Obelisk:~/Obelisk: speak Testing green
Testing  # (in green text)
user@Obelisk:~/Obelisk: whereami
/home/user/Obelisk
```

## Contributing

Feel free to fork the repo and submit pull requests with improvements! Ideas for new commands, better error handling, or UI tweaks are welcome. Please include tests and update the README if adding features.

1. Fork the project.
2. Create a feature branch (`git checkout -b feature/AmazingCommand`).
3. Commit your changes (`git commit -m 'Add new command'`).
4. Push to the branch (`git push origin feature/AmazingCommand`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Built with ☕ by [Sukhanpreet Singh Dhillon](https://github.com/RbbSukhRkhe). Enjoy exploring the shell!
