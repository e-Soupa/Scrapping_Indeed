Setup Plugins & Activate Venv
1. Create Project Folder & Enter It on VSCode
`mkdir indeed_scraper cd indeed_scraper`

2. Create & Activate Python Virtual Environment
- Create: `python3 -m venv venv`
- Activate: `source venv/bin/activate` (do it each time when reboot)

3. Install Required Python Packages
    - `pip install selenium
    - `pip install undetected-chromedriver` 
    - `pip install setuptools  # required for Python 3.12+`

3bis: Only if setuptools does not work (Optional)
- `sudo apt install python3.11 python3.11-venv`
- `python3.11 -m venv venv`
- `source venv/bin/activate`
- `pip install undetected-chromedriver`

4. Install Chromium Browser (if not already installed)
- `sudo apt install chromium`

5. (Optional) Install Chromium Driver (not needed for undetected-chromedriver)
`sudo apt install chromium-driver`
