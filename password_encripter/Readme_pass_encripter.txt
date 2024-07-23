***************************************
*             Library                 *
***************************************

Fernet uses symmetric encryption, which means the same key is used for both
encryption and decryption. When you create a Fernet key, it is a 256-bit key
that is used to encrypt and decrypt your data securely.

***************************************
*            Functioning              *
***************************************

This script works by taking a password as input.
The program will encrypt it and return two documents:

1. **'pass.key'**: Contains the encryption key.
2. **'pass_enc'**: Contains the encrypted password.
