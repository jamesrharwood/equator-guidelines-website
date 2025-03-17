---
id: randomisation
title: 4a. Randomisation Use
checklist: 
    text: State whether randomisation was used to allocate experimental units to control and treatment groups. If done, provide the method used to generate the randomisation sequence.
---

## What to write

State whether randomisation was used to allocate experimental
units to control and treatment groups.

If done, provide the method used to generate the randomisation sequence.

## Explanation

Using appropriate randomisation methods during the
allocation to groups ensures that each experimental unit has an equal
probability of receiving a particular treatment and provides balanced
numbers in each treatment group. Selecting an animal 'at random' (i.e.,
haphazardly or arbitrarily) from a cage is not statistically random, as
the process involves human judgement. It can introduce bias that
influences the results, as a researcher may (consciously or
subconsciously) make judgements in allocating an animal to a particular
group, or because of unknown and uncontrolled differences in the
experimental conditions or animals in different groups. Using a
validated method of randomisation helps minimise selection bias and
reduce systematic differences in the characteristics of animals
allocated to different groups
[@pbio.3000411.ref062; @pbio.3000411.ref063; @pbio.3000411.ref064]. Inferential
statistics based on nonrandomised group allocation are not valid
[@pbio.3000411.ref065; @pbio.3000411.ref066]. Thus, the use of
randomisation is a prerequisite for any experiment designed to test a
hypothesis. Examples of appropriate randomisation methods include online
random number generators (e.g.,
<https://www.graphpad.com/quickcalcs/randomize1/>) or a function like
Rand() in spreadsheet software such as Excel, Google Sheets, or
LibreOffice. The EDA has a dedicated feature for randomisation and
allocation concealment [@pbio.3000411.ref019].

Systematic reviews have shown that animal experiments that do not report
randomisation or other bias-reducing measures such as blinding are more
likely to report exaggerated effects that meet conventional measures of
statistical significance
[@pbio.3000411.ref067; @pbio.3000411.ref068; @pbio.3000411.ref069]. It is especially
important to use randomisation in situations in which it is not possible
to blind all or parts of the experiment, but even with randomisation,
researcher bias can pervert the allocation. This can be avoided by using
allocation concealment (see Item 5. Blinding). In studies in which
sample sizes are small, simple randomisation may result in unbalanced
groups; here, randomisation strategies to balance groups such as
randomising in matched pairs
[@pbio.3000411.ref070; @pbio.3000411.ref071; @pbio.3000411.ref072] and blocking are
encouraged [@pbio.3000411.ref017]. Reporting the precise method used
to allocate animals or experimental units to groups enables readers to
assess the reliability of the results and identify potential
limitations.

Report the type of randomisation used (simple, stratified, randomised
complete blocks, etc.; see @sec-randomisation-strategy), the method used to
generate the randomisation sequence (e.g., computer-generated
randomisation sequence, with details of the algorithm or programme
used), and what was randomised (e.g., treatment to experimental unit,
order of treatment for each animal). If this varies between experiments,
report this information specifically for each experiment. If
randomisation was not the method used to allocate experimental units to
groups, state this explicitly and explain how the groups being compared
were formed.

## Considerations for the randomisation strategy {#sec-randomisation-strategy}

### Simple randomisation

All animals/samples are simultaneously randomised to the treatment
groups without considering any other variable. This strategy is rarely
appropriate, as it cannot ensure that comparison groups are balanced for
other variables that might influence the result of an experiment.

### Randomisation within blocks

Blocking is a method of controlling natural variation among experimental
units. This splits up the experiment into smaller subexperiments
(blocks), and treatments are randomised to experimental units within
each block
[@pbio.3000411.ref017; @pbio.3000411.ref066; @pbio.3000411.ref073].
This takes into account nuisance variables that could potentially bias
the results (e.g., cage location, day or week of procedure).

Stratified randomisation uses the same principle as randomisation within
blocks, only the strata tend to be traits of the animal that are likely
to be associated with the response (e.g., weight class or tumour size
class). This can lead to differences in the practical implementation of
stratified randomisation as compared with block randomisation (e.g.,
there may not be equal numbers of experimental units in each weight
class).

### Other randomisation strategies

Minimisation is an alternative strategy to allocate animals/samples to
treatment group to balance variables that might influence the result of
an experiment. With minimisation, the treatment allocated to the next
animal/sample depends on the characteristics of those animals/samples
already assigned. The aim is that each allocation should minimise the
imbalance across multiple factors [@pbio.3000411.ref074]. This
approach works well for a continuous nuisance variable such as body
weight or starting tumour volume.

### Examples of nuisance variables that can be accounted for in the randomisation strategy

- Time or day of the experiment
- Litter, cage, or fish tank
- Investigator or surgeon---different level of experience in the
    people administering the treatments, performing the surgeries, or
    assessing the results may result in varying stress levels in the
    animals or duration of anaesthesia
- Equipment (e.g., PCR machine, spectrophotometer)---calibration may
    vary
- Measurement of a study parameter (e.g., initial tumour volume)
- Animal characteristics (e.g., sex, age bracket, weight bracket)
- Location---exposure to light, ventilation, and disturbances may vary
    in cages located at different height or on different racks, which
    may affect important physiological processes

### Implication for the analysis

If blocking factors are used in the randomisation, they should also be
included in the analysis. Nuisance variables increase variability in the
sample, which reduces statistical power. Including a nuisance variable
as a blocking factor in the analysis accounts for that variability and
can increase the power, thus increasing the ability to detect a real
effect with fewer experimental units. However, blocking uses up degrees
of freedom and thus reduces the power if the nuisance variable does not
have a substantial impact on variability.

## Examples

> 'Fifty 12-week-old male Sprague-Dawley rats, weighing 320--360g, were
obtained from Guangdong Medical Laboratory Animal Center (Guangzhou,
China) and randomly divided into two groups (25 rats/group): the intact
group and the castration group. Random numbers were generated using the
standard = RAND() function in Microsoft Excel'
[@pbio.3000411.ref075].

> 'Animals were randomized after surviving the initial I/R, using a
computer based random order generator' [@pbio.3000411.ref076].

> 'At each institute, phenotyping data from both sexes is collected at
regular intervals on age-matched wildtype mice of equivalent genetic
backgrounds. Cohorts of at least seven homozygote mice of each sex per
pipeline were generated.... The random allocation of mice to
experimental group (wildtype versus knockout) was driven by Mendelian
Inheritance' [@pbio.3000411.ref029].
