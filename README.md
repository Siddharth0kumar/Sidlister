# Sidlister - Subdomain Enumeration Tool
![Sidlister](https://github.com/Siddharth0kumar/Sidlister/assets/89460704/1573b13b-1664-4bae-a200-be1f37d9b775)

Sidlister is a Python-based subdomain enumeration tool that leverages the power of Sublist3r to quickly and efficiently discover subdomains associated with a target domain. With a user-friendly command-line interface and a touch of humor, Sidlister makes the process of subdomain enumeration not only effective but also fun.

**Key Features:**

- Utilizes Sublist3r to perform subdomain enumeration.
- Provides a stylish and humorous ASCII art introduction upon execution.
- Generates organized HTML reports containing enumerated subdomains.
- Simple and straightforward usage for both beginners and experienced users.
- Easily installed as a global command for quick access.

**Usage:**

Sidlister is designed to simplify the process of subdomain enumeration. Users can run the tool, enter the target domain, and watch as Sidlister efficiently discovers and lists subdomains in an HTML report. The tool is perfect for security professionals, penetration testers, and anyone interested in understanding the subdomain landscape of a website.

**Installation:**

Sidlister can be installed with a single command, making it accessible from any terminal window. Detailed installation instructions are provided in the README file.

**License:**

Sidlister is open-source software and is released under the MIT License. Users are encouraged to modify and customize the tool to suit their needs.

**Acknowledgments:**

Sidlister relies on the power of Sublist3r for subdomain enumeration and pyfiglet for creating eye-catching ASCII art introductions. The tool was developed with the goal of simplifying subdomain enumeration while adding a touch of fun to the process.

This description can be customized further to match your tool's unique features and characteristics.

## Introduction

Sidlister is a Python tool for enumerating subdomains of a domain using Sublist3r. It also provides a fun ASCII art introduction when executed.

## Installation

To install Sidlister, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/siddharth0kumar/Sidlister.git
   ```

2. Navigate to the Sidlister directory:

   ```bash
   cd Sidlister
   ```

3. Run the setup script to install Sidlister as a global command:

   ```bash
   chmod +x sidup.sh
   ./sidup.sh
   ```

## Usage

After installing Sidlister, you can use it as follows:

1. Run Sidlister by typing:

   ```bash
   python3 Sidlister.py
   
   ```
   # @Points to remember 

2. Enter the domain name (without http/https) when prompted.

3. Sidlister will enumerate subdomains using Sublist3r and save the results in an HTML file.

4. The HTML file will be saved as `mephisto_results.html` in the current directory.

5. You can view the results by opening `mephisto_results.html` in a web browser.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Siddharth0kumar/Sidlister/blob/main/LICENSE) file for details.

## Acknowledgments

- ASCII art generated using [pyfiglet](https://pypi.org/project/pyfiglet/).
- Subdomain enumeration performed using [Sublist3r](https://github.com/aboul3la/Sublist3r).

