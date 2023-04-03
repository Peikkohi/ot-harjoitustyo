```mermaid
sequenceDiagram
	participant Ma as Main
	participant M as Machine
	participant E as Engine
	participant F as FuelTank

	Ma->>M: Machine()
	activate M
	M->>F: FuelTank()
	activate F
	deactivate F
	M->>F: fill(40)
	activate F
	deactivate F
	M->>E: Engine(fueltank)
	activate E
	deactivate E
	deactivate M
	Ma->>M: drive()
	activate M
	M->>E: start()
	activate E
	E->>F: consume(5)
	activate F
	deactivate F
	deactivate E
	M->>E: is_running()
	activate E
	E->>F: fuel_contents
	activate F
	F-->>E: 35
	deactivate F
	E-->>M: True
	deactivate E
	M->>E: use_energy()
	activate E
	E->>F: consume(10)
	activate F
	deactivate F
	deactivate E
	deactivate M
```
