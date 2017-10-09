FROM selenium/base:3.5.3-boron

RUN sudo apt-get update && sudo apt-get install -y python python-selenium

ENV HUB_HOST hub
ENV HUB_PORT 4444


#========================
# Selenium Configuration
#========================

EXPOSE 4444
COPY web-page-screenshot.py /usr/local/bin/
CMD ["python", "/usr/local/bin/web-page-screenshot.py"]
