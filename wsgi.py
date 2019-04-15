from grow_easily_server.app import create_app


app = create_app()
app.run(port=8080)
