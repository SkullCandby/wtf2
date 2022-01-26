import random

from pyvis import network as net
from IPython.core.display import display, HTML
from flask import Flask, request, render_template, request, redirect, url_for, jsonify, flash, make_response

app = Flask(  # Create a flask app
    __name__,
    template_folder='template',
    static_folder=''# Name of html file folder  # Name of directory for static files
)

g = net.Network(height="400px", width="50%", heading="")
g.add_node('1', color='#00ff1e', label='1')
g.save_graph("template/example.html")
HP, ENEREGY = 100, 100
i = 0
#pos = request.cookies.get(request.remote_addr).split('&*')[1]
secret_rofl = 0
nb = []
dd = {}
textix = {}
pos = '1'
textix[pos] = ''
dd[pos] = i
txt = ''
scrt_rofl = 0
dd_energy_hp = {}
global vis
vis = 1

@app.route('/game', methods=["GET"])
def my_form():
    global pos
    global scrt_rofl
    global ENEREGY
    global txt
    nb = list(g.neighbors(request.cookies.get(request.remote_addr).split('&*')[1]))
    print(nb, request.cookies.get(request.remote_addr).split('&*')[1], 'залупа нб')
    print(dd, '_-____-__-')
    print(textix, 'txt')
    if scrt_rofl < 80:
        name = request.cookies.get(request.remote_addr)
        print(request.cookies)
        resp = make_response(render_template('index.html', nb=nb, hp=HP, energy=ENEREGY, txt=textix[request.cookies.get(request.remote_addr).split('&*')[1]], vis=vis, name=name))
        try:
            print(request.cookies.get(request.remote_addr))
        except:
            print('error')
        return resp
    else:
        return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

@app.route('/game', methods=["POST"])
def my_form_post():
    global pos
    global i
    global HP
    global scrt_rofl
    global ENEREGY
    global textix
    global txt
    global vis
    print(dd, '1234241414')
    if request.form.get('game_plan') is not None:
        if vis == 0:
            vis = 1
        else:
            vis = 0
    if request.form.get('desc') is not None:
        textix[request.cookies.get(request.remote_addr).split('&*')[1]] = request.form.get('desc')
        print(request.cookies.get(request.remote_addr).split('&*')[1])
        print(textix[request.cookies.get(request.remote_addr).split('&*')[1]])
    if request.form.get('name') is not None:
        text = request.form.get('name')
        g.nodes[dd[request.cookies.get(request.remote_addr).split('&*')[1]]]['label'] = text
        g.save_graph("template/example.html")
        print(g.nodes)
    if request.form.get("sosed") is not None:
        try:
            print('request.form.get('')')
            g.nodes[dd[request.cookies.get(request.remote_addr).split('&*')[1]]]['color'] = '#00ff1e'
            g.nodes[dd[(request.form.get('sosed'))]]['color'] = '162347'
            print(g.nodes, 'KAKAHA')
            a, b = dd_energy_hp[request.cookies.get(request.remote_addr).split('&*')[1], (request.form.get('sosed'))]
            HP += a
            ENEREGY += b
            #request.cookies.get(request.remote_addr).split('&*')[0] = (request.form['sosed'])
            res = make_response(redirect('/game'))
            res.set_cookie(request.remote_addr, request.cookies.get(request.remote_addr).split('&*')[1] + '&*' + request.form['sosed'])
            print(request.cookies.get(request.remote_addr).split('&*')[1], 'dwadadaddwdwadawd')
            g.save_graph("template/example.html")
            print(textix)
            return res
        except:
            print('You bad')
            scrt_rofl +=1
            pass
    if request.form.get("add") is not None:
        #
        try:
            print('dwadadw', request.form.get('add'))
            print((g.nodes))
            print(dd)
            print(request.cookies.get(request.remote_addr).split('&*')[1],'SUKKKA')
            print(request.form.get('add'))
            g.nodes[dd[request.cookies.get(request.remote_addr).split('&*')[1]]]['color'] = '#00ff1e'
            g.nodes[dd[request.form.get('add')]]['color'] = '162347'

            a, b = dd_energy_hp[request.cookies.get(request.remote_addr).split('&*')[1], (request.form['add'])]
            HP += a
            ENEREGY += b
            res = make_response(redirect('/game'))
            name = request.cookies.get(request.remote_addr).split('&*')[1]
            res.set_cookie(request.remote_addr, name + '&*' + request.form.get("add"))
            print(request.cookies,'res')
            print(request.cookies.get(request.remote_addr))
            g.save_graph("template/example.html")
            return res
        except:
            print('You bad')
            scrt_rofl += 1
            pass
    if request.form.get("sv") is not None:

        textix[request.form['sv']] = ''
        try:
            i+=1
            dd[(request.form['sv'])] = i
            g.add_node((request.form['sv']), color='#00ff1e'
                       )
            g.add_edge(request.cookies.get(request.remote_addr).split('&*')[1], (request.form['sv']))
            if (request.cookies.get(request.remote_addr).split('&*')[1], (request.form['sv'])) not in dd_energy_hp and ((request.form['sv']), request.cookies.get(request.remote_addr).split('&*')[1]) not in dd:
                a, b = -1 * random.randrange(0, 10), -1 * random.randrange(0, 10)
                c, d = -1 * random.randrange(0, 10), -1 * random.randrange(0, 10)
                dd_energy_hp[(request.cookies.get(request.remote_addr).split('&*')[1], (request.form['sv']))] = (a, b)
                dd_energy_hp[((request.form['sv']), request.cookies.get(request.remote_addr).split('&*')[1])] = (c, d)
            g.save_graph("template/example.html")


        except:
            print('You bad')
            scrt_rofl += 1
            pass
    if request.form.get('change_name') is not None:
        print('namous')
        print(g)
        print(type(g))
        return redirect('/')

    return redirect('/game')

@app.route('/', methods=["POST","GET"])
def cookies():
    print('cock')
    if request.form.get('cock') is not None:
        print('cocken')
        res = make_response(redirect('/game'))
        print(request.form.get('cock'))

        res.set_cookie(request.remote_addr, request.form.get('cock') + '&*' + '1')
        return res
    else:
        res = make_response(redirect('/game'))
        res.set_cookie(request.remote_addr, '_' + '&*' + '1')
    if request.form.get('play') is not None:
        return redirect('/game')
    return ((((render_template('start.html')))))

if __name__ == '__main__':
    app.run(host='192.168.1.21')