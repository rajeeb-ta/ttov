# %cd /content/ttovai
from pyngrok import ngrok

public_url = ngrok.connect(8188)
print(public_url)