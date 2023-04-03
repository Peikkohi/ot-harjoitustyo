```mermaid
sequenceDiagram
	Main->>Laitehallinto: HKLLaitehallinto()
	activate Laitehallinto
	deactivate Laitehallinto
	Main->>Rautatietotori: Lataajalaite()
	activate Rautatietotori
	deactivate Rautatietotori
	Main->>Ratikka6: Lukijalaite()
	activate Ratikka6
	deactivate Ratikka6
	Main->>Bussi244: Lukijalaite()
	activate Bussi244
	deactivate Bussi244
	Main->>Laitehallinto: lisaa_lataaja(Rautatietotori)
	activate Laitehallinto
	deactivate Laitehallinto
	Main->>Laitehallinto: lisaa_lukija(Ratikka6)
	activate Laitehallinto
	deactivate Laitehallinto
	Main->>Laitehallinto: lisaa_lukija(Bussi244)
	activate Laitehallinto
	deactivate Laitehallinto
	Main->>lippu_luukku: Kioski()
	activate lippu_luukku
	deactivate lippu_luukku
	Main->>lippu_luukku: osta_matkakortti("Kalle")
	activate lippu_luukku
	lippu_luukku->>kallen_kortti: Matkakortti("Kalle")
	activate kallen_kortti
	deactivate kallen_kortti
	Main->>Rautatietotori: lataa_arvoa(kallen_kortti, 3)
	activate Rautatietotori
	Rautatietotori->>kallen_kortti: kasvata_arvoa(3)
	activate kallen_kortti
	deactivate kallen_kortti
	deactivate Rautatietotori
	Main->>Ratikka6: osta_lippu(kallen_kortti, 0)
	activate rakitta6
	Ratikka6->>kallen_kortti: arvo
	activate kallen_kortti
	kallen_kortti-->>Ratikka6: 3
	deactivate kallen_kortti
	Ratikka6->>kallen_kortti: vahenna_arvoa(1.5)
	activate kallen_kortti
	deactivate kallen_kortti
	Ratikka6-->>Main: True
	deactivate Ratikka6
	Main->>Bussi244: osta_lippu(kallen_kortti, 2)
	activate Bussi244
	Bussi244->>kallen_kortti: arvo
	activate kallen_kortti
	kallen_kortti-->>Bussi244: 1.5
	deactivate kallen_kortti
	Bussi244-->>Main: False
	deactivate Bussi244
```
