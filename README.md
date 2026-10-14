# WEB SCRAPING

This repository contains a collection of Python scripts for web scraping scenarios.

1. [The first scenario](./downloader.py) involves downloading various files whose links are contained in the href attribute of an <a> tag:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div>
        <p>
            <a href="file1.pdf">File 1</a>
            <a href="file2.pdf"> File2 </a>
        </p>
    </div>
</body>
</html>

```