import pdfkit
import filters

from flask import Flask, render_template, request, abort, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Add the Jinja filters.
app.jinja_env.filters['title'] = filters.title
app.jinja_env.filters['is_dict'] = filters.is_dict
app.jinja_env.filters['is_list'] = filters.is_list


@app.route('/', methods=['POST'])
def generate_pdf():
    json_data = request.get_json()

    if not json_data:
        abort(400)

    html_text = render_template('systematicReviewProtocol.html', data=json_data)
    pdf = pdfkit.from_string(html_text, False)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=%s.pdf' % 'yourfilename'
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route('/', methods=['GET'])
def test_render():
    json_data = {
        'title': 'This is my test title',
        'typeOfReview': 'systematic review',
        'authorsContracts': 'Yes',
        'abstract': 'Yes',
        'background': 'Yes',
        'stakeholderAgreement': 'Yes',
        'objectivesOfTheReview': {
            'objectives': 'Not applicable',
            'definitionsOfTheQuestionComponent': 'Break down and summarise question key elements e.g. population, intervention(s)/exposure(s), comparator(s), and outcome(s).'
        },
        'methods': 'My own methods',
        'searches': {
            'searchStrategy': 'Yes',
            'searchString': 'hello world thanks for everything',
            'languagesBibliographicDatabases': [
                'lang db 01',
                'lang db 02'
            ],
            'languagesGreyDatabases': [
                'grey db 01',
                'grey db 02'
            ],
            'webSearchEngines': [
                'http://www.google.com/',
                'http://www.bing.com/',
                'http://www.yahoo.com/'
            ],
            'organisationalWebsites': [
                'http://www.digitalsolutionfoundry.co.za/',
                'http://www.hello.com/'
            ],
            'estimatingTheComprehensivenessOfTheSearch': 'Yes',
            'searchUpdate': 'No'
        },
        'articleScreeningAndStudyInclusionCriteria': {
            'screeningStrategy': 'Yes',
            'consistencyChecking': 'Yes',
            'inclusionCriteria': 'Yes',
            'reasonsForExclusion': 'Yes'
        },
        'criticalAppraisal': {
            'criticalAppraisalUsedInSynthesis': 'Yes',
            'consistencyChecking': 'Yes'
        },
        'dataExtraction': {
            'metaDataExtractionAndCodingStrategy': 'Yes',
            'dataExtractionStrategy': 'Yes',
            'approachesToMissingData': 'Yes',
            'consistencyChecking': 'Yes'
        },
        'potentialEffectModifiersForHeterogeneity': 'Yes',
        'dataSynthesisAndPresentation': {
            'typeOfSynthesis': 'narrative only',
            'narrativeSynthesisStrategy': 'Yes',
            'quantitativeSynthesisStrategy': 'Yes',
            'qualitativeSynthesisStrategy': 'Yes',
            'otherSynthesisStrategy': 'Yes',
            'assessmentOfRiskOfPublicationBias': 'Yes',
            'knowledgeGapAndClusterIdentificationStrategy': 'Yes',
            'demonstratingProceduralIndependence': 'Yes'
        },
        'declarations': {
            'competingInterests': 'Yes'
        }
    }

    return render_template('systematicReviewProtocol.html', data=json_data)
