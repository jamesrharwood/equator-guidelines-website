---
id: selection-process
title: "8. Selection Process"
summary: 
    text: Specify the methods used to decide whether a study met the inclusion criteria of the review, including how many reviewers screened each record and each report retrieved, whether they worked independently, and, if applicable, details of automation tools used in the process.
writing_guide:
    text: >-
        Did you use an automatic classifier to eliminate records before screening by humans?  If so, report the number eliminated in the PRISMA flow diagram as ‘Records marked as ineligible by automation tools’  

        How many human reviewers independently screened titles and abstracts to decide whether to retrieve the full text? What process was used to resolve disagreements between screeners? 

        How many human reviewers independently screened each full text article to determine eligibility?  What process was used to resolve disagreements between screeners?  

        How many stages of screening were there, and what rules did you have to guide the people involved in the process? 

        Did you use any other method to eliminate records, such as sets of already screened out records?  

        Were the people involved in the screening and selection process independent from the review authors?  

        Did you use crowd-sourcing or automation techniques in the process of selecting eligible studies? If so, how did you integrate these into the selection process? 

        Did you use a machine learning tool (e.g. Cochrane RCT Classifier) to eliminate records or replace a human screener?  If so, report a reference to the version you used. 

        If you didn’t have enough information to decide if a study was eligible, what process did you use to obtain information from study investigators or other sources? 

        If abstracts or articles required translation into another language to determine their eligibility, what translation process did you use?   
---

Specify the methods used to decide whether a study met the inclusion criteria of the review, including how many reviewers screened each record and each report retrieved, whether they worked independently, and, if applicable, details of automation tools used in the process.

## Essential elements for systematic reviews regardless of the selection processes used

