# RSA Encryption and Decryption Project

## Overview

This project implements RSA (Rivest-Shamir-Adleman) encryption and decryption in Python. RSA is a widely used public-key cryptosystem that provides secure communication over an insecure channel. This implementation includes key generation, encryption, and decryption functionalities.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Features

- Key generation for RSA encryption and decryption
- Encryption of plaintext messages
- Decryption of ciphertext messages
- Supports variable key sizes for increased security

## Requirements

- Python 3.x

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/RSA-Encryption-Decryption.git
cd RSA-Encryption-Decryption
```

2. Install dependencies (if any):

```bash
# If using a virtual environment
pip install -r requirements.txt
```

## Usage

1. Generate RSA key pair:

```bash
python rsa_key_generator.py
```

2. Encrypt a message:

```bash
python rsa_encrypt.py
```

3. Decrypt a ciphertext:

```bash
python rsa_decrypt.py
```

## Examples

### Key Generation

```bash
python rsa_key_generator.py
```

This will generate public and private keys and save them in the `keys/` directory.

### Encryption

```bash
python rsa_encrypt.py
```

Follow the prompts to enter the plaintext message and choose the public key file. The encrypted message will be saved in the `output/` directory.

### Decryption

```bash
python rsa_decrypt.py
```

Follow the prompts to enter the ciphertext message and choose the private key file. The decrypted message will be displayed on the console.

## Contributing

If you would like to contribute to the project, please follow these steps:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes
4. Test your changes
5. Commit your changes
6. Push your changes to your fork
7. Create a pull request

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code as per the terms of the license.
