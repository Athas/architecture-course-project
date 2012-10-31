### Architectural Prototype

For setup, make sure Python setup tools are installed, and the `pip` command
is available.

Run the following in the main project directory (either in a virtual
environment or as root):
    
    pip install -r requirements.txt

### Execution

Execute the following command to run the STS prototype.

    python src/runserver.py

Execute the following command to start up a simple simulation of a
truck fleet.

    python src/trucksim.py

You can then make API queries using curl, for example to list all
truck positions within ten distance units of point (0,0):

    curl localhost:5000/api/location/0.0/0.0/10.0

(You'll have to wait about thirty seconds for the truck simulation to
send data.)
