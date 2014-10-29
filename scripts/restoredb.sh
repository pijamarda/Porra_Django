#!/bin/bash
gunzip -c porra_proyect.gz | psql --single-transaction porra_proyect
