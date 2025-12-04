# Lunar Microservice
This microservice allows the user to receive data about the moon at the current time they request it.

## Run as a Test
To run this program as a test you can ignore index.php and start_lunar.php

Step 1: open up your terminal and run server.py with this command:
```bash
py server.py
```

Step 2: while the server is running, open up another terminal and enter this:
```bash
node test.js
```

Step 3: this will confirm that the microservice can run happily on your device
Troubleshooting: If you do not have ephem installed, run the following command to install it:
```bash
py -m pip install ephem
```

## Run Within Your Program
To run this program within your program:

Step 1: Add start_lunar.php into your project folder, and not the microservice one. Do include the microservice file in your project. <br>
Step 2: Adjust the file paths in start_lunar.php to your project's. <br>
Step 3: Run server.py in the background using a terminal with this command:
```bash
py server.py
```
Step 4: Call start_lunar.php to get your moon data, I put an example php file of this call in "index.php".