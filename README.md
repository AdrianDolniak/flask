# Simple Flask App

[![Build Status](https://travis-ci.com/AdrianDolniak/flask-hello-world.svg?branch=master)](https://travis-ci.com/AdrianDolniak/flask-hello-world) <a href="https://www.statuscake.com" title="Website Uptime Monitoring"><img src="https://app.statuscake.com/button/index.php?Track=4018761&Days=1&Design=5" /></a>


### Aplikacja Dydaktyczna wyświetlająca imię i wiadomość w różnych formatach dla zajęć o Continuous Integration, Continuous Delivery i Continuous Deployment.


Rozpocząnając pracę z projektem (wykorzystując virtualenv). Hermetyczne środowisko dla pojedyńczej aplikacji w python-ie:

    # ubuntu, add to ~/.bashrc
    $ source /usr/local/bin/virtualenvwrapper.sh
    
    # centos, add to ~/.bashrc
    $ source /usr/bin/virtualenvwrapper.sh
   
    # tworzymy hermetyczne środowisko dla bibliotek aplikacji:
    $ mkvirtualenv simple-flask-app
    $ pip install -r requirements.txt
    $ pip install -r test_requirements.txt

  Sprawdź: [documentację virtualenvwrappera](https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html) oraz [biblioteki flask](http://flask.pocoo.org).

Uruchamianie applikacji:

    # jako zwykły program
    $ python main.py

    # albo:
    $ PYTHONPATH=. FLASK_APP=hello_world flask run

Uruchamianie testów (see: http://doc.pytest.org/en/latest/capture.html):


    $ PYTHONPATH=. py.test
    $ PYTHONPATH=. py.test  --verbose -s

Kontynuując pracę z projektem, aktywowanie hermetycznego środowiska dla aplikacji py:

  
    $ source /usr/local/bin/virtualenvwrapper.sh # nie trzeba, jeśli już w .bashrc
    $ workon simple-flask-app

    # deaktywacja virtualenv
    $ deactivate

Integracja z TravisCI:

  
    # plik .travis.yml
    # budowa pakietu (Makefile - Docker)
    # instalacja pakietu do repozytorium współdzielonym z klientem 

https://hub.docker.com


## Pomocnicze


### Ubuntu

Instalacja python virtualenv i virtualenvwrapper:


    $ sudo pip install virtualenv
    $ sudo pip install virtualenvwrapper

Instalacja dockera: [dockerce howto](https://docs.docker.com/install/linux/docker-ce/ubuntu/)


    $ sudo apt-get remove docker docker-engine docker.io containerd runc
    
    $ sudo apt-get update
    $ sudo apt-get install \
        apt-transport-https \
        ca-certificates \
        curl \
        gnupg-agent \
        software-properties-common
        
    $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    
    $ sudo add-apt-repository \
        "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
        $(lsb_release -cs) \
        stable"
    

### Centos


Instalacja python virtualenv i virtualenvwrapper:


    $ yum install -y python-pip
    $ pip install -U pip
    $ pip install virtualenv
    $ pip install virtualenvwrapper

Instalacja docker-a: [dockerce howto](https://docs.docker.com/install/linux/docker-ce/centos/)


    $ yum remove docker \
        docker-common \
        container-selinux \
        docker-selinux \
        docker-engine

    $ yum install -y yum-utils

    $ yum-config-manager \
      --add-repo \
      https://download.docker.com/linux/centos/docker-ce.repo

    $ yum makecache fast
    $ yum install -y docker-ce
    $ systemctl start docker

### Materiały


https://virtualenvwrapper.readthedocs.io/en/latest/
