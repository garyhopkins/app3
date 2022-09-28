#!/bin/bash
pwd="$(pwd)"
docker run -it -p 8080:8080 -v "$pwd"/code:/app app3backend /bin/bash
