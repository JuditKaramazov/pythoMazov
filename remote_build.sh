python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
rm -rf public
reflex init
API_URL=https://api.pythomazov.tech reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip
deactivate
