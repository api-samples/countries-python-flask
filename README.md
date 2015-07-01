Python Countries REST JSON API example.

Open the project with IntelliJ IDEA 14 with the Python plugin installed.

Build:

    sudo docker build --rm -t mikaelhg/countries-python-flask .

Run:
     
    sudo docker run -it --rm -p 5000:5000 mikaelhg/countries-python-flask 

When developing locally, just create a python virtualenv, run `pip install -r requirements.txt`,
and execute `countries.py` for the application, or `rest_tests.py` for the functional tests.

You can also run the unit tests in the Docker container:

    sudo docker run -it --rm mikaelhg/countries-python-flask python rest_tests.py
