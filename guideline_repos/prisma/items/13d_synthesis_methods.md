---
id: synthesis_methods_d
title: "13d. Synthesis methods – Synthesis methods"
summary: 
    title: 13d. Synthesis methods
---

Describe any methods used to synthesise results and provide a rationale for the choice(s). If meta-analysis was performed, describe the model(s), method(s) to identify the presence and extent of statistical heterogeneity, and software package(s) used.

## Essential elements

-   If statistical synthesis methods were used, reference the software,
    packages, and version numbers used to implement synthesis methods
    (such as *metan* in Stata 16,[@ref117] metafor (version 2.1-0) in
    R[@ref118]).

-   If it was not possible to conduct a meta-analysis, describe and
    justify the synthesis methods (such as combining P values was used
    because no or minimal information beyond P values and direction of
    effect was reported in the studies) or summary approach used.

-   If meta-analysis was done, specify:

    -   the meta-analysis model (fixed-effect, fixed-effects, or
        random-effects) and provide rationale for the selected model.

    -   the method used (such as Mantel-Haenszel,
        inverse-variance).[@ref103]

    -   any methods used to identify or quantify statistical
        heterogeneity (such as visual inspection of results, a formal
        statistical test for heterogeneity,[@ref103] heterogeneity
        variance (τ^2^), inconsistency (such as I^2^ [@ref119]), and
        prediction intervals[@ref120]).

-   If a random-effects meta-analysis model was used, specify:

    -   the between-study (heterogeneity) variance estimator used (such
        as DerSimonian and Laird, restricted maximum likelihood (REML)).

    -   the method used to calculate the confidence interval for the
        summary effect (such as Wald-type confidence interval,
        Hartung-Knapp-Sidik-Jonkman[@ref108]).

-   If a Bayesian approach to meta-analysis was used, describe the prior
    distributions about quantities of interest (such as intervention
    effect being analysed, amount of heterogeneity in results across
    studies).[@ref103]

-   If multiple effect estimates from a study were included in a
    meta-analysis (as may arise, for example, when a study reports
    multiple outcomes eligible for inclusion in a particular
    meta-analysis), describe the method(s) used to model or account for
    the statistical dependency (such as multivariate meta-analysis,
    multilevel models, or robust variance estimation).[@ref37] [@ref69]

-   If a planned synthesis was not considered possible or appropriate,
    report this and the reason for that decision.

## Additional elements

-   If a random-effects meta-analysis model was used, consider
    specifying other details about the methods used, such as the method
    for calculating confidence limits for the heterogeneity variance.

## Explanation

Various statistical methods are available to
synthesise results, the most common of which is meta-analysis of effect
estimates (see @sec-meta-analysis). Meta-analysis is
used to synthesise effect estimates across studies, yielding a summary
estimate. Different meta-analysis models are available, with the
random-effects and fixed-effect models being in widespread use. Model
choice can importantly affect the summary estimate and its confidence
interval; hence the rationale for the selected model should be provided
(see below). For random-effects models,
many methods are available, and their performance has been shown to
differ depending on the characteristics of the meta-analysis (such as
the number and size of the included studies[@ref113] [@ref114]).

## Meta-analysis and its extensions {#sec-meta-analysis}

Meta-analysis is a statistical technique used to synthesise results when
study effect estimates and their variances are available, yielding a
quantitative summary of results.[@ref103] The method facilitates
interpretation that would otherwise be difficult to achieve if, for
example, a narrative summary of each result was presented, particularly
as the number of studies increases. Furthermore, meta-analysis increases
the chance of detecting a clinically important effect as statistically
significant, if it exists, and increases the precision of the estimated
effect.[@ref104]

### Meta-analysis models and methods

The summary estimate is a weighted average of the study effect
estimates, where the study weights are determined primarily by the
meta-analysis model. The two most common meta-analysis models are the
"fixed-effect" and "random-effects" models.[@ref103] The assumption
underlying the fixed-effect model is that there is one true (common)
intervention effect and that the observed differences in results across
studies reflect random variation only. This model is sometimes referred
to as the "common-effects" or "equal-effects" model.[@ref103] A
fixed-effect model can also be interpreted under a different assumption,
that the true intervention effects are different and unrelated. This
model is referred to as the "fixed-effects" model.[@ref105] The
random-effects model assumes that there is not one true intervention
effect but, rather, a distribution of true intervention effects and that
the observed differences in results across studies reflect real
differences in the effects of an intervention.[@ref104] The
random-effects and fixed-effects models are similar in that they assume
the true intervention effects are different, but they differ in that the
random-effects model assumes the effects are related through a
distribution, whereas the fixed-effects model does not make this
assumption.

Many considerations may influence an author's choice of meta-analysis
model. For example, their choice may be based on the clinical and
methodological diversity of the included studies and the expectation
that the underlying intervention effects will differ (potentially
leading to selection of a random-effects model) or concern about
small-study effects (the tendency for smaller studies to show different
effects to larger ones,[@ref106] potentially leading to fitting of both
a random-effects and fixed-effect model). Sometimes authors select a
model based on the heterogeneity statistics observed (for example,
switch from a fixed-effect to a random-effects model if the I^2^
statistic was \>50%).[@ref107] However, this practice is strongly
discouraged.

