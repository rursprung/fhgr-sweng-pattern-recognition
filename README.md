# FHGR B.Sc. MR: SWEng Project (Image Recognition)

[![CI](https://github.com/rursprung/fhgr-sweng-pattern-recognition/actions/workflows/ci.yaml/badge.svg)](https://github.com/rursprung/fhgr-sweng-pattern-recognition/actions/workflows/ci.yaml)
![License: GPLv3](https://img.shields.io/github/license/rursprung/fhgr-sweng-pattern-recognition)

This is a mini-project for the software engineering course of the [FHGR B.Sc. Mobile Robotics](https://fhgr.ch/mr),
implemented by [Dominic Eicher](https://github.com/Nic822) and [Ralph Ursprung](https://github.com/rursprung).

This project reads an image and tries to recognise different patterns in it, including their colour. The result is
logged (both on the console and in a CSV file) as well as visualised in a GUI.

## Architecture Overview

```mermaid
graph LR
    IL -->|Image|PR
    IL -->|Image|Viz
    PR -->|"List of Patterns
    (Location, Shape, Colour)"|Viz
    Viz -->|"image with markup"|Screen
    
    PR -->|"List of Patterns
    (Location, Shape, Colour)"|ConsoleLogger
    ConsoleLogger-->|"Text
    (Log Entries)"|Screen
    PR -->|"List of Patterns
    (Location, Shape, Colour)"|CSVLogger
    CSVLogger -->|"CSV
    (Log Entries)"|CSVFile
    
    IL[Image Loader]
    Viz[Visualizer]
    PR[Pattern Recognition]
    ConsoleLogger[Console Logger]
    CSVLogger[CSV Logger]
    Screen[[Screen]]
    CSVFile[[CSV File]]
```

## License

As this is purely an educational project there's no need for others to include it in their commercial works.
Accordingly, this is licensed under the **GNU General Public License v3.0 or later** (SPDX: `GPL-3.0-or-later`).
See [LICENSE](LICENSE) for the full license text.
