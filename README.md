# TODO
- [ ] Icons
- [ ] API [docs](https://developer.accuweather.com)
- [ ] Templates [Python template engine](https://www.makotemplates.org)
- [ ] Dockerfile
- [ ] Webhook

# Prerequirments
Install python3 virtual env 
```python
python3 -m venv venv
```

Actiavate python3 virtual env
Unix like:
```bash
source venv/bin/activate   
```

Windows like:
```bash
venv\Scripts\activate.bat
```

Install all packages:
```python
pip3 install -r requirements.txt
```

# Running
First of all u need token from @BotFather, then put it in .env file with key BOT_TOKEN, then run the following command:
```bash
make 
```

#### If make isn't installed on you machine just do:
```python 
python3 main.py
```
