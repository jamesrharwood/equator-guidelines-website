---
id: matching-criteria
title: "6b. Matching criteria"
checklist: 
    text: "**Cohort study:** For matched studies, give matching criteria and number of exposed and unexposed.
        **Case-control study:** For matched studies, give matching criteria and the number of controls per case."
---

## What to write

**Cohort study:** For matched studies, give matching criteria and number of exposed and unexposed.

**Case-control study:** For matched studies, give matching criteria and the number of controls per case.

## Explanation

Matching is much more common in case-control studies, but occasionally,
investigators use matching in cohort studies to make groups comparable
at the start of follow-up. Matching in cohort studies makes groups
directly comparable for potential confounders and presents fewer
intricacies than with case-control studies. For example, it is not
necessary to take the matching into account for the estimation of the
relative risk [@pmed-0040297-b048]. Because matching in cohort
studies may increase statistical precision investigators might allow for
the matching in their analyses and thus obtain narrower confidence
intervals.

In case-control studies matching is done to increase a study's
efficiency by ensuring similarity in the distribution of variables
between cases and controls, in particular the distribution of potential
confounding variables [@pmed-0040297-b048; @pmed-0040297-b049].
Because matching can be done in various ways, with one or more controls
per case, the rationale for the choice of matching variables and the
details of the method used should be described. Commonly used forms of
matching are frequency matching (also called group matching) and
individual matching. In frequency matching, investigators choose
controls so that the distribution of matching variables becomes
identical or similar to that of cases. Individual matching involves
matching one or several controls to each case. Although intuitively
appealing and sometimes useful, matching in case-control studies has a
number of disadvantages, is not always appropriate, and needs to be
taken into account in the analysis (see [below](#matching)).

Even apparently simple matching procedures may be poorly reported. For
example, authors may state that controls were matched to cases 'within
five years', or using 'five year age bands'. Does this mean that, if a
case was 54 years old, the respective control needed to be in the
five-year age band 50 to 54, or aged 49 to 59, which is within five
years of age 54? If a wide (e.g., 10-year) age band is chosen, there is
a danger of residual confounding by age (see [below](#grouping)), for example because
controls may then be younger than cases on average.

### Matching in case-control studies {#matching}

In any case-control study, sensible choices need to be made on whether
to use matching of controls to cases, and if so, what variables to match
on, the precise method of matching to use, and the appropriate method of
statistical analysis. Not to match at all may mean that the distribution
of some key potential confounders (e.g., age, sex) is radically
different between cases and controls. Although this could be adjusted
for in the analysis there could be a major loss in statistical
efficiency.

The use of matching in case-control studies and its interpretation are
fraught with difficulties, especially if matching is attempted on
several risk factors, some of which may be linked to the exposure of
prime interest [@pmed-0040297-b050; @pmed-0040297-b051]. For
example, in a case-control study of myocardial infarction and oral
contraceptives nested in a large pharmaco-epidemiologic data base, with
information about thousands of women who are available as potential
controls, investigators may be tempted to choose matched controls who
had similar levels of risk factors to each case of myocardial
infarction. One objective is to adjust for factors that might influence
the prescription of oral contraceptives and thus to control for
*confounding by indication*. However, the result will be a control group
that is *no longer representative* of the oral contraceptive use in the
source population: controls will be older than the source population
because patients with myocardial infarction tend to be older. This has
several implications. A crude analysis of the data will produce odds
ratios that are usually biased towards unity if the matching factor is
associated with the exposure. The solution is to perform a matched or
stratified analysis (see [{{< meta items.statistical-methods-matching-cases-controls.title >}}]({{< meta items.statistical-methods-matching-cases-controls.web_path >}})). In addition, because the matched
control group ceases to be representative for the population at large,
the exposure distribution among the controls can no longer be used to
estimate the population attributable fraction (see [{{< meta items.main-results-risk.title >}}]({{< meta items.main-results-risk.web_path >}})#measures-of-association)
[@pmed-0040297-b052]. Also, the effect of the matching factor can no
longer be studied, and the search for well-matched controls can be
cumbersome -- making a design with a non-matched control group
preferable because the non-matched controls will be easier to obtain and
the control group can be larger. *Overmatching* is another problem,
which may reduce the efficiency of matched case-control studies, and, in
some situations, introduce bias. Information is lost and the power of
the study is reduced if the matching variable is closely associated with
the exposure. Then many individuals in the same matched sets will tend
to have identical or similar levels of exposures and therefore not
contribute relevant information. Matching will introduce irremediable
bias if the matching variable is not a confounder but in the causal
pathway between exposure and disease. For example, in vitro
fertilization is associated with an increased risk of perinatal death,
due to an increase in multiple births and low birth weight infants
[@pmed-0040297-b053]. Matching on plurality or birth weight will
bias results towards the null, and this cannot be remedied in the
analysis.

Matching is intuitively appealing, but the complexities involved have
led methodologists to advise against routine matching in case-control
studies. They recommend instead a careful and judicious consideration of
each potential matching factor, recognizing that it could instead be
measured and used as an adjustment variable without matching on it. In
response, there has been a reduction in the number of matching factors
employed, an increasing use of frequency matching, which avoids some of
the problems discussed above, and more case-control studies with no
matching at all [@pmed-0040297-b054]. Matching remains most
desirable, or even necessary, when the distributions of the confounder
(e.g., age) might differ radically between the unmatched comparison
groups [@pmed-0040297-b048; @pmed-0040297-b049].

### Grouping {#grouping}

There are several reasons why continuous data may be grouped
[@pmed-0040297-b086]. When collecting data it may be better to use
an ordinal variable than to seek an artificially precise continuous
measure for an exposure based on recall over several years. Categories
may also be helpful for presentation, for example to present all
variables in a similar style, or to show a dose-response relationship.

Grouping may also be done to simplify the analysis, for example to avoid
an assumption of linearity. However, grouping loses information and may
reduce statistical power [@pmed-0040297-b087] especially when
dichotomization is used
[@pmed-0040297-b082; @pmed-0040297-b085; @pmed-0040297-b088]. If a
continuous confounder is grouped, residual confounding may occur,
whereby some of the variable's confounding effect remains unadjusted
for (see [{{< meta items.statistical-methods-description.title >}}]({{< meta items.statistical-methods-description.web_path >}}#confounding))
[@pmed-0040297-b062; @pmed-0040297-b089]. Increasing the number of
categories can diminish power loss and residual confounding, and is
especially appropriate in large studies. Small studies may use few
groups because of limited numbers.

Investigators may choose cut-points for groupings based on commonly used
values that are relevant for diagnosis or prognosis, for practicality,
or on statistical grounds. They may choose equal numbers of individuals
in each group using quantiles [@pmed-0040297-b090]. On the other
hand, one may gain more insight into the association with the outcome by
choosing more extreme outer groups and having the middle group(s) larger
than the outer groups [@pmed-0040297-b091]. In case-control studies,
deriving a distribution from the control group is preferred since it is
intended to reflect the source population. Readers should be informed if
cut-points are selected post hoc from several alternatives. In
particular, if the cut-points were chosen to minimise a P value the true
strength of an association will be exaggerated [@pmed-0040297-b081].

When analysing grouped variables, it is important to recognise their
underlying continuous nature. For instance, a possible trend in risk
across ordered groups can be investigated. A common approach is to model
the rank of the groups as a continuous variable. Such linearity across
group scores will approximate an actual linear relation if groups are
equally spaced (e.g., 10 year age groups) but not otherwise. Il'yasova
et al [@pmed-0040297-b092]. recommend publication of both the
categorical and the continuous estimates of effect, with their standard
errors, in order to facilitate meta-analysis, as well as providing
intrinsically valuable information on dose-response. One analysis may
inform the other and neither is assumption-free. Authors often ignore
the ordering and consider the estimates (and P values) separately for
each category compared to the reference category. This may be useful for
description, but may fail to detect a real trend in risk across groups.
If a trend is observed, a confidence interval for a slope might indicate
the strength of the observation.

## Examples

### Cohort study

"For each patient who initially received a statin, we used
propensity-based matching to identify one control who did not receive a
statin according to the following protocol. First, propensity scores
were calculated for each patient in the entire cohort on the basis of an
extensive list of factors potentially related to the use of statins or
the risk of sepsis. Second, each statin user was matched to a smaller
pool of non-statin-users by sex, age (plus or minus 1 year), and index
date (plus or minus 3 months). Third, we selected the control with the
closest propensity score (within 0.2 SD) to each statin user in a 1:1
fashion and discarded the remaining controls." [@pmed-0040297-b046].

### Case-control study

> "We aimed to select five controls for every case from among individuals
in the study population who had no diagnosis of autism or other
pervasive developmental disorders (PDD) recorded in their general
practice record and who were alive and registered with a participating
practice on the date of the PDD diagnosis in the case. Controls were
individually matched to cases by year of birth (up to 1 year older or
younger), sex, and general practice. For each of 300 cases, five
controls could be identified who met all the matching criteria. For the
remaining 994, one or more controls was excluded\..." [@pmed-0040297-b047].
