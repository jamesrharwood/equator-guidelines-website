---
id: 19_data_management
title: "19. Data management"
---
Plans for data entry, coding, security, and storage, including any related processes to promote data quality (eg, double data entry; range checks for data values). Reference to where details of data management procedures can be found, if not in the protocol

## Read More

Careful planning of data management with appropriate personnel can help to prevent flaws that compromise data validity. The protocol should provide a full description of the data entry and coding processes, along with measures to promote their quality, or provide key elements and a reference to where full information can be found. These details are particularly important for the primary outcome data. The protocol should also document data security measures to prevent unauthorised access to or loss of participant data, as well as plans for data storage (including timeframe) during and after the trial. This information facilitates an assessment of adherence to applicable standards and regulations.

Differences in data entry methods can affect the trial in terms of data accuracy,268 cost, and efficiency.271 For example, when compared with paper case report forms, electronic data capture can reduce the time required for data entry, query resolution, and database release by combining data entry with data collection (Item 18a).271 277 When data are collected on paper forms, data entry can be performed locally or at a central site. Local data entry can enable fast correction of missing or inaccurate data, while central data entry facilitates blinding (masking), standardisation, and training of a core group of data entry personnel.

Raw, non-numeric data are usually coded for ease of data storage, review, tabulation, and analysis. It is important to define standard coding practices to reduce errors and observer variation. When data entry and coding are performed by different individuals, it is particularly important that the personnel use unambiguous, standardised terminology and abbreviations to avoid misinterpretation.

As with data collection (Item 18a), standard processes are often implemented to improve the accuracy of data entry and coding.281 284 Common examples include double data entry296; verification that the data are in the proper format (eg, integer) or within an expected range of values; and independent source document verification of a random subset of data to identify missing or apparently erroneous values. Though widely performed to detect data entry errors, the time and costs of independent double data entry from paper forms need to be weighed against the magnitude of reduction in error rates compared to single-data entry.297 298 299

## Examples

> 13.9.2. Data Forms and Data Entry
In the FSGS-CT [focal segmental glomerulosclerosis—clinical trial], all data will be entered electronically. This may be done at a Core Coordinating Center or at the participating site where the data originated. Original study forms will be entered and kept on file at the participating site. A subset will be requested later for quality control; when a form is selected, the participating site staff will pull that form, copy it, and sent [sic] the copy to the DCC [data coordinating center] for re-entry.
...Participant files are to be stored in numerical order and stored in a secure and accessible place and manner. Participant files will be maintained in storage for a period of 3 years after completion of the study.
13.9.3. Data Transmission and Editing
The data entry screens will resemble the paper forms approved by the steering committee. Data integrity will be enforced through a variety of mechanisms. Referential data rules, valid values, range checks, and consistency checks against data already stored in the database (ie, longitudinal checks) will be supported. The option to chose [sic] a value from a list of valid codes and a description of what each code means will be available where applicable. Checks will be applied at the time of data entry into a specific field and/or before the data is written (committed) to the database. Modifications to data written to the database will be documented through either the data change system or an inquiry system. Data entered into the database will be retrievable for viewing through the data entry applications. The type of activity that an individual user may undertake is regulated by the privileges associated with his/her user identification code and password.
13.9.4. Data Discrepancy Inquiries and Reports to Core Coordinating Centers
Additional errors will be detected by programs designed to detect missing data or specific errors in the data. These errors will be summarized along with detailed descriptions for each specific problem in Data Query Reports, which will be sent to the Data Managers at the Core Coordinating Centers...
...The Data Manager who receives the inquiry will respond by checking the original forms for inconsistency, checking other sources to determine the correction, modifying the original (paper) form entering a response to the query. Note that it will be necessary for Data Managers to respond to each inquiry received in order to obtain closure on the queried item.

> The Core Coordinating Center and participating site personnel will be responsible for making appropriate corrections to the original paper forms whenever any data item is changed . . . Written documentation of changes will be available via electronic logs and audit trails.
...
Biopsy and biochemistry reports will be sent via e-mail when data are received from the Core Lab.
...
13.9.5. Security and Back-Up of Data
... All forms, diskettes and tapes related to study data will be kept in locked cabinets. Access to the study data will be restricted. In addition, Core Coordinating Centers will only have access to their own center’s data. A password system will be utilized to control access . . . These passwords will be changed on a regular basis. All reports prepared by the DCC will be prepared such that no individual subject can be identified.

> A complete back up of the primary DCC database will be performed twice a month. These tapes will be stored off-site in a climate-controlled facility and will be retained indefinitely. Incremental data back-ups will be performed on a daily basis. These tapes will be retained for at least one week on-site. Back-ups of periodic data analysis files will also be kept. These tapes will be retained at the off-site location until the Study is completed and the database is on file with NIH [National Institutes of Health]. In addition to the system back-ups, additional measures will be taken to back-up and export the database on a regular basis at the database management level...

> 13.9.6. Study status reports
The DCC will send weekly email reports with information on missing data, missing forms, and missing visits. Personnel at the Core Coordinating Center and the Participating Sites should review these reports for accuracy and report any discrepancies to the DCC...
...
13.9.8. Description of Hardware at DCC
A SUN Workstation environment is maintained in the department with a SUN SPARCstation 10 model 41 as the server . . . Primary access to the departments [sic] computing facilities will be through the Internet . . . For maximum programming efficiency, the Oracle database management system and the SAS and BMDP statistical analysis systems will be employed for this study. . . .

> Oracle facilitates sophisticated integrity checks through a variety of mechanisms including stored procedures, stored triggers, and declarative database integrity—for between table verifications. Oracle allows data checks to be programmed once in the database rather than repeating the same checks among many applications . . . Security is enforced through passwords and may be assigned at different levels to groups and individuals.