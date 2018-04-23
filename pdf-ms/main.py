import pdfkit

from flask import Flask, render_template, request, abort, make_response

app = Flask(__name__)
options = {
    'page-size': 'A4',
    'dpi': 400,
    'encoding': 'utf-8',
}


@app.route('/', methods=['POST'])
def generate_pdf():
    json_data = request.get_json()

    if not json_data:
        abort(400)

    html_text = render_template('pdf.html', data=json_data)
    pdf = pdfkit.from_string(html_text, False)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=%s.pdf' % 'yourfilename'
    return response

@app.route('/', methods=['GET'])
def test_render():
    json_data = {
        'message': 'test the world'
    }

    return render_template('pdf.html', data=json_data)
