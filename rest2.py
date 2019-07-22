from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
import json
from auth_user import *
from retrieve_stocks import *

def make_app():
  urls = ([
    ("/user/login", userLogin),
    ("/user/getStocks", userGetStocks)
  ])
  return Application(urls, debug=True)

class userLogin(RequestHandler):
  def post(self):
    data = json.loads(self.request.body.decode("utf-8"))
    email = data["email"]
    password = data["pwd"]
    response = authenticateUser(email, password)
    print("Email: " + email)
    print("Password: " + password)
    print("Response: " + str(response))
    responseData = {
      "responseCode": response
    }
    print(responseData)
    self.write(json.dumps(responseData))


class userGetStocks(RequestHandler):
  def post(self):
    response = getStockData()
    response = json.dumps(response)
    self.write(response)


if __name__ == '__main__':
  app = make_app()
  app.listen(8888)
  IOLoop.instance().start()