There are different methods available to assign weights in fixed-effect
or random-effects meta-analyses (such as Mantel-Haenszel,
inverse-variance).[@ref103] For random-effects meta-analyses, there are
also different ways to estimate the between-study variance (such as
DerSimonian and Laird, restricted maximum likelihood (REML)) and
calculate the confidence interval for the summary effect (such as
Wald-type confidence interval, Hartung-Knapp-Sidik-Jonkman[@ref108]).
Readers are referred to Deeks et al[@ref103] for further information on
how to select a particular meta-analysis model and method.

### Subgroup analyses, meta-regression, and sensitivity analyses

Extensions to meta-analysis, including subgroup analysis and
meta-regression, are available to explore causes of variation of results
across studies (that is, statistical heterogeneity).[@ref103] Subgroup
analyses involve splitting studies or participant data into subgroups
and comparing the effects of the subgroups. Meta-regression is an
extension of subgroup analysis that allows for the effect of continuous
and categorical variables to be investigated.[@ref109] Authors might use
either type of analysis to explore, for example, whether the
intervention effect estimate varied with different participant
characteristics (such as mild versus severe disease) or intervention
characteristics (such as high versus low dose of a drug).

Sensitivity analyses are undertaken to examine the robustness of
findings to decisions made during the review process. This involves
repeating an analysis but using different decisions from those
originally made and informally comparing the findings.[@ref103] For
example, sensitivity analyses might have been done to examine the impact
on the meta-analysis of including results from conference abstracts that
have never been published in full, including studies where most (but not
all) participants were in a particular age range, including studies at
high risk of bias, or using a fixed-effect versus random-effects
meta-analysis model.

Sensitivity analyses differ from subgroup analyses. Sensitivity analyses
consist of making informal comparisons between different ways of
estimating the same effect, whereas subgroup analyses consist of
formally undertaking a statistical comparison across the
subgroups.[@ref103]

### Extensions to meta-analysis that model or account for dependency

In most meta-analyses, effect estimates from independent studies are
combined. Standard meta-analysis methods are appropriate for this
situation, since an underlying assumption is that the effect estimates
are independent. However, standard meta-analysis methods are not
appropriate when the effect estimates are correlated. Correlated effect
estimates arise when multiple effect estimates from a single study are
calculated using some or all of the same participants and are included
in the same meta-analysis. For example, where multiple effect estimates
from a multi-arm trial are included in the same meta-analysis, or effect
estimates for multiple outcomes from the same study are included. For
this situation, a range of methods are available that appropriately
model or account for the dependency of the effect estimates. These
methods include multivariate meta-analysis,[@ref110] multilevel
models,[@ref111] or robust variance estimation.[@ref112] See Lopez-Lopez
for further discussion.[@ref69]

When study data are not amenable to meta-analysis of effect estimates,
alternative statistical synthesis methods (such as calculating the
median effect across studies, combining P values) or structured
summaries might be used.[@ref28] [@ref115] Additional guidance for
reporting alternative statistical synthesis methods is available (see
Synthesis Without Meta-analysis (SWiM) reporting guideline[@ref116]).

Regardless of the chosen synthesis method(s), authors should provide
sufficient detail such that readers are able to assess the
appropriateness of the selected methods and could reproduce the reported
results (with access to the data).

## Examples

### Example 1: meta-analysis

"As the effects of functional appliance treatment were deemed to be
highly variable according to patient age, sex, individual maturation of
the maxillofacial structures, and appliance characteristics, a
random-effects model was chosen to calculate the average distribution of
treatment effects that can be expected. A restricted maximum likelihood
random-effects variance estimator was used instead of the older
DerSimonian-Laird one, following recent guidance. Random-effects 95%
prediction intervals were to be calculated for meta-analyses with at
least three studies to aid in their interpretation by quantifying
expected treatment effects in a future clinical setting. The extent and
impact of between-study heterogeneity were assessed by inspecting the
forest plots and by calculating the tau-squared and the I-squared
statistics, respectively. The 95% CIs (uncertainty intervals) around
tau-squared and the I-squared were calculated to judge our confidence
about these metrics. We arbitrarily adopted the I-squared thresholds of
\>75% to be considered as signs of considerable heterogeneity, but we
also judged the evidence for this heterogeneity (through the uncertainty
intervals) and the localization on the forest plot...All analyses were
run in Stata SE 14.0 (StataCorp, College Station, TX) by one
author."[@ref183]

### Example 2: calculating the median effect across studies

> "We based our primary analyses upon consideration of dichotomous process
adherence measures (for example, the proportion of patients managed
according to evidence-based recommendations). In order to provide a
quantitative assessment of the effects associated with reminders without
resorting to numerous assumptions or conveying a misleading degree of
confidence in the results, we used the median improvement in dichotomous
process adherence measures across studies...With each study represented
by a single median outcome, we calculated the median effect size and
interquartile range across all included studies for that
comparison."[@ref184]