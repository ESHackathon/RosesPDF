import pdfkit

from flask import Flask, render_template, request, abort, make_response
from filters import title

app = Flask(__name__)

# Add the Jinja filters.
app.jinja_env.filters['title'] = title


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
    return response


@app.route('/', methods=['GET'])
def test_render():
    json_data = {
        'title': '',
        'typeOfReview': '',
        'authorsContracts': '',
        'abstract': '',
        'background': '',
        'stakeholderAgreement': '',
        'objectivesOfTheReview': {
            'objectives': '',
            'definitionsOfTheQuestionComponent': ''
        },
        'methods': '',
        'searches': {
            'searchStrategy': '',
            'searchString': '',
            'languagesBibliographicDatabases': [],
            'languagesGreyDatabases': [],
            'webSearchEngines': [],
            'organisationalWebsites': [],
            'estimatingTheComprehensivenessOfTheSearch': '',
            'searchUpdate': ''
        },
        'articleScreeningAndStudyInclusionCriteria': {
            'screeningStrategy': '',
            'consistencyChecking': '',
            'inclusionCriteria' : '',
            'reasonsForExclusion': ''
        },
        'criticalAppraisal': {
            'criticalAppraisalUsedInSynthesis': '',
            'consistencyChecking': ''
        },
        'dataExtraction': {
            'metaDataExtractionAndCodingStrategy': '',
            'dataExtractionStrategy': '',
            'approachesToMissingData': '',
            'consistencyChecking': ''
        },
        'potentialEffectModifiersForHeterogeneityy': '',
        'dataSynthesisANdPresentationTypeOfSynthesis': {
            'narrativeSynthesisStrategy': '',
            'quantitativeSynthesisStrategy': '',
            'qualitativeSynthesisStrategy': '',
            'otherSynthesisStrategy': '',
            'assessmentOfRiskOfPublicationBias': '',
            'knowledgeGapAndClusterIdentificationStrategy': '',
            'demonstratingProceduralIndependence': '',
        },
        'declarations': {
            'competingInterests': ''
        }
    }

    return render_template('systematicReviewProtocol.html', data=json_data)
