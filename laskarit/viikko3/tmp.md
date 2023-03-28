```mermaid
classDiagram
Monopoli "1" -- "2" Noppa
Monopoli "1" -- "1" Pelilauta
Monopoli "1" -- "2..8" Pelaaja
Pelilauta "1" -- "40" Ruutu
Ruutu "1" -- "1" Ruutu
Pelaaja "1" -- "1" Pelinappula
Pelinappula "1" -- "1" Ruutu
```
