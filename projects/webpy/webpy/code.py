import web

urls = (
	'/', 'index',
	)

render = web.template.render('templates/')

db = web.database(dbn='sqlite', db='testdb')

class index:
    def GET(self):
        todos = db.select('todo')
        return render.index(todos)


		# return render.index(name)

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()


