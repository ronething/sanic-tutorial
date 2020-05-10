# -*- coding:utf-8 _*-  
""" 
@author: ashing 
@time: 2020/5/10 4:55 下午
@mail: axingfly@gmail.com

Less is more.
"""

from sanic import Sanic, Blueprint
from sanic.response import text


def init(app2: Sanic):
    bp = Blueprint(name='sample2', url_prefix="/v1")

    @bp.route("/feed")
    async def hello(request):
        return text('hello world')

    @bp.middleware
    async def print_on_request(request):
        print("I am a spy")

    @bp.middleware('request')
    async def halt_request(request):
        print("halt request")
        # return text('I halted the request')

    @bp.middleware('response')
    async def halt_response(request, response):
        print("halt response")
        # return text('I halted the response')

    app2.blueprint(bp)


if __name__ == '__main__':
    app = Sanic()
    init(app)
    app.run(host='127.0.0.1', port=9000, debug=True)
