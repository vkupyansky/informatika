[![Русский](https://img.shields.io/badge/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-181717?style=for-the-badge)](README.ru.md)

# Informatics

An archive of HTML and CSS lab assignments from 2018. Static pages demonstrate markup and element styling.

## Features

- Text formatting, links, and images.
- Tables, frames, and supporting assignment pages.
- View in a browser without installing dependencies.

## Installation and startup

Open `index.html` in a browser, or start a local server from the project root:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

The site will be available at [localhost:8000](http://localhost:8000). No build, database, or external services are required.

## Usage

Choose a lab assignment on the home page. The "Назад" (Back) links return to the list; pages in `lab/` contain assignments and examples. Images in `images/` are resources used by the assignment pages.

## Checks

```bash
python3 -W error scripts/check.py
node --check js/javascript.js
```

These commands check local links and resources, including CSS and frame pages, as well as JavaScript syntax. They do not make external requests.

## Limitations

The third lab assignment and the second and third tasks of the fifth assignment are incomplete. Legacy HTML elements and the original educational layouts are preserved; a modern responsive version is not being developed. The project uses system fonts; font files without a redistribution license are not included.
