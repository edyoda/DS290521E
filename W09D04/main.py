from sanic import Sanic
from sanic.response import json

app = Sanic("My Hello, world app")

@app.route('/apple',methods=['POST'])
async def test(request):
	payload = request.json
	print(type(payload.keys()))
	return json({'hello': 'world'})

@app.route('/mango')
async def test2(request):
	return json({'mango':'tasty'})

if __name__ == '__main__':
    app.run()