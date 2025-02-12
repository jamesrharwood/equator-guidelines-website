from markdown import Markdown

RG_BODY = """
<p>Your research will be used by people from different disciplines and backgrounds for decades to come. Reporting guidelines list the information you should describe so that <span class="defined" data-bs-toggle="offcanvas" href="#glossaryItemresearch_consumers" aria-controls="offcanvasExample" role="button"><em>everyone</em></span> can understand, replicate, and synthesise your work.</p>
<p>Reporting guidelines do not prescribe how research should be designed or conducted. Rather, they help authors transparently describe what they did, why they did it, and what they found.</p>
<p>Reporting guidelines make writing research easier, and transparent research leads to better patient outcomes.</p>
<div class="feature-callout">
<p><img src="/assets/images/bubblecons/bubblecons_files_folders_page-90-icon-line-colour.svg" class="feature-icon img-fluid"></p>
<p><strong>Easier writing</strong></p>
<p>Following guidance makes writing easier and quicker.</p>
<div class="learn-more">
<p><a href="">Learn more »</a></p>
</div>
</div>
<div class="feature-callout">
<p><img src="/assets/images/bubblecons/bubblecons_files_folders_favourite-74-icon-line-colour.svg" class="feature-icon img-fluid"></p>
<p><strong>Smoother publishing</strong></p>
<p>Many journals require completed reporting checklists at submission.</p>
<div class="learn-more">
<p><a href="">Learn more »</a></p>
</div>
</div>
<div class="feature-callout">
<p><img src="/assets/images/bubblecons/bubblecons_awards_3_awrad-6-icon-line-colour.svg" class="feature-icon img-fluid"></p>
<p><strong>Maximum impact</strong></p>
<p>From nobel prizes to null results, articles have more impact when everyone can use them.</p>
<div class="learn-more">
<p><a href="">Learn more »</a></p>
</div>
</div>
"""

EVERYONE = """
You work will be read by different people, for different reasons, around the world, and for decades to come. Reporting guidelines help you consider all of your potential audiences. For example, your research may be read by researchers from different fields, by clinicians, patients, evidence synthesisers, peer reviewers, or editors. Your readers will need information to understand, to replicate, apply, appraise, synthesise, and use your work. """
CASE_CONTROL_STUDIES = """A study that compares two groups of people: those with the disease or condition under study (cases) and a very similar group of people who do not have the disease or condition (controls). Researchers study the medical and lifestyle histories of the people in each group to learn what factors may be associated with the disease or condition. For example, one group may have been exposed to a particular substance that the other was not. Also called retrospective study. ([source](https://www.cancer.gov/publications/dictionaries/cancer-terms/def/case-control-study))."""

COHORT_STUDIES = """A research study that compares a particular outcome (such as lung cancer) in groups of individuals who are alike in many ways but differ by a certain characteristic (for example, female nurses who smoke compared with those who do not smoke). ([source](https://www.cancer.gov/publications/dictionaries/cancer-terms/def/cohort-study)).
"""

CROSS_SECTIONAL = """A type of research study in which a group of people is observed, or certain information is collected, at a single point in time or over a short period of time. For example, a survey may be done to collect information about the total number of people in a group who have or had a certain disease (such as cancer) or risk factor (such as smoking or obesity). In this example, the survey may be able to provide some information about whether there is an association between the smoking (risk factor) and the cancer (disease) but does not prove that they are linked. Results from a cross-sectional study may be used to plan other research studies. A cross-sectional study is a type of observational (epidemiologic) study. ([source](https://www.cancer.gov/publications/dictionaries/cancer-terms/def/cross-sectional-study))"""

CASE_REPORT = """
Case reports are detailed reports of the diagnosis, treatment, and follow-up of an individual patient. Case reports also contain some demographic information about the patient (for example, age, gender, ethnic origin) ([source](https://www.cancer.gov/publications/dictionaries/cancer-terms/def/case-report)).

Case series are group or series of case reports involving patients who were given similar treatment. Reports of case series usually contain detailed information about the individual patients. This includes demographic information (for example, age, gender, ethnic origin) and information on diagnosis, treatment, response to treatment, and follow-up after treatment ([source](https://www.cancer.gov/publications/dictionaries/cancer-terms/def/case-series)).
"""

TRIPOD = """Prediction models are developed to aid health care providers in estimating the probability or risk that a specific disease or condition is present (diagnostic models) or that a specific event will occur in the future (prognostic models), to inform their decision making."""

