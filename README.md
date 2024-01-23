# Monoalphabet Cipher Breaker

<div align="center">

[![Python](https://img.shields.io/badge/Python-black?logo=python&logoColor=white&labelColor=grey&color=%233776AB)](<https://www.python.org/> "Python")
[![License: MIT](<https://img.shields.io/github/license/danielfeitopin/monoalphabet-cipher-breaker>)](LICENSE "License")
[![GitHub issues](https://img.shields.io/github/issues/danielfeitopin/monoalphabet-cipher-breaker)](<https://github.com/danielfeitopin/monoalphabet-cipher-breaker> "Issues")
[![GitHub stars](https://img.shields.io/github/stars/danielfeitopin/monoalphabet-cipher-breaker)](<https://github.com/danielfeitopin/monoalphabet-cipher-breaker/stargazers> "Stars")

</div>

This repository contains a Python program for decoding a substitution cipher text using frequency analysis and letter substitution.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

Python 3.9

### Installation

Clone this repository

```bash
git clone https://github.com/<username>/<repository>.git
```

Change directory to the cloned repository

```bash
cd <repository>
```

## Usage

The program can be run using the following commands:

### Linux

```bash
python monoalphabet_breaker.py <path_to_cipher_file>
```

### Windows

```cmd
monoalphabet_breaker.py <path_to_cipher_file>
```

## How It Works

The program performs the following steps:

- Reads the cipher text file.
- Analyzes the text for letter frequencies and statistics.
- Prompts the user for substitution commands to decode the text.
- Displays the substituted text and the substitution table.

### Help

```
Commands:
help: Show this help menu.
set a b: Includes 'a' as the plain text key with value 'b' in the confirmed dict.
unset a: Removes key 'a' from confirmed dict.
exit: Quit the program.
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE "License") file for details.
