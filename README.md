# Ohjelmistotekniikan harjoitustyö
Muotojen animointityökalu, jolla näytön sijaintien välille saa määriteltyä liikeratoja. (inbetweening/tweening) Lisää muodolle uusia kohteita, valitse kohde, vaihda sivun vivuista kohteen sijaintia. Kun olet lisännyt useemman kohteen laita animaatio käyntiin!



## Dokumentaatio
* [Muutosten kirjanpito](tween-animation-app/dokumentaatio/changelog.md)
* [Vaatimusmäärittely](tween-animation-app/dokumentaatio/vaatimusmäärittely.md)
* [Arkkitehtuurikaavio](tween-animation-app/dokumentaatio/arkkitehtuuri.md)
* [Työaikakirjanpito](tween-animation-app/dokumentaatio/työaikakirjanpito.txt)

## Asennus
0. Lataa [julkaisu](https://github.com/Peikkohi/tween-animation-app/releases/tag/viikko5)
1. Mene alikansioon "tween-animation-app" (`cd tween-animation-app`)
2. Asenna riippuvuudet: `poetry install`
3. Käynnistä sovellus: `poetry run invoke start`

## Testaus
Suorita: `poetry run invoke test`

## Testikattavuus
Testikattavuusraporttihakemisto `htmlcov` voi saada komennolla:
`poetry run invoke coverage_report`

## Pylint
`poetry run invoke lint`
