Pré requisitos:

Precisa ter o python instalado na sua máquina juntamente com o pip

```
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
```

# Adding Google Chrome to the repositories
```
sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
```
# Updating apt to see and install Google Chrome
```
apt-get -y update
```
```
apt-get install -yqq google-chrome-stable unzip
```
# Download the Chrome Driver
```
wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
```
# Unzip the Chrome Driver into /usr/local/bin directory
```
unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/
```
# PIP and DEPENCENCIES
```
pip install --upgrade pip
```

```
pip install -r requirements.txt
```
