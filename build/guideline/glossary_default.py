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
CASE_CONTROL_STUDIES = """
In case-control studies, investigators compare exposures between people with a particular disease outcome (cases) and people without that outcome (controls). Investigators aim to collect cases and controls that are representative of an underlying cohort or a cross-section of a population. That population can be defined geographically, but also more loosely as the catchment area of health care facilities. The case sample may be 100% or a large fraction of available cases, while the control sample usually is only a small fraction of the people who do not have the pertinent outcome. Controls represent the cohort or population of people from which the cases arose. Investigators calculate the ratio of the odds of exposures to putative causes of the disease among cases and controls. Depending on the sampling strategy for cases and controls and the nature of the population studied, the odds ratio obtained in a case-control study is interpreted as the risk ratio, rate ratio or (prevalence) odds ratio.

A classic case-control study is [Smoking and Carcinoma of the Lung](https://pmc.ncbi.nlm.nih.gov/articles/PMC2038856/) by Richard Doll and A Bradford Hill which suggested a link between smoking and lung cancer."""
COHORT_STUDIES = """
In cohort studies, In a cohort study, one or more groups are closely monitored and outcomes measured over time. Researchers collect information about people and their exposures to factors which might affect their health at baseline, let time pass, and then measure the occurrence of pre-specified outcomes. Researchers commonly make contrasts between individuals who are exposed and not exposed to these factors, or among groups of individuals with different levels of exposure. Investigators may assess several different outcomes, and examine exposure and outcome variables at multiple points during follow-up. Some cohorts are closed - for example birth cohorts. They enrol a defined number of participants at the beginning of the study and follow them from that time forward, often at set intervals up to a fixed end date. Some are open cohorts - for example inhabitants of a town. This means people enter and leave the population at different points in time . Open cohorts change due to deaths, births, and migration, but the composition of the population with regard to variables such as age and gender may remain approximately constant, especially over a short period of time. In a closed cohort cumulative incidences (risks) and incidence rates can be estimated; when exposed and unexposed groups are compared, this leads to risk ratio or rate ratio estimates. Open cohorts estimate incidence rates and rate ratios.

A classic cohort study is [The British Doctors' Cohort](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2362092/#bib9) by Richard Doll and A Bradford Hill which confirmed the link between smoking and lung cancer."""


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
        'text': 'Ipsum Lorem',
        'id': 'case_control_studies',
        'pattern': 'case-control studies',
    },
    'cross-sectional_studies': {
        'title': 'Cross-sectional studies',
        'text': 'Ipsum Lorem',
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
        'text': 'Ipsum Lorem',
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
        'text': 'Ipsum Lorem',
        'id': 'diagnostic_test_accuracy_studies',
        'pattern': 'diagnostic test accuracy studies',
    },
    'prediction_models': {
        'title': 'Prediction Models',
        'text': 'Ipsum Lorem',
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