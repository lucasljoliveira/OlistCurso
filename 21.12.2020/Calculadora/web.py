from flask import Flask, render_template
from calculadora import soma, subtracao, divisao, multiplicacao


if __name__ == '__main__':
    app = Flask(__name__)

    @app.route('/')
    def index():
        h1 = '<h1> Calculadora Olist </h1>'
        ol = '''
                <ul>
                    <li><a href = "/soma">Somar</a></li>
                    <li><a href = "/subtracao">Subtração</a></li>
                    <li><a href = "/divisao">Divisão</a></li>
                    <li><a href = "/multiplicacao">Multiplicação</a></li>
                </ul>
            '''
        return f'{h1} {ol}'

    @app.route('/soma')
    def calc_soma():
        n1 = 3.0
        n2 = 5.0
        resultado = soma(n1, n2)
        h1 = '<h1> Calculadora Olist </h1>'
        h3 = f'<h3>A soma de {n1} + {n2}: {resultado}</h3>'
        voltar = '<a href="/">Voltar!</a>'
        return f'{h1} {h3} <br /> {voltar}'
        #return render_template('soma.html', v1=n1, v2=n2, r=resultado)
        # no soma.html utilizar chaves duplas {{v1}} {{v2}} {{r}}

    @app.route('/subtracao')
    def calc_subtracao():
        n1 = 3.0
        n2 = 5.0
        resultado = subtracao(n1, n2)
        h1 = '<h1> Calculadora Olist </h1>'
        h3 = f'<h3>A subtracao de {n1} - {n2}: {resultado}</h3>'
        voltar = '<a href="/">Voltar!</a>'
        return f'{h1} {h3} <br /> {voltar}'

    @app.route('/divisao')
    def calc_divisao():
        n1 = 3.0
        n2 = 5.0
        resultado = divisao(n1, n2)
        h1 = '<h1> Calculadora Olist </h1>'
        h3 = f'<h3>A divisão de {n1} / {n2}: {resultado}</h3>'
        voltar = '<a href="/">Voltar!</a>'
        return f'{h1} {h3} <br /> {voltar}'

    @app.route('/multiplicacao')
    def calc_multiplicacao():
        n1 = 4.0
        n2 = 5.0
        resultado = multiplicacao(n1, n2)
        h1 = '<h1> Calculadora Olist </h1>'
        h3 = f'<h3>A multiplicação de {n1} * {n2}: {resultado}</h3>'
        voltar = '<a href="/">Voltar!</a>'
        return f'{h1} {h3} <br /> {voltar}'

    app.run(debug = True)