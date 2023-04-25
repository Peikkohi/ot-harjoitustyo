# Ohjelman rakenteen luokkakaavio

```mermaid
classDiagram
Setting <|-- FrameSetting
Setting <|-- TweenSetting
Setting "1..*" -- "1" Animator
Animator "1" -- "1" Manager
```

# Animaation käyntiinlaitto sekvenssikaavio

```mermaid
sequenceDiagram
	participant Mainloop
	participant Animate
	participant Frame
	participant Position
	participant Schedule
	participant Play

	Mainloop->>Play: animator.play()
	activate Play
	Play->>Animate: animator.animate()
	activate Animate
	deactivate Animate
	Mainloop->>Animate: animator.animate()
	activate Animate
	deactivate Animate
´´´
