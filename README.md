# Ohjelmistotekniikan harjoitustyö
Muotojen animointityökalu, jolla ruudun sijaintien välille saa määriteltyä liikeratoja. (inbetweening/tweening)

## Dokumentaatio
* [Muutosten kirjanpito](tween-animation-app/dokumentaatio/changelog.md)
* [Vaatimusmäärittely](tween-animation-app/dokumentaatio/vaatimusmäärittely.md)
* [Arkkitehtuurikaavio](tween-animation-app/dokumentaatio/arkkitehtuuri.md)
* [Työaikakirjanpito](tween-animaiton-app/dokumentaatio/työaikakirjapito.txt)

## Asennus
1. Asenna riippuvuudet: `poetry install`
2. Käynnistä sovellus: `poetry run invoke start`

## Testaus
Suorita: `poetry run invoke test`

## Testikattavuus
Testikattavuusraporttihakemisto `htmlcov` voi saada komennolla:
`poetry run invoke coverage_report`

## Pylint
`poetry run invoke lint`
