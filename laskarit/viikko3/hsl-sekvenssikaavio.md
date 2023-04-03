```mermaid
sequenceDiagram
	main->>laitehallinto: HKLLaitehallinto
	activate laitehallinto
	deactivate laitehallinto
	main->>rautatietori: Lataajalaite()
	activate rautatietori
	deactivate rautatietori
	main->>ratikka6: Lukijalaite()
	activate ratikka6
	deactivate ratikka6
	main->>bussi244: Lukijalaite()
	activate bussi244
	deactivate bussi244
	main->>laitehallinto: lisaa_lataaja(rautatietori)
	activate laitehallinto
	deactivate laitehallinto
	main->>laitehallinto: lisaa_lukija(ratikka6)
	activate laitehallinto
	deactivate laitehallinto
	main->>laitehallinto: lisaa_lukija(bussi244)
	activate laitehallinto
	deactivate laitehallinto
	main->>lippu_luukku: Kioski()
	activate lippu_luukku
	deactivate lippu_luukku
	main->>lippu_luukku: osta_matkakortti("Kalle")
	activate lippu_luukku
	lippu_luukku->>kallen_kortti: Matkakortti("Kalle")
	activate kallen_kortti
	deactivate kallen_kortti
	main->>rautatietori: lataa_arvoa(kallen_kortti, 3)
	activate rautatietori
	rautatietori->>kallen_kortti: kasvata_arvoa(3)
	activate kallen_kortti
	deactivate kallen_kortti
	deactivate rautatietori
	main->>ratikka6: osta_lippu(kallen_kortti, 0)
	activate rakitta6
	ratikka6->>kallen_kortti: arvo
	activate kallen_kortti
	kallen_kortti-->>ratikka6: 3
	deactivate kallen_kortti
	ratikka6->>kallen_kortti: vahenna_arvoa(1.5)
	activate kallen_kortti
	deactivate kallen_kortti
	ratikka6-->>main: True
	deactivate ratikka6
	main->>bussi244: osta_lippu(kallen_kortti, 2)
	activate bussi244
	bussi244->>kallen_kortti: arvo
	activate kallen_kortti
	kallen_kortti-->>bussi244: 1.5
	deactivate kallen_kortti
	bussi244-->>main: False
	deactivate bussi244
```