-   Report how many reviewers screened each record (title/abstract) and
    each report retrieved, whether multiple reviewers worked
    independently (that is, were unaware of each other's decisions) at
    each stage of screening or not (for example, records screened by one
    reviewer and exclusions verified by another), and any processes used
    to resolve disagreements between screeners (for example, referral to
    a third reviewer or by consensus).

-   Report any processes used to obtain or confirm relevant information
    from study investigators.

-   If abstracts or articles required translation into another language
    to determine their eligibility, report how these were translated
    (for example, by asking a native speaker or by using software
    programs).

## Essential elements for systematic reviews using automation tools in the selection process

-   Report how automation tools were integrated within the overall study
    selection process; for example, whether records were excluded based
    solely on a machine assessment or whether machine assessments were
    used to double-check human decisions.

-   If an externally derived machine learning classifier was applied
    (such as Cochrane RCT Classifier), either to eliminate records or to
    replace a single screener, include a reference or URL to the version
    used. If the classifier was used to eliminate records before
    screening, report the number eliminated in the PRISMA flow diagram
    as "Records marked as ineligible by automation tools."

-   If an internally derived machine learning classifier was used to
    assist with the screening process, identify the software/classifier
    and version, describe how it was used (such as to remove records or
    replace a single screener) and trained (if relevant), and what
    internal or external validation was done to understand the risk of
    missed studies or incorrect classifications. For example, authors
    might state that the classifier was trained on the set of records
    generated for the review in question (as may be the case when
    updating reviews) and specify which thresholds were applied to
    remove records.

-   If machine learning algorithms were used to prioritise screening
    (whereby unscreened records are continually re-ordered based on
    screening decisions), state the software used and provide details of
    any screening rules applied (for example, screening stopped
    altogether leaving some records to be excluded based on automated
    assessment alone, or screening switched from double to single
    screening once a pre-specified number or proportion of consecutive
    records was eliminated).

## Essential elements for systematic reviews using crowdsourcing or previous "known" assessments in the selection process

-   If crowdsourcing was used to screen records, provide details of the
    platform used and specify how it was integrated within the overall
    study selection process.

-   If datasets of already-screened records were used to eliminate
    records retrieved by the search from further consideration, briefly
    describe the derivation of these datasets. For example, if prior
    work has already determined that a given record does not meet the
    eligibility criteria, it can be removed without manual checking.
    This is the case for Cochrane's Screen4Me service, in which an
    increasingly large dataset of records that are known not to
    represent randomised trials can be used to eliminate any matching
    records from further consideration.

## Explanation

Study selection is typically a multi-stage process in
which potentially eligible studies are first identified from screening
titles and abstracts, then assessed through full text review and, where
necessary, contact with study investigators. Increasingly, a mix of
screening approaches might be applied (such as automation to eliminate
records before screening or prioritise records during screening). In
addition to automation, authors increasingly have access to screening
decisions that are made by people independent of the author team (such
as crowdsourcing) (see [box 3](#box3){ref-type="boxed-text"}). Authors
should describe in detail the process for deciding how records retrieved
by the search were considered for inclusion in the review, to enable
readers to assess the potential for errors in selection.[@ref49]
[@ref50] [@ref51] [@ref52]

## Study selection methods

Several approaches to selecting studies exist. Here we comment on the
advantages and disadvantages of each.

1.  *Assessment of each record by one reviewer:* Single screening is an
    efficient use of time and resources, but there is a higher risk of
    missing relevant studies[@ref49] [@ref50] [@ref51]

2.  *Assessment of records by more than one reviewer:* Double screening
    can vary from duplicate checking of all records (by two or more
    reviewers independently) to a second reviewer checking a sample only
    (for example, a random sample of screened records, or all excluded
    records). This approach may be more reliable than single screening
    but at the expense of increased reviewer time, given the time needed
    to resolve discrepancies[@ref49] [@ref50] [@ref51]

3.  *Priority screening to focus early screening effort on most relevant records:*
    Instead of screening records in year, title, author or
    random order, machine learning is used to identify relevant studies
    earlier in the screening process than would otherwise be the case.
    Priority screening is an iterative process in which the machine
    continually reassesses unscreened records for relevance. This
    approach can increase review efficiency by enabling the review team
    to start on subsequent steps of the review while less relevant
    records are still being screened. Both single and multiple reviewer
    assessments can be combined with priority screening[@ref52] [@ref53]

4.  *Priority screening with the automatic elimination of less relevant records:* 
    Once the most relevant records have been identified using
    priority screening, teams may choose to stop screening based on the
    assumption that the remaining records are unlikely to be relevant.
    However, there is a risk of erroneously excluding relevant studies
    because of uncertainty about when it is safe to stop screening; the
    balance between efficiency gains and risk tolerance will be
    review-specific[@ref52] [@ref53]

5.  *Machine learning classifiers:* Machine learning classifiers are
    statistical models that use training data to rank records according
    to their relevance. They can be calibrated to achieve a given level
    of recall, thus enabling reviewers to implement screening rules,
    such as eliminating records or replacing double with single
    screening. Because the performance of classifiers is highly
    dependent on the data used to build them, classifiers should only be
    used to classify records for which they are designed[@ref53]
    [@ref54]

6.  *Previous "known" assessments:* Screening decisions for records
    that have already been manually checked can be reused to exclude the
    same records from being reassessed, provided the eligibility
    criteria are the same. For example, groups that maintain registers
    of controlled trials to facilitate systematic reviews can avoid
    continually rescreening the same records by matching and then
    including/excluding those records from further consideration.

7.  *Crowdsourcing:* Crowdsourcing involves recruiting (usually via the
    internet) a large group of individuals to contribute to a task or
    project, such as screening records. If crowdsourcing is integrated
    with other study selection approaches, the specific platforms used
    should have well established and documented agreement algorithms,
    and data on crowd accuracy and reliability[@ref55] [@ref56]

## Example

> "Three researchers (AP, HB-R, FG) independently reviewed titles and
abstracts of the first 100 records and discussed inconsistencies until
consensus was obtained. Then, in pairs, the researchers independently
screened titles and abstracts of all articles retrieved. In case of
disagreement, consensus on which articles to screen full-text was
reached by discussion. If necessary, the third researcher was consulted
to make the final decision. Next, two researchers (AP, HB-R)
independently screened full-text articles for inclusion. Again, in case
of disagreement, consensus was reached on inclusion or exclusion by
discussion and if necessary, the third researcher (FG) was
consulted."[@ref174]

For examples of systematic reviews using automation tools,
crowdsourcing, or previous "known" assessments in the selection process,
see supplementary table S1 on bmj.com

<!-- #TODO fix "S1 table on bmj.com" -->