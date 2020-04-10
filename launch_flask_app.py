from subprocess import run


def load_jupyter_server_extension(nbapp):
    run(["python", "./flask-app/main.py"])
