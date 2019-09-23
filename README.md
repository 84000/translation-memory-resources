# 84000 
# translation-memory-resources

## **CONTENTS**
**I. Documentation** 
1. [Objectives](https://github.com/84000/translation-memory-resources/blob/master/README.md#1-objectives)
2. [Scripts](https://github.com/84000/translation-memory-resources/blob/master/README.md#2-scripts)
3. [Finished TMs](https://github.com/84000/translation-memory-resources/blob/master/README.md#3-finished-tms)

**II. Instructions for TM Editors**
1. [Instructions for Aligning TMs from Pre-Segmented Text Files Using InterText](https://github.com/84000/translation-memory-resources/wiki/TM-Editor-Guidelines#1-instructions-for-aligning-tms-from-pre-segmented-text-files-using-intertext)
2. [TM Standards](https://github.com/84000/translation-memory-resources/wiki/TM-Editor-Guidelines#2-tm-standards)
# **I. Documentation**

# 1. Objectives:

The purpose of this project is to create simple phrase-by-phrase, English-Tibetan translation memories by aligning 84000's published English translations with the Tibetan source texts found in the eKangyur (based on the Derge edition of the Kangyur). Our objective is to (1) create TMs as a resource to used on CAT platforms such as [OmegaT](https://omegat.org/), and (2) create useful data for other digital Tibetan tools and projects such as word alingers, spell checkers, translation machine learning, and perhaps aligning our Tibetan-English segments with segments created by other groups who are creating canonical TMs from Chinese, Sanskrit, or other sources.

Because of this, it is important that we standardize our process for creating TMs for the best possible degree of consistency. Standards for the TMs in terms of segment length and structure need to be defined in a clear way so that they will be segmented constantly by all the TM editors working on the project. Also the TMs for each text need to be complete and contain all strings of the English and Tibetan texts including repetitions and strings that are omitted in either the source or target, although the latter can be removed from the TMs for use in CAT platforms.

For all of the TMs created previously, before 9/01/2019, this had not been the case because the TMs were mainly created primarily with their use with CAT tools in mind. Although these previous TMs may still be useful data for the other projects mentioned above, they are not ideal because they contain a significant amount of omissions and inconsistencies. These previous versions will all be labeled -v1.0… and all the TMs created according to these new guidelines will be labeled -v2.0...

To align the Tibetan-source and English-target two text (.txt) files will be generated with scripts and [InterText](https://wanthalf.saga.cz/intertext) application will be used to actually create the alignment and generate the .tmx files.

# 2. Scripts:

The “preprocess.py” script will create an “input” folder for placing the raw text files for both the English and Tibetan. The files generated in the “output” folder will be ready for aligning in InterText.  
## 2.A. Tibetan eKangyur Text Segmented with Pybo:

Using [pybo](https://github.com/Esukhia/pybo), the script, “preprocess.py” has been customized for pre-segmenting the Tibetan and will be used to generate a Tibetan .txt file from [eKangyur](https://github.com/Esukhia/derge-kangyur) (note that pybo will need to be installed locally to run the script). Each segment will be formatted with line breaks. This will provide a foundational consistency since it follows some predetermined rules, although the Tibetan may then be further merged/split by the TM editors according to the guidelines below (4.A-C). 

The Tibetan includes:

- word segmentation created with spaces according to pybo’s bo tokenization. 
- underscores representing the actual spaces found in the Kangyur text.
- folio references in the eKangyur format, [3a], [3b] etc...

For example:
> དོན་དམ་པ་ ལ་ མཁས་ [147a]  པ འི་ ཆོས་ དང་ ལྡན་པ་ དང་ །_ མྱ་ངན་ ལས་ འདས་པ འི་ ཆོས་ དང་ ལྡན་པ་ ནི་ མ་ ཡིན་ ནོ །_།
ཀྱེ་ རྒྱལ་བ འི་ བུ་ དག་ ཡང་ དེ་བཞིན་ གཤེགས་པ་ དག་ ལ་ མི་ མཁྱེན་པ་ དང་ །_ མི་ གཟིགས་པ འམ །_ མི་ གསན་པ་ དང་ །_ རྣམ་པར་ མི་ མཁྱེན་པ་ ཅུང་ཟད་ ཀྱང་ མི་ མངའ་ སྟེ །_
འོངས་པ་ ཡང་ མཁྱེན །_
མ་འོངས་པ་ ཡང་ མཁྱེན །_
འདས་པ་ ཡང་ མཁྱེན །_
ད་ལྟ ར་ བྱུང་བ་ ཡང་ མཁྱེན །_
## 2.A. English Text Generated from 84000 TEI:

Note that before the English may be processed by the “preprocess.py” script. Another script needs to be set up to generate the English .txt file for alignment using [84000’s published TEI](link).

The output should contain the milestones, folio references, and notes contained in simple angular brackets including their relevant ids separated by spaces: 

- Milestones along with their @xml:id, e.g.:  <milestone UT22084-061-006-16>
- Folio references along with their @cRef, e.g.: <ref F.143.b>
- Notes with their @index preceded by a hashtag “#” symbol, as well as their @xml:id, e.g.: <note #2 UT22084-061-006-214>
- But do *not* include the actual content of the note, the TM editors will instead reference the note section of the 84000 reading room.  
- <head> elements should be included. For now, as I am noticing that some of the English in the <head> is indeed a translation of the Tibetan and sometimes it is an interjection of the translator’s outline. The solution to this is to include all of them and instruct TM editors to match interjected English headings with blank entries for the Tibetan.

Single line breaks should be placed at the end of each paragraph or stanza, i.e., for every instance of a </p> or </lg> found in the TEI.

For example:
> <milestone UT22084-061-006-16> <ref F.143.b> Homage to the Omniscient One! <milestone UT22084-061-006-17>
Thus did I hear at one time. The Blessed One was dwelling on the banks of the great Nairañjanā River, together with seven thousand bodhisattvas. Among them were the Noble Avalokiteśvara, Vajrapāṇi, Maitreya, and Mañjuśrī, and all the great śrāvakas like Subhūti, Śāriputra, and Maudgalyāyana. He was circumambulated by Śakra, Brahmā, and all the protectors of the world, as well as all the kings, ministers, brahmins, and householders, and was <ref F.144.a> placed in front of the assembly. After being presented with offerings of almsfood, he pleased his surrounding retinue with a teaching on Dharma, and encouraged, uplifted, and complimented them. By means of his great supernatural power, the Tathāgata and his surrounding retinue were then transported to the city of Vārāṇasī, where they stayed in the grove of the caretaker of mango trees.<note #2 UT22084-061-006-214> <milestone UT22084-061-006-18> At that time the earth trembled greatly,

This exported .txt should then be placed in the import folder created by the “preprocess.py” script. The ids will then be stripped and saved in the “tmp” folder while the texts are being aligned in InterText. They will then be reinserted in the final .tmx file.
## 2.C. Scripts to Run on .TMX Files Exported from InterText:

[Still need to see how the .TMX will be exported from InterText and configure the final form of .TMX what follows are some general principles that I am mentioning as a draft.]

### Markup

- Milestones converted to <milestone xml:id=””/>
- Notes converted to <note xml:id=””/>
- References in both Tib and Eng to <ref folio=””/>
- Some markup at the root element or body identifying the actual text’s TEI id

### Flags

- If a segment has English not translated from the Dege but an alternate Kangyur edition or an alternate language source (Sanskrit, Chinese, etc...)  the TM editors are instructed to add a ! mark to the beginning of the Tibetan segments. The lead editor will then later clarify these flags as markup and possibly add citations into the markup aswell. Usually alternative sources should be declared by the notes, however, this may not always be the case, and sometimes some investigation will be necessary on part of the lead editor.  

-Also, if there are any errors in the English, whether they are typos, omissions with no annotated clarification, or deemed to be incorrect translations by the TM editor, these should be flagged with a % mark at the beginning of the English segment (note that flags for omissions in the English will just be a % mark in the empty English segment). They have also been instructed to enter errors in [a google sheet for editorial review of the TEI as well](https://docs.google.com/spreadsheets/d/14yYoNnVP6AitSvNjaSOyVNHErAttolzVjQDSjd196IA/edit?usp=sharing). The lead editor will then review these when finalizing the TMs. 

Note, these flags may be converted into markup in the exported TMX, but they could also be left as is within the segment strings, as this scheme would be easy and useful for translators as long as they are aware what the ! and % mean.

In our previous TMs (“-v1.0”), the folio numbers were put into elements, e.g.:

> <prop name="folio">F.71.a</prop>

These were siblings to the actual <seg>s in the .tmx appearing not inside the segments but as an element marking up each translation unit <tu>; These are essential for allowing the TM search tool to link to the page in the reading room as -v1.0 has no milestone markers. It would probably be best if all the references that mark the actual page turns remained present in the segment strings: <ref folio=”11.a”/> but then also have the most recent folio ref marked as the <prop> element in every tu 

Here is an example translation unit with all these attributes (flag has been added arbitrarily):

> <tu>
<prop name="folio">F.143.b</prop>
<flag type="alternateSource">Sanskrit source [citation]</flag>
<tuv xml:lang="en">
<seg><milestone xml:id="UT22084-061-006-214"/> <ref folio="143.b"/> Homage to the Omniscient One!</seg>
</tuv>
<tuv xml:lang="bo">
<seg><ref folio="143.b"/> ཐམས་ཅད་མཁྱེན་པ་ལ་ཕྱག་འཚལ་ལོ། །</seg>
</tuv>
</tu>


# 3. Finished TMs:

[Document the previous versions “-1.0” vs. current “-2.0”, all the metadata, and how they are to be used with OmegaT and 84000’s TM search tool.]

## **-v1.0**

## **-v2.0**
- <milestone/>, <ref/>, and <note/> elements should be able to appear directly in the segments “<seg/>” but remain hidden on CAT platforms and still be functional (though I have only tested with OmegaT so far).

- @xml:id in <milestone/> and <note/> corresponds to unique identifier in published 84000 TEI file.










