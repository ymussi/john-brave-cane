#!/bin/bash

entrypoint(){
    cd /app/brave_cane/brave_cane
    # upgrade database
    echo "upgrade database ...."
    alembic upgrade head

    cd ..
    # run webserver
    echo "starting webserver ...."
    uwsgi --ini /app/brave_cane/run.ini

}

entrypoint