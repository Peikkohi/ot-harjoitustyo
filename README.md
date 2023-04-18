# Ohjelmistotekniikan harjoitustyö
Muotojen animointityökalu (inbetweening/tweening)

## Dokumentaatio
* [Viikoittaiset muutokset](tween-animation-app/dokumentaatio/changelog.md)
* [Arkkitehtuurikaavio](tween-animation-app/dokumentaatio/arkkitehtuuri.md)

## Asennus
1. Asenna riippuvuudet: `poetry install`
2. Käynnistä sovellus: `poetry run invoke start`

## Testaus
Suorita: `poetry run invoke test`

## Testikattavuus
Testikattavuusraporttihakemisto `htmlcov` voi saada komennolla:
`poetry run invoke coverage_report`
