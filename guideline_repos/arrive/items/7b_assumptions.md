---
id: statistical-methods-assumptions
title: 7b. Statistical Assumptions
checklist: 
    text: Describe any methods used to assess whether the data met the assumptions of the statistical approach, and what was done if the assumptions were not met.
---

## What to write

Describe any methods used to assess whether the data met the assumptions of the statistical approach, and what was done if the assumptions were not met.

## Explanation

Hypothesis tests are based on assumptions about the
underlying data. Describing how assumptions were assessed and whether
these assumptions are met by the data enables readers to assess the
suitability of the statistical approach used. If the assumptions are
incorrect, the conclusions may not be valid. For example, the
assumptions for data used in parametric tests (such as a *t* test, *z*
test, ANOVA, etc.) are that the data are continuous, the residuals from
the analysis are normally distributed, the responses are independent,
and different groups have similar variances.

There are various tests for normality, for example, the Shapiro-Wilk and
Kolmogorov-Smirnov tests. However, these tests have to be used
cautiously. If the sample size is small, they will struggle to detect
non-normality; if the sample size is large, the tests will detect
unimportant deviations. An alternative approach is to evaluate data with
visual plots, e.g., normal probability plots, box plots, scatterplots.
If the residuals of the analysis are not normally distributed, the
assumption may be satisfied using a data transformation in which the
same mathematical function is applied to all data points to produce
normally distributed data (e.g., log~e~, log~10~, square root).

Other types of outcome measures (binary, categorical, or ordinal) will
require different methods of analysis, and each will have different sets
of assumptions. For example, categorical data are summarised by counts
and percentages or proportions and are analysed by tests of proportions;
these analysis methods assume that data are binary, ordinal or nominal,
and independent [@pbio.3000411.ref018].

For each statistical test used (parametric or nonparametric), report the
type of outcome measure and the methods used to test the assumptions of
the statistical approach. If data were transformed, identify precisely
the transformation used and which outcome measures it was applied to.
Report any changes to the analysis if the assumptions were not met and
an alternative approach was used (e.g., a nonparametric test was used,
which does not require the assumption of normality). If the relevant
assumptions about the data were not tested, state this explicitly.

## Examples

> 'Model assumptions were checked using the Shapiro-Wilk normality test
and Levene's Test for homogeneity of variance and by visual inspection
of residual and fitted value plots. Some of the response variables had
to be transformed by applying the natural logarithm or the second or
third root, but were back-transformed for visualization of significant
effects' [@pbio.3000411.ref101].

> 'The effects of housing (treatment) and day of euthanasia on cortisol
levels were assessed by using fixed-effects 2-way ANOVA. An initial
exploratory analysis indicated that groups with higher average cortisol
levels also had greater variation in this response variable. To make the
variation more uniform, we used a logarithmic transform of each fish's
cortisol per unit weight as the dependent variable in our analyses. This
action made the assumptions of normality and homoscedasticity (standard
deviations were equal) of our analyses reasonable'
[@pbio.3000411.ref102].
