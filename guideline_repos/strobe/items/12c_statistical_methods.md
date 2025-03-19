---
id: statistical-methods-missing-data
title: "12c. Statistical methods – missing data"
checklist: 
    text: Explain how missing data were addressed.
---

## What to write

Explain how missing data were addressed.

## Explanation

Missing data are common in observational research. Questionnaires posted
to study participants are not always filled in completely, participants
may not attend all follow-up visits and routine data sources and
clinical databases are often incomplete. Despite its ubiquity and
importance, few papers report in detail on the problem of missing data
[@pmed-0040297-b005; @pmed-0040297-b107]. Investigators may use any
of several approaches to address missing data. We describe some
strengths and limitations of various approaches in [{{< meta items.statistical-methods-missing-data.title >}}]({{< meta items.statistical-methods-missing-data.web_path >}}#missing-data)
. We advise that authors
report the number of missing values for each variable of interest
(exposures, outcomes, confounders) and for each step in the analysis.
Authors should give reasons for missing values if possible, and indicate
how many individuals were excluded because of missing data when
describing the flow of participants through the study (see also item
13). For analyses that account for missing data, authors should describe
the nature of the analysis (e.g., multiple imputation) and the
assumptions that were made (e.g., missing at random, see [{{< meta items.statistical-methods-missing-data.title >}}]({{< meta items.statistical-methods-missing-data.web_path >}}#missing-data)).

### Missing data: problems and possible solutions {#missing-data}

A common approach to dealing with missing data is to restrict analyses
to individuals with complete data on all variables required for a
particular analysis. Although such 'complete-case' analyses are
unbiased in many circumstances, they can be biased and are always
inefficient [@pmed-0040297-b108]. Bias arises if individuals with
missing data are not typical of the whole sample. Inefficiency arises
because of the reduced sample size for analysis.

Using the last observation carried forward for repeated measures can
distort trends over time if persons who experience a foreshadowing of
the outcome selectively drop out [@pmed-0040297-b109]. Inserting a
missing category indicator for a confounder may increase residual
confounding [@pmed-0040297-b107]. Imputation, in which each missing
value is replaced with an assumed or estimated value, may lead to
attenuation or exaggeration of the association of interest, and without
the use of sophisticated methods described below may produce standard
errors that are too small.

Rubin developed a typology of missing data problems, based on a model
for the probability of an observation being missing
[@pmed-0040297-b108; @pmed-0040297-b110]. Data are described as
missing completely at random (MCAR) if the probability that a particular
observation is missing does not depend on the value of any observable
variable(s). Data are missing at random (MAR) if, given the observed
data, the probability that observations are missing is independent of
the actual values of the missing data. For example, suppose younger
children are more prone to missing spirometry measurements, but that the
probability of missing is unrelated to the true unobserved lung
function, after accounting for age. Then the missing lung function
measurement would be MAR in models including age. Data are missing not
at random (MNAR) if the probability of missing still depends on the
missing value even after taking the available data into account. When
data are MNAR valid inferences require explicit assumptions about the
mechanisms that led to missing data.

Methods to deal with data missing at random (MAR) fall into three broad
classes [@pmed-0040297-b108; @pmed-0040297-b111]: likelihood-based
approaches [@pmed-0040297-b112], weighted estimation
[@pmed-0040297-b113] and multiple imputation
[@pmed-0040297-b111; @pmed-0040297-b114]. Of these three
approaches, multiple imputation is the most commonly used and flexible,
particularly when multiple variables have missing values
[@pmed-0040297-b115]. Results using any of these approaches should
be compared with those from complete case analyses, and important
differences discussed. The plausibility of assumptions made in missing
data analyses is generally unverifiable. In particular it is impossible
to prove that data are MAR, rather than MNAR. Such analyses are
therefore best viewed in the spirit of sensitivity analysis (see items
12e and 17).

## Examples

> "Our missing data analysis procedures used missing at random (MAR)
assumptions. We used the MICE (multivariate imputation by chained
equations) method of multiple multivariate imputation in STATA. We
independently analysed 10 copies of the data, each with missing values
suitably imputed, in the multivariate logistic regression analyses. We
averaged estimates of the variables to give a single mean estimate and
adjusted standard errors according to Rubin's rules"
[@pmed-0040297-b106].