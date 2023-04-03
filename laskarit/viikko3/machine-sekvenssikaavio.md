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
	F-->>M
	M->>F: fill(40)
	activate F
	deactivate F
	F-->>M
	M->>E: Engine(fueltank)
	activate E
	deactivate E
	deactivate M
	E-->>Ma
	Ma->>M: drive()
	activate M
	M->>E: start()
	activate E
	E->>F: consume(5)
	activate F
	deactivate F
	deactivate E
	F-->>M
	M->>E: is_running()
	activate E
	E->>F: fuel_contents
	activate F
	deactivate F
	F-->>E: 35
	deactivate E
	E-->>M: True
	M->>E: use_energy()
	activate E
	E->>F: consume(10)
	activate F
	deactivate F
	deactivate E
	deactivate M
	F-->>Ma
```
