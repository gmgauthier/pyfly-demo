# API TESTING WITH HOVERFLY (HoverPy)

### WHAT

This is a very simple project to demonstrate the perported uses of HoverFly (an api mocking/simulation tool). In this case, the testing use case is demonstrated by way of a custom pytest suite found in the tests directory.

### HOW

1> Run the included `install.sh` script. This will:
* confirm that you have python3 installed and ready for use
* confirm that you have the HoverFly CLI installed and ready for use
* confirm that you have pipenv for python3, and configure your project virtual environment

2> Run the included `rundemo.sh` script, after install. This will:
* use the pipenv environment to execute the hoverfly tests with pytest. What are these tests doing? 1: fire up the flask app. 2: hit both the GET endpoint and the POST endpoint, and execute a simple assert on the response JSONs. The test is actually using the stored session data for its comparison, rather than testing within the session itself. The suite deletes the session data files, when all tests are complete.

### DETAILS

The `/app` directory contains a very simple Flask server app, designed to emulate a live application with available api endpoints. It's useless beyond the scope of this demo. It models two simple GET requests, and a simple POST request, both of which return json responses as many of our service APIs do. 

The `/tests` directory contains a few standard Flask app unit tests, merely for reference. The main event, is the `test_hov.py` file, which contains the test code that includes the use of HoverFly capture/simulate code. It's actually a bit underwhelming, because of how easy it is to use in tests.

The point of having both sets of tests, is to show the difference between what a set of unit tests on an api project would look like, compared with a separate set of hoverfly api tests, which would be written to talk directly to a live api (note how the hoverfly tests require me to start the server in the setup).

I'm not sure if the hoverfly CLI binaries are actually necessary for the python bindings to work, but I added the installation of them here anyway, just to be sure, and to provide some documentation for future installations.

Why does it matter that we're using stored session data, rather than executing asserts during an active session? Well, for one thing, the stored session data could be used to execute mocked tests at a later date (the server need not be live). Or, mock sessions could be used to model CONTRACTS. Or, they could be used for ongoing development on a new endpoint.

More experimentation needs to be done, to determine the full value of the tool.
