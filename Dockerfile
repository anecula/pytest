FROM selenium/base:3.5.3-boron


#========================
# Selenium Configuration
#========================

EXPOSE 4444
COPY web-page-screenshot.py  /usr/local/bin/
