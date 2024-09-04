#!/bin/zsh

echo "Borrando la caché de mutmut..."
rm .mutmut-cache

echo "Ejecutando pruebas de mutación con mutmut..."
pipenv run mutmut run

echo "Generando reporte HTML de mutmut..."
pipenv run mutmut html

# Cambia el nombre del archivo si mutmut genera algo distinto o si tienes una ubicación específica para el reporte
HTML_REPORT="html/index.html"

echo "Abriendo el reporte HTML..."
# En macOS
open $HTML_REPORT

# En Linux (descomenta la línea correspondiente a tu entorno)
# xdg-open $HTML_REPORT
# En Windows (Git Bash o WSL)
# start $HTML_REPORT
