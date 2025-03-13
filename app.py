from flask import Flask, redirect, jsonify

app = Flask(__name__)

def write(msg = "Nothing"):
  f = open("list.txt", "a")
  f.write(msg + "\n")
  f.close()

#tttttttttt

def read():
  f = open("list.txt", "r")
  data = []
  for line in f:
    data.append(line.strip())
  f.close()
  return data


def delete():
  f = open("list.txt", "w")
  f.write("")
  f.close()


@app.route('/')
def index():
  return redirect('/list/')


@app.route('/list/')
def getList():
  result = read()
  return jsonify(result)


@app.route('/list/add/<item>')
def addItem(item):
  write(item)
  return jsonify(200)


@app.route('/list/delete')
def deleteList():
  delete()
  return jsonify(200)


if __name__ == '__main__':
  app.run()