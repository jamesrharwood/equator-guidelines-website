---
id: statistical-methods-description
title: "12a. Statistical methods"
checklist: 
    text: Describe all statistical methods, including those used to control for confounding.
---

## What to write

Describe all statistical methods, including those used to control for confounding.

## Explanation

In general, there is no one correct statistical analysis but, rather,
several possibilities that may address the same question, but make
different assumptions. Regardless, investigators should pre-determine
analyses at least for the primary study objectives in a study protocol.
Often additional analyses are needed, either instead of, or as well as,
those originally envisaged, and these may sometimes be motivated by the
data. When a study is reported, authors should tell readers whether
particular analyses were suggested by data inspection. Even though the
distinction between pre-specified and exploratory analyses may sometimes
be blurred, authors should clarify reasons for particular analyses.

If groups being compared are not similar with regard to some
characteristics, adjustment should be made for possible confounding
variables by stratification or by multivariable regression (see [{{< meta items.statistical-methods-description.title >}}]({{< meta items.statistical-methods-description.web_path >}}#confounding))
[@pmed-0040297-b094]. Often, the study design determines which type
of regression analysis is chosen. For instance, Cox proportional hazard
regression is commonly used in cohort studies [@pmed-0040297-b095].
whereas logistic regression is often the method of choice in
case-control studies [@pmed-0040297-b096; @pmed-0040297-b097].
Analysts should fully describe specific procedures for variable
selection and not only present results from the final model
[@pmed-0040297-b098; @pmed-0040297-b099]. If model comparisons are
made to narrow down a list of potential confounders for inclusion in a
final model, this process should be described. It is helpful to tell
readers if one or two covariates are responsible for a great deal of the
apparent confounding in a data analysis. Other statistical analyses such
as imputation procedures, data transformation, and calculations of
attributable risks should also be described. Non-standard or novel
approaches should be referenced and the statistical software used
reported. As a guiding principle, we advise statistical methods be
described "with enough detail to enable a knowledgeable reader with
access to the original data to verify the reported results"
[@pmed-0040297-b100].

In an empirical study, only 93 of 169 articles (55%) reporting
adjustment for confounding clearly stated how continuous and
multi-category variables were entered into the statistical model
[@pmed-0040297-b101]. Another study found that among 67 articles in
which statistical analyses were adjusted for confounders, it was mostly
unclear how confounders were chosen [@pmed-0040297-b004].

### Confounding {#confounding}

Confounding literally means confusion of effects. A study might seem to
show either an association or no association between an exposure and the
risk of a disease. In reality, the seeming association or lack of
association is due to another factor that determines the occurrence of
the disease but that is also associated with the exposure. The other
factor is called the confounding factor or confounder. Confounding thus
gives a wrong assessment of the potential 'causal' association of an
exposure. For example, if women who approach middle age and develop
elevated blood pressure are less often prescribed oral contraceptives, a
simple comparison of the frequency of cardiovascular disease between
those who use contraceptives and those who do not, might give the wrong
impression that contraceptives protect against heart disease.

Investigators should think beforehand about potential confounding
factors. This will inform the study design and allow proper data
collection by identifying the confounders for which detailed information
should be sought. Restriction or matching may be used. In the example
above, the study might be restricted to women who do not have the
confounder, elevated blood pressure. Matching on blood pressure might
also be possible, though not necessarily desirable (see [{{< meta items.matching-criteria.title >}}]({{< meta items.matching-criteria.web_path >}}#matching)). In the analysis phase,
investigators may use stratification or multivariable analysis to reduce
the effect of confounders. Stratification consists of dividing the data
in strata for the confounder (e.g., strata of blood pressure), assessing
estimates of association within each stratum, and calculating the
combined estimate of association as a weighted average over all strata.
Multivariable analysis achieves the same result but permits one to take
more variables into account simultaneously. It is more flexible but may
involve additional assumptions about the mathematical form of the
relationship between exposure and disease.

Taking confounders into account is crucial in observational studies, but
readers should not assume that analyses adjusted for confounders
establish the 'causal part' of an association. Results may still be
distorted by residual confounding (the confounding that remains after
unsuccessful attempts to control for it [@pmed-0040297-b102]),
random sampling error, selection bias and information bias (see [{{< meta items.bias.title >}}]({{< meta items.bias.web_path >}}#bias)
).

## Examples

> "The adjusted relative risk was calculated using the Mantel-Haenszel
technique, when evaluating if confounding by age or gender was present
in the groups compared. The 95% confidence interval (CI) was computed
around the adjusted relative risk, using the variance according to
Greenland and Robins and Robins et al." [@pmed-0040297-b093].