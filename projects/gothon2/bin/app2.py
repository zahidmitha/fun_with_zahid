import web

urls = (
  '/elrold', 'elrond'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class elrond(object):
    def GET(self):
        greeting = "Money"
        return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()


#why can't I change index in 2 places?
