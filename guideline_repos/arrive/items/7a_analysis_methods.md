---
id: statistical-methods-analysis-methods
title: 7a. Statistical Methods used for each Analysis
checklist: 
    text: Provide details of the statistical methods used for each analysis, including software used.
---

## What to write

Provide details of the statistical methods used for each analysis, including software used.

## Explanation

The statistical analysis methods implemented will
reflect the goals and the design of the experiment; they should be
decided in advance before data are collected (see Item 19. Protocol
registration). Both exploratory and hypothesis-testing studies might use
descriptive statistics to summarise the data (e.g., mean and SD, or
median and range). In exploratory studies in which no specific
hypothesis was tested, reporting descriptive statistics is important for
generating new hypotheses that may be tested in subsequent experiments,
but it does not allow conclusions beyond the data. In addition to
descriptive statistics, hypothesis-testing studies might use inferential
statistics to test a specific hypothesis.

Reporting the analysis methods in detail is essential to ensure readers
and peer reviewers can assess the appropriateness of the methods
selected and judge the validity of the output. The description of the
statistical analysis should provide enough detail so that another
researcher could reanalyse the raw data using the same method and obtain
the same results. Make it clear which method was used for which
analysis.

Analysing the data using different methods and selectively reporting
those with statistically significant results constitutes p-hacking and
introduces bias in the literature
[@pbio.3000411.ref090; @pbio.3000411.ref094]. Report all analyses
performed in full. Relevant information to describe the statistical
methods include

- the outcome measures
- the independent variables of interest
- the nuisance variables taken into account in each statistical test
    (e.g., as blocking factors or covariates)
- what statistical analyses were performed and references for the
    methods used
- how missing values were handled
- adjustment for multiple comparisons
- the software package and version used, including computer code if
    available [@pbio.3000411.ref097]

The outcome measure is potentially affected by the treatments or
interventions being tested but also by other factors, such as the
properties of the biological samples (sex, litter, age, weight, etc.)
and technical considerations (cage, time of day, batch, experimenter,
etc.). To reduce the risk of bias, some of these factors can be taken
into account in the design of the experiment, for example, by using
blocking factors in the randomisation (see Item 4. Randomisation).
Factors deemed to affect the variability of the outcome measure should
also be handled in the analysis, for example, as a blocking factor
(e.g., batch of reagent or experimenter) or as a covariate (e.g.,
starting tumour size at point of randomisation).

Furthermore, to conduct the analysis appropriately, it is important to
recognise the hierarchy that can exist in an experiment. The hierarchy
can induce a clustering effect; for example, cage, litter, or animal
effects can occur when the outcomes measured for animals from the same
cage/litter, or for cells from the same animal, are more similar to each
other. This relationship has to be managed in the statistical analysis
by including cage/litter/animal effects in the model or by aggregating
the outcome measure to the cage/litter/animal level. Thus, describing
the reality of the experiment and the hierarchy of the data, along with
the measures taken in the design and the analysis to account for this
hierarchy, is crucial to assessing whether the statistical methods used
are appropriate.

For bespoke analysis---for example, regression analysis with many
terms---it is essential to describe the analysis pipeline in detail.
This could include detailing the starting model and any model
simplification steps.

When reporting descriptive statistics, explicitly state which measure of
central tendency is reported (e.g., mean or median) and which measure of
variability is reported (e.g., standard deviation, range, quartiles, or
interquartile range). Also describe any modification made to the raw
data before analysis (e.g., relative quantification of gene expression
against a housekeeping gene). For further guidance on statistical
reporting, refer to the Statistical Analyses and Methods in the
Published Literature (SAMPL) guidelines [@pbio.3000411.ref098].

## Examples

> 'Analysis of variance was performed using the GLM procedure of SAS (SAS
Inst., Cary, NC). Average pen values were used as the experimental unit
for the performance parameters. The model considered the effects of
block and dietary treatment (5 diets). Data were adjusted by the
covariant of initial body weight. Orthogonal contrasts were used to test
the effects of SDPP processing (UV vs no UV) and dietary SDPP level (3%
vs 6%). Results are presented as least squares means. The level of
significance was set at P \< 0.05' [@pbio.3000411.ref099].

> 'All risk factors of interest were investigated in a single model.
Logistic regression allows blocking factors and explicitly investigates
the effect of each independent variable controlling for the effects of
all others.... As we were interested in husbandry and environmental
effects, we blocked the analysis by important biological variables (age;
backstrain; inbreeding; sex; breeding status) to control for their
effect. (The role of these biological variables in barbering behavior,
particularly with reference to barbering as a model for the human
disorder trichotillomania, is described elsewhere ...). We also blocked
by room to control for the effect of unknown environmental variables
associated with this design variable. We tested for the effect of the
following husbandry and environmental risk factors: cage mate
relationships (i.e. siblings, non-siblings, or mixed); cage type (i.e.
plastic or steel); cage height from floor; cage horizontal position
(whether the cage was on the side or the middle of a rack); stocking
density; and the number of adults in the cage. Cage material by cage
height from floor; and cage material by cage horizontal position
interactions were examined, and then removed from the model as they were
nonsignificant. N = 1959 mice were included in this analysis'
[@pbio.3000411.ref100].
