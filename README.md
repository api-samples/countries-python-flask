Python Countries REST JSON API example.

Open the project with IntelliJ IDEA 14 with the Python plugin installed.

Build:

    sudo docker build --rm -t mikaelhg/countries-python-flask .

Run:
     
    sudo docker run -it --rm -p 5000:5000 mikaelhg/countries-python-flask 

Run in production with uwsgi:
     
    sudo docker run -it --rm -p 5000:5000 mikaelhg/countries-python-flask uwsgi --http :5000 -w countries:app
