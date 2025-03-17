---
id: sample-size-justification
title: 2b. Sample Size Justification
checklist: 
    text: Explain how the sample size was decided. Provide details of any a priori sample size calculation, if done.
---

## What to write

Explain how the sample size was decided.

Provide details of any a priori sample size calculation, if done.

## Explanation

For any type of experiment, it is crucial to explain
how the sample size was determined. For hypothesis-testing experiments,
in which inferential statistics are used to estimate the size of the
effect and to determine the weight of evidence against the null
hypothesis, the sample size needs to be justified to ensure experiments
are of an optimal size to test the research question
[@pbio.3000411.ref033; @pbio.3000411.ref034] (see Item 13.
Objectives). Sample sizes that are too small (i.e., underpowered
studies) produce inconclusive results, whereas sample sizes that are too
large (i.e., overpowered studies) raise ethical issues over unnecessary
use of animals and may produce trivial findings that are statistically
significant but not biologically relevant [@pbio.3000411.ref035].
Low power has three effects: first, within the experiment, real effects
are more likely to be missed; second, when an effect is detected, this
will often be an overestimation of the true effect size
[@pbio.3000411.ref024]; and finally, when low power is combined with
publication bias, there is an increase in the false positive rate in the
published literature [@pbio.3000411.ref036]. Consequently,
low-powered studies contribute to the poor internal validity of research
and risk wasting animals used in inconclusive research
[@pbio.3000411.ref037].

Study design can influence the statistical power of an experiment, and
the power calculation used needs to be appropriate for the design
implemented. Statistical programmes to help perform a priori sample size
calculations exist for a variety of experimental designs and statistical
analyses, both freeware (web-based applets and functions in R) and
commercial software [@pbio.3000411.ref038]--[@pbio.3000411.ref040].
Choosing the appropriate calculator or algorithm to use depends on the
type of outcome measures and independent variables, and the number of
groups. Consultation with a statistician is recommended, especially when
the experimental design is complex or unusual.

When the experiment tests the effect of an intervention on the mean of a
continuous outcome measure, the sample size can be calculated a priori,
based on a mathematical relationship between the predefined,
biologically relevant effect size, variability estimated from prior
data, chosen significance level, power, and sample size (see @sec-information-used-in-a-power-calculation and
[@pbio.3000411.ref017; @pbio.3000411.ref041] for practical advice).
If you have used an a priori sample size calculation, report

- the analysis method (e.g., two-tailed Student *t* test with a 0.05 significance threshold)
- the effect size of interest and a justification explaining why an effect size of that magnitude is relevant
- the estimate of variability used (e.g., standard deviation) and how it was estimated
- the power selected.

## Information used in a power calculation {#sec-information-used-in-a-power-calculation}

Sample size calculation is based on a mathematical relationship between
the following parameters: effect size, variability, significance level,
power, and sample size. Questions to consider are the following:

### The primary objective of the experiment---What is the main outcome measure?

The primary outcome measure should be identified in the planning stage
of the experiment; it is the outcome of greatest importance, which will
answer the main experimental question.

### The predefined effect size---What is a biologically relevant effect size?

The effect size is estimated as a biologically relevant change in the
primary outcome measure between the groups under study. This can be
informed by similar studies and involves scientists exploring what
magnitude of effect would generate interest and would be worth taking
forward into further work. In preclinical studies, the clinical
relevance of the effect should also be taken into consideration.

### What is the estimate of variability?

Estimates of variability can be obtained

- From data collected from a preliminary experiment conducted under identical conditions to the planned experiment, e.g., a previous experiment in the same laboratory, testing the same treatment under similar conditions on animals with the same characteristics
- From the control group in a previous experiment testing a different treatment
- From a similar experiment reported in the literature

### Significance threshold---What risk of a false positive is acceptable?

The significance level or threshold (α) is the probability of obtaining
a false positive. If it is set at 0.05, then the risk of obtaining a
false positive is 1 in 20 for a single statistical test. However, the
threshold or the *p*-values will need to be adjusted in scenarios of
multiple testing (e.g., by using a Bonferroni correction).

### Power---What risk of a false negative is acceptable?

For a predefined, biologically meaningful effect size, the power (1 − β)
is the probability that the statistical test will detect the effect if
it genuinely exists (i.e., true positive result). A target power between
80% and 95% is normally deemed acceptable, which entails a risk of false
negative between 5% and 20%.

### Directionality---Will you use a one- or two-sided test?

The directionality of a test depends on the distribution of the test
statistics for a given analysis. For tests based on *t* or *z*
distributions (such as *t* tests), whether the data will be analysed
using a one- or two-sided test relates to whether the alternative
hypothesis is directional or not. An experiment with a directional
(one-sided) alternative hypothesis can be powered and analysed with a
one-sided test with the goal of maximising the sensitivity to detect
this directional effect. Controversy exists within the statistics
community on when it is appropriate to use a one-sided test
[@pbio.3000411.ref042]. The use of a one-sided test requires
justification of why a treatment effect is only of interest when it is
in a defined direction and why they would treat a large effect in the
unexpected direction no differently from a nonsignificant difference
[@pbio.3000411.ref043]. Following the use of a one-sided test, the
investigator cannot then test for the possibility of missing an effect
in the untested direction. Choosing a one-tailed test for the sole
purpose of attaining statistical significance is not appropriate.

Two-sided tests with a nondirectional alternative hypothesis are much
more common and allow researchers to detect the effect of a treatment
regardless of its direction.

Note that analyses such as ANOVA and chi-squared are based on
asymmetrical distributions (F-distribution and chi-squared distribution)
with only one tail. Therefore, these tests do not have a directionality
option.

There are several types of studies in which a priori sample size
calculations are not appropriate. For example, the number of animals
needed for antibody or tissue production is determined by the amount
required and the production ability of an individual animal. For studies
in which the outcome is the successful generation of a sample or a
condition (e.g., the production of transgenic animals), the number of
animals is determined by the probability of success of the experimental
procedure.

In early feasibility or pilot studies, the number of animals required
depends on the purpose of the study. When the objective of the
preliminary study is primarily logistic or operational (e.g., to improve
procedures and equipment), the number of animals needed is generally
small. In such cases, power calculations are not appropriate and sample
sizes can be estimated based on operational capacity and constraints
[@pbio.3000411.ref044]. Pilot studies alone are unlikely to provide
adequate data on variability for a power calculation for future
experiments. Systematic reviews and previous studies are more
appropriate sources of information on variability
[@pbio.3000411.ref045].

If no power calculation was used to determine the sample size, state
this explicitly and provide the reasoning that was used to decide on the
sample size per group. Regardless of whether a power calculation was
used or not, when explaining how the sample size was determined take
into consideration any anticipated loss of animals or data, for example,
due to exclusion criteria established upfront or expected attrition (see
Item 3. Inclusion and exclusion criteria).

## Examples

> 'The sample size calculation was based on postoperative pain numerical
rating scale (NRS) scores after administration of buprenorphine (NRS AUC
mean = 2.70; noninferiority limit = 0.54; standard deviation = 0.66) as
the reference treatment... and also Glasgow Composite Pain Scale (GCPS)
scores... using online software (Experimental design assistant;
<https://eda.nc3rs.org.uk/eda/login/auth>). The power of the experiment
was set to 80%. A total of 20 dogs per group were considered necessary'
[@pbio.3000411.ref046].

> 'We selected a small sample size because the bioglass prototype was
evaluated in vivo for the first time in the present study, and
therefore, the initial intention was to gather basic evidence regarding
the use of this biomaterial in more complex experimental designs'
[@pbio.3000411.ref047].
