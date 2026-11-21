# Test scripts

Python + Playwright. Install: `pip install playwright` then `playwright install chromium`.
Run from this folder: `python3 flow2.py` (26 flow checks) and `python3 audit.py` (link and click audit).
They open `../site/index.html` by default; set `SITE_URL` to test a deployed URL.
The video pause/play check needs a browser that plays H.264: use `BROWSER_CHANNEL=chrome`.
