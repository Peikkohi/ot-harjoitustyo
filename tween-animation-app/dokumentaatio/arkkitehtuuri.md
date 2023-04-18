```mermaid
classDiagram
Setting <|-- FrameSetting
Setting <|-- TweenSetting
Setting "1..*" -- "1" Animator
Animator "1" -- "1" Manager
```
