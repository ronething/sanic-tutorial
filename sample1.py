# coding=utf-8

from sanic import Sanic


def init(app: Sanic):
    @app.websocket('/feed')
    async def feed(request, ws):
        while True:
            data = await ws.recv()
            # print('Received：', data)
            # print('Sending：' + data)
            await ws.send("recv:" + data)


if __name__ == '__main__':
    app = Sanic()
    init(app)
    app.run(host='127.0.0.1', port=9000)