STARD = """Diagnostic accuracy studies focus on estimating the ability of the test(s) to correctly identify subjects with a predefined target condition, or the condition of interest (sensitivity) as well as to clearly identify those without the condition (specificity)."""

QUALITATIVE_RESEARCH = """Research that aims to gather and analyse non-numerical (descriptive) data in order to gain an understanding of individuals' social reality, including understanding their attitudes, beliefs, and motivation. This type of research typically involves in-depth interviews, focus groups, or field observations in order to collect data that is rich in detail and context. Qualitative research is often used to explore complex phenomena or to gain insight into people's experiences and perspectives on a particular topic. It is particularly useful when researchers want to understand the meaning that people attach to their experiences or when they want to uncover the underlying reasons for people's behavior. Qualitative methods include ethnography, grounded theory, discourse analysis, and interpretative phenomenological analysis. ([source](https://en.wikipedia.org/wiki/Qualitative_research))"""

glossary_default = {
    'reporting_guidelines': {
        'title': 'Reporting Guidelines are recommendations to help describe your work clearly', 
        'text': RG_BODY, 
        'id': 'reporting_guideline',
        'pattern': 'reporting guidelines?'
    },
    'research_consumers': {
        'title': 'Who reads research?', 
        'text': EVERYONE, 
        'id': 'research_consumers',
        'pattern': 'by everyone'
    },
    'cohort_studies': {
        'title': 'Cohort studies',
        'text': COHORT_STUDIES,
        'id': 'cohort_studies',
        'pattern': 'cohort studies',
    },
    'case_control_studies': {
        'title': 'Case-control studies',
        'text': CASE_CONTROL_STUDIES,
        'id': 'case_control_studies',
        'pattern': 'case-control studies',
    },
    'cross-sectional_studies': {
        'title': 'Cross-sectional studies',
        'text': CROSS_SECTIONAL,
        'id': 'cross_sectional_studies',
        'pattern': 'cross-sectional studies',
    },
    'systematic_reviews': {
        'title': 'Systematic reviews',
        'text': 'Ipsum Lorem',
        'id': 'systematic_reviews',
        'pattern': 'systematic reviews',
    },
    'systematic_review_protocols': {
        'title': 'Systematic review protocols',
        'text': 'Ipsum Lorem',
        'id': 'systematic_review_protocols',
        'pattern': 'systematic review protocols',
    },
    'meta_analyses': {
        'title': 'Meta analyses of Observational Studies',
        'text': 'Ipsum Lorem',
        'id': 'meta_analyses',
        'pattern': 'meta analyses of observational studies',
    },
    'randomised_trials': {
        'title': 'Randomised Trials',
        'text': 'Ipsum Lorem',
        'id': 'randomised_trials',
        'pattern': 'randomised trials',
    },
    'randomised_trial_protocols': {
        'title': 'Randomised Trial Protocols',
        'text': 'Ipsum Lorem',
        'id': 'randomised_trial_protocols',
        'pattern': 'randomised trial protocols',
    },
    'qualitative_research': {
        'title': 'Qualitative research',
        'text': QUALITATIVE_RESEARCH,
        'id': 'qualitative_research',
        'pattern': 'qualitative research',
    },
    'case_reports': {
        'title': 'Case Reports',
        'text': 'Ipsum Lorem',
        'id': 'case_reports',
        'pattern': 'case reports',
    },
    'diagnostic_test_accuracy_studies': {
        'title': 'Diagnostic Test Accuracy Studies',
        'text': STARD,
        'id': 'diagnostic_test_accuracy_studies',
        'pattern': 'diagnostic test accuracy studies',
    },
    'prediction_models': {
        'title': 'Prediction Models',
        'text':  TRIPOD,
        'id': 'prediction_models',
        'pattern': 'prediction models',
    },
    'animal_research': {
        'title': 'Animal Research',
        'text': 'Ipsum Lorem',
        'id': 'animal_research',
        'pattern': 'animal research',
    },
    'qi': {
        'title': 'Quality Improvement in Healthcare',
        'text': 'Ipsum Lorem',
        'id': 'qi',
        'pattern': 'quality improvement studies',
    },
    'economic_evaluations': {
        'title': 'Economic Evaluations in Healthcare',
        'text': 'Ipsum Lorem',
        'id': 'economic_evaluations',
        'pattern': 'economic evaluations',
    },
}

md = Markdown()
for k, v in glossary_default.items():
    v.update({'text': md.convert(v['text'])})