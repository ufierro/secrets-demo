#!/usr/bin/env python
import random
import logging
import os


log = logging.getLogger()

for _ in range(0, 150):
    print(random.randint(0,100))

logging.warning("Imprimiendo credenciales")
print("cadenaConCredenciales")
# Retrieves PASSWORD1 environment variable, falls back to string if not found
print(os.getenv("PASSWORD1", "no_declaraste_nada"))
