# OPCUA Client-Server Documentation

# Introduction

The OPCUA Client-Server is a program designed to facilitate communication between an OPC client and server, allowing retrieval of data from the client. This documentation provides instructions on how to use the program effectively.

## Usage
Keep both the client and server in same network and expose OPC server to client

# Features
Establishes communication between OPC client and server.
Retrieves data from the client.
Displays results graphically for different sensors.
Usage
Prerequisites
Ensure that both the OPC client and server are on the same network and that the OPC server is exposed to the client.

# Running the server
Execute the following command to run the server, replacing <server-ip> with the actual IP address of the server:


Copy code
python manage.py runserver <server-ip>:8000

# Running the Client
Execute the following command to run the client:

Copy code
python manage.py runserver


# Creating and Logging In
Follow the prompts to create a user account and log in using the provided credentials.

# Starting the OPC Server
Access the following URL to start the OPC server, replacing <server-ip> with the actual IP address of the server:

Copy code
http://<server-ip>:8000/start-server


# Result
The results will be displayed graphically for different sensors.

# Note
Currently, the program can only be executed on a local machine.
Ensure proper network configuration for seamless communication between client and server.

# Conclusion
The OPCUA Client-Server simplifies the process of retrieving data from OPC clients through a user-friendly interface. By following the instructions provided in this documentation, users can effectively utilize the program to meet their data retrieval needs.
