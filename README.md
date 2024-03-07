## Luxonis Scraping Task

### Overview

As a next step, we have prepared a specific testing task for our hiring purposes that is relevant to the role you applied for:
Use scrapy framework to scrape the first 500 items (title, image url) from sreality.cz (flats, sell) and save it in the Postgresql database. Implement a simple HTTP server in python and show these 500 items on a simple page (title and image) and put everything to single docker compose command so that I can just run "docker-compose up" in the Github repository and see the scraped ads on http://127.0.0.1:8080 page.

### How to run this

```bash
   git clone https://github.com/Timothy102/luxonis.git

```bash
   docker-compose up --build

Note: Port 8080 on my device is saved by the Docker Daemon, hence I diverted traffic through port 8000. Nevertheless, I've included code that would have used NGINX as a reverse proxy(nginx.conf). Commented it out on docker-compose.yml
