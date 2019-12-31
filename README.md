# 84000 
# translation-memory-resources

## **CONTENTS**
**I. Documentation** 
1. [Objectives](https://github.com/84000/translation-memory-resources/blob/master/README.md#1-objectives)
2. [Scripts](https://github.com/84000/translation-memory-resources/blob/master/README.md#2-scripts)
3. [Finished TMs](https://github.com/84000/translation-memory-resources/blob/master/README.md#3-finished-tms)

**II. Instructions for TM Editors**
1. [Instructions for Aligning TMs from Pre-Segmented Text Files Using InterText](https://github.com/84000/translation-memory-resources/wiki/TM-Editor-Guidelines#1-instructions-for-aligning-tms-from-pre-segmented-text-files-using-intertext)
2. [TM Standards](https://github.com/84000/translation-memory-resources/wiki/TM-Editor-Guidelines) (from Table of Contents)
# **I. Documentation**

The scripts and documentation here were initially created for 84000’s own workflow, however, all the resources used here are open and available for other organizations or publishers wishing to replicate this methodology for making their own TM resources.

# 1. Objectives:

The purpose of this project is to create simple phrase-by-phrase, English-Tibetan translation memories by aligning 84000's published English translations with the Tibetan source texts found in the eKangyur (based on the Derge edition of the Kangyur). Although, this repository’s workflow is geared for 84000, this methodology is intended to be universal and may be reproduced by any individual or group to be used for their own Tibetan TM projects. Our objective is to (1) create TMs in the form of .tmx files to be used on CAT platforms such as [OmegaT](https://omegat.org/), and (2) create useful data for other digital Tibetan tools and projects such as word alingers, spell checkers, translation machine learning, and perhaps aligning our Tibetan-English segments with segments created by other groups who are creating canonical TMs from Chinese, Sanskrit, or other sources. 

Because of this, it is important that we standardize our process for creating TMs for the best possible degree of consistency. Standards for the TMs in terms of segment length and structure need to be defined in a clear way so that they will be segmented constantly by all the TM editors working on the project. Therefore, [Part II of this documentation](https://github.com/84000/translation-memory-resources/wiki/TM-Editor-Guidelines#1-instructions-for-aligning-tms-from-pre-segmented-text-files-using-intertext) (on the wiki page) contains detailed guidelines for our recommended TM standards.  

All of the TMs that have been gathered at this time are available in the [data-translation-memory repository](https://github.com/84000/data-translation-memory).

For all of the TMs created previously, before 10/01/2019, this had not been the case because the TMs were primarily created with their use for CAT platforms in mind. Although these previous TMs are still very useful for the projects mentioned above, they are not completely ideal because they contain a significant amount of inconsistencies, and additionally they omit repeting segments which make them less useful for machine learning projects. Both of these versions of the TMs are included in the database linked above, but the TMs created without the standards documented here will all be labeled "-v1" and moving forward all the new TMs created according to these new guidelines will be labeled "-v2".

To create the TMs, two text (.txt) files containing the Tibetan-source and English-target respectively are be generated with scripts, and the [InterText](https://wanthalf.saga.cz/intertext) application is used to align the texts and generate the .tmx files. Additionally, InterText generates a set of .xml alignment files, which we are storing in a separate directory, the latter is not useful for translators using CAT platforms, but may be valuable data for future machine learning projects.

# 2. Scripts:

The preprocess.py script used in this repository is set up to convert 84000's published TEI texts into a simple text file and store relevant markup in a tempory .json file. Then TM editors align the text files using InterText and the metadata is re-entered in a suitable format with the postprocess.py script. These scripts are specifically arranged for the tags used in 84000's TEI. For other projects seeking to replicate this methodology, we can arrange to have the scripts adjusted for each project depending on the markup they would like to include in their final TMs. It isn't required to include markup up .tmx files but recording things like folio references, milestones, flags, and identifiers for annotations will make those TMs more useful. At the very least, if there is no desired markup, running the simple [pybo-catscript](https://github.com/Esukhia/cat-scripts) will pre-segment the Tibetan source text according to our model.

The “preprocess.py” script will create an “pre_input” folder for placing the raw text files for both the English and Tibetan. The files generated in the “pre_output” folder will be ready for aligning in InterText. Likewise, when the alignment is completed in InterText the exported .tmx TMs and .xml aligment files should be placed into the "post_out" folders generated by the "postprocess.py" script. Again, these scripts are specifically set up for 84000 publications so any project emulating this methodology should contact @celso-scott to adjust the script according to their project's needs.

## 2.A. Pre-segmentation of eKangyur with the Pybo Script:

The “preprocess.py” script uses [pybo](https://github.com/Esukhia/pybo), a Tibetan word tokenizer, to identify verbs and pre-segment the text from the [eKangyur](https://github.com/Esukhia/derge-kangyur) (note that pybo needs to be installed locally to run the script). This initial segmentation will create a foundational consistency since it follows at set of predetermined rules we have written into the script, although the Tibetan will then need to be further merged/split by the TM editors according to the [TM Guidelines in the wiki](https://github.com/84000/translation-memory-resources/wiki/TM-Editor-Guidelines). 

The outputed Tibetan text includes:

- Word-segmentation created with spaces according to pybo’s tokenization. 
- Sentence-segmentation created with line breaks according to the script’s identification of clauses according to conjugated verbs and a set of rules concerning the particles immediately following those verbs which govern those clauses. 
- Underscores representing the actual spaces found in the Kangyur text.
- Folio references in the eKangyur format, [3a], [3b] etc...

For example:

```
དོན་དམ་པ་ ལ་ མཁས་ [147a]  པ འི་ ཆོས་ དང་ ལྡན་པ་ དང་ །_ མྱ་ངན་ ལས་ འདས་པ འི་ ཆོས་ དང་ ལྡན་པ་ ནི་ མ་ ཡིན་ ནོ ། _ །
ཀྱེ་ རྒྱལ་བ འི་ བུ་ དག་ ཡང་ དེ་བཞིན་ གཤེགས་པ་ དག་ ལ་ མི་ མཁྱེན་པ་ དང་ །_ མི་ གཟིགས་པ འམ །_ མི་ གསན་པ་ དང་ །_ རྣམ་པར་ མི་ མཁྱེན་པ་ ཅུང་ཟད་ ཀྱང་ མི་ མངའ་ སྟེ །_
འོངས་པ་ ཡང་ མཁྱེན །_
མ་འོངས་པ་ ཡང་ མཁྱེན །_
འདས་པ་ ཡང་ མཁྱེན །_
ད་ལྟ ར་ བྱུང་བ་ ཡང་ མཁྱེན །_
```

The preprocess script will ideally cover 60% of the segmentation and the TM editors will refine and edit the TMs based on that. As mentioned, the script follows the same segmentation rules found in the [pybo-catscript](https://github.com/Esukhia/cat-scripts), which is intended be used by translators to presegment any Tibetan text for use on CAT platforms like OmegaT. The hope is that this will optimize TM fuzzy matching for translators since they may use the pybo-catscript as a model for their own segmentation.

[Currently my OmegaT tutorial does not yet explain how and why to use the pybo-catscript, but I will be adding details about this soon. In the near future, I would like to make arrangements to have this script hosted somewhere online, so that translators may run the script on a text file through a simple upload. Although the pybo-catscript is already available now, it requires that translators know how to clone the repository, install Python, install pybo, and run the script].

## 2.A. English Text Generated from 84000 TEI:

The .txt files used for aligning the English translation are generated by the preprocess.py script from [84000’s published TEI](https://github.com/84000/data/tree/master/tei/translations) (Note there are currently two scripts being used to set up the English, contact @Celso-Scott for more details).

The output contains milestones, folio references, and notes; the corresponding ids to the milestones and notes are stored in a .json file while the alignment is being performed in InterText, but will be re-inserted into the final TMs:

- Milestones are represented with $ symbol:  $1, $2, $3, etc. 
- Folio references are represented as: F.2.b, F.3.a, F.3.b etc. (Note that these are to be used for the TM editor's reference, but in the finalized TM records, they will all be removed because they are already accurately located in the Tibetan-source and there may be some disparity between where they are placed in the Tibetan source and where they were placed in the English translation.)
- Notes with their @index preceded by a hashtag “#” symbol: #2, #3, #4, etc. The text file does not include the actual content of the note, the TM editors will instead reference the note section of the 84000 reading room, which correspond to the index used here.  

Single line breaks are placed at the end of each paragraph or stanza, i.e., for every instance of a &lt;/p> or &lt;/lg> found in the TEI.

For example:

```
The Noble Great Vehicle Sūtra
The Question of Kṣemaṅkara
$1 [167.b] Homage to all buddhas and bodhisattvas!
$2 Thus did I hear at one time. The Blessed One was staying in the Nyagrodha Park of the Śākyas, near Kapila
vastu in the Śākya country, together with a great saṅgha of five hundred monks. At that time a Śākya youth#2 
named Kṣemaṅkara set out from the city of Kapilavastu for Nyagrodha Park, where the Blessed One was staying. 
As soon as he arrived there, he touched his head to the feet of the Blessed One and sat down to one side.
```

These two .txt files containing the Tibetan source and English translation may now be sent to the TM editors to create the alignments. TM editors, do not need to be trained to run the scripts but should be trained to focus simply on creating the alignments in InterText.

## 2.C. Scripts to Run on .TMX Files Exported from InterText:

When the alignment is completed in InterText, the completed alignments are generated using the "Export" command. This will export three .xml alignment files, additionally the alignment should be exported as a .tmx file with the "Export texts as --> TMX (stripped markup)" command. 

Both the postprocess-TMX.py and postprocess-XML.py scripts should be run on all of these files in the "post_output" folder generated by the script. As mentioned the script will re-insert all of the id tags for the notes, milestones, and folio references. Additionally the script will clean up the header and create markup for any flags created by the TM editors in InterText (for flags, see details below).  

### Markup

All the final TM's markup will be contained in valid XML markup:
- Milestone references converted to &lt;milestone xml:id=””/>
- Note references converted to &lt;note xml:id=””/>
- Inline Kangyur folio references in the Tibetan converted to &lt;ref folio=””/> (folio references in English are not used).
- One folio reference also added to the node of a &lt;prop name="folio"> element for every segment (recalled from the previous inline folio reference, see below).
- @eft:text-id will be added to the &lt;header> of the .tmx identifying the text’s TEI id.

All of this markup data may be used to link each TM unit to [84000's published TEI](https://github.com/84000/data-tei), and may also be used to link to the milestones, notes, or folio references directly to texts in the [84000 reading room](https://read.84000.co/section/lobby.html).

### Flags

- If a segment has English not translated from the Dege but an alternate Kangyur edition or an alternate language source (Sanskrit, Chinese, etc...)  the TM editors are instructed to add a ! mark to the beginning of the Tibetan segments. The lead editor will then later clarify these flags as markup and possibly add citations into the markup aswell. Usually alternative sources should be declared by the notes, however, this may not always be the case, and sometimes some investigation will be necessary on part of the lead editor.  

- Also, if there are any errors in the English, whether they are typos, omissions with no annotated clarification, or deemed to be incorrect translations by the TM editor, these should be flagged with a % mark at the beginning of the English segment (note that flags for omissions in the English will just be a % mark in the empty English segment). They have also been instructed to enter errors in [a google sheet for editorial review of the TEI as well](https://docs.google.com/spreadsheets/d/14yYoNnVP6AitSvNjaSOyVNHErAttolzVjQDSjd196IA/edit?usp=sharing). The lead editor will then review these when finalizing the TMs, and ostensibly they will be corrected and the flags removed after reviewal.  

Note, these flags will be converted into markup in the exported TMX (see examples in part [3.](https://github.com/84000/translation-memory-resources/blob/master/README.md#markup-2) below), but they could also be left as is within the segment strings, as this scheme would be easy and useful for translators as long as they are aware what the ! and % mean.

### Every Segment to be Marked with a Folio Reference

As with our previous TMs (“-v1.0”), every segment has metadata marking the folio reference; this will be in the form of a &lt;prop/> element e.g.:

> &lt;prop name="folio">F.71.a&lt;/prop>

Not to be confused with the folio references found inline with the Tibetan segments, which mark the actual page turns. This  &lt;prop/> element will appear as a sibling to each translation unit &lt;tu> with the node derived from the previous inline folio reference in the Tibetan, or the current inline one if found in the segment. Thus every segment may be linked to the page on which it is found as our current [TM search tool](http://translator-tools.84000-translate.org/index.html?tab=tibetan-search) demonstrates.

Here is an example translation unit with all these attributes (a flag has been added arbitrarily):

```
<tu>
<prop name="folio">F.143.b</prop>
<eft:flag type="alternateSource">Sanskrit source [citation]</flag>
<tuv xml:lang="en">
<seg><tei:milestone xml:id="UT22084-061-006-214"/><tei:ref folio="143.b"/>Homage to the Omniscient One!</seg>
</tuv>
<tuv xml:lang="bo">
<seg><ref folio="143.b"/>! ཐམས་ཅད་མཁྱེན་པ་ལ་ཕྱག་འཚལ་ལོ། །</seg>
</tuv>
</tu>
```
# 3. Finished TMs:

As mentioned, all of the TMs are in the form of .tmx files and stored in the [data-translation-memory repository](https://github.com/84000/data-translation-memory). A .tmx file uses simple XML markup to align segments of text on the phrase/sentence level (examples will be given below). All of the TMs that were created before 10/01/2019 are also in this format, but were created differently using our [own application](http://translation-memory.84000-translate.org) and used less rigorous standards for defining TM segments. Therefore, we are distinguishing the files by version numbers “-v1.0…” and “v.2.0…”.

The older TMs are still useful resources although they do not follow the same standards. At some point we might consider creating new v.2 TMs to replace them, however, in the meantime, while not completely ideal, they are certainly suitable and should be readily used on CAT platforms and as data for other projects such as machine learning.

The differences between the two versions, their markup format and segment standards, are documented as follows:

## **-v1.0** Created on our Own Application
### Methodology:

When we initially begin segmenting the TMs, since we had not yet defined the segmentation in terms of grammar; the editors were simply instructed to match segments according to wherever they could sensibly make a clean break. They were given the ideal target for creating segments with a length of 10-15 English words or about 10-20 Tibetan syllables. This is the ideal length for a segment because it is long enough to have enough context to be understood but short enough to have a high likelihood of being recalled in a fuzzy match. However, often since the grammar is rearranged in the English, the segments were made to be longer in order to find a clean break. TM editors were told to prioritize accuracy over reaching this ideal segment size. One issue with this is that the English translation often governed the segmentation along side the Tibetan, as it was necessary to find these clean breaks. Rather than this, ideally we want the segmentation to be governed by the Tibetan grammar so that the segmentation is consistent and can be applied universally to new translation projects. 

Another challenge that arose under this first methodology was that there are occasionally passages in the translation based on alternative editions of the Kangyur or alternative language sources. Also there was the case of Toh 100, which was entirely based on the Sanskrit. In such cases the TM editors were told to skip passages that did not matchup to the Tibetan found in the Dege in the eKangyur (In Toh 100 there were actually a lot of text that did match up to the eKangyur, so we went ahead and made the TMs wherever they matched up).

Another shortcoming was that that the TM creation tool had some difficulty reading segments of duplicate strings on the same folio page. Because we were anticipating the TMs just to be used on CAT platforms at the time, TM editors were instructed to skip duplicate strings since that would save time, and a TM of exactly the same string only needs to be entered once in order for it to be recalled on a CAT platform. However, this is less ideal because there are now gaps in that alignment record. I have been told this is not ideal for the data to be used for training machine learning since there is no longer a complete record of the alignment as a bitext. However, for the most part, the majority of the segments from each text are included in the record. 

### Summary of Issues with the Version 1.0 Methodology:
- Segments did not follow any specific grammatical protocols.
- Segmentation was sometimes governed according to English translation in order to make clean breaks. 
- Duplicates were often omitted and so there is not a completed record of the bitext.
- No flags for TMs translated from alternate sources; these were simply skipped if they did not match up to the eKangyur. 

### Markup
These TMs were created using the standard TMX format with some added metadata:
- The Tibetan folio page is marked for each segment in a &lt;prop name="folio"> element, this allows the segment to be linked directly to the page in the eKangyur or English publication, for example in [our own TM search tool](http://translator-tools.84000-translate.org/index.html?tab=tibetan-search).
- The position of the Tibetan string on that folio page was marked with &lt;prop name="position"> representing the character count on that page, however, note that the UI would always read from the first instance of the string on each page, so this is not entirely reliable for duplicate strings. 
- A timestamp and creationid for each TM segment.

Here is a sample of the markup from version -1.0 :

```
<tmx xmlns="http://www.lisa.org/tmx14">
    <header xmlns:eft="http://read.84000.co/ns/1.0" creationtool="84000-translation-memory" creationtoolversion="1.0.0.0" datatype="PlainText" segtype="phrase" adminlang="en" srclang="bo" o-tmf="TEI" creationdate="2018-03-26T16:01:47.493Z" creationid="celso" eft:text-id="UT22084-054-003"/>
    <body>
        <tu tuid="1">
            <prop name="folio">F.153.a</prop>
            <prop name="position">1</prop>
            <tuv xml:lang="bo" creationdate="2018-03-26T16:01:47.493Z" creationid="celso">
                <seg>སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་ལ་ཕྱག་འཚལ་ལོ། །</seg>
            </tuv>
            <tuv xml:lang="en" creationdate="2018-03-26T16:01:47.493Z" creationid="celso">
                <seg>Homage to all buddhas and bodhisattvas!</seg>
            </tuv>
        </tu>
    <!--etc.-->
    </body>
</tmx>
```

## **-v2.0** Using InterText and Following New TM Guidelines.
### Methodology:

InterText is a more efficient application for editing the TM segments. Because we can run the English and Tibetan through scripts ahead of time, we can arrange the Tibetan segmentation to be close to what we want, and then the TM editors just need to align that with the English sentences. This methodology also creates a complete record of [the bitext alignment](https://github.com/84000/translation-memory-resources/blob/master/README.md#xml-alignment-files-generated-by-intertext) because the TM editors need to account for every string of text in both the Tibetan and English including repetitions and translations made from alternate sources. In the latter cases, TM editors will be instructed to flag the beginning of Tibetan segments with a ! character when the English has been translated from a different source. These can then be converted into markup and may be omitted from TMs used on CAT platforms, or if the translator wishes they may still be used since some segments will still be quite close to the Dege source and may still be useful, but they will be able to recognize the flag warning of this discrepancy. The notes and the accompanying index number will be present in the English text and the TM editors will be instructed to check them for possible alternate sources as they are editing the TMs.

With the time and convenience TM editors save using InterText, they will be directed to use the more rigorous TM standards described [on the wiki page](https://github.com/84000/translation-memory-resources/wiki/TM-Editor-Guidelines#2-tm-standards). Under these new guidelines segmentation will be done from the perspective of the Tibetan grammar rather than the English. In cases where the English compounds two Tibetan segments into an intermingled English string, then the TM editors will be instructed to reduplicate that English string and bracket any text that is not represented in the matching Tibetan string. (See the example given for this in [the TM Editor’s Guidelines linked here](https://github.com/84000/translation-memory-resources/wiki/TM-Editor-Guidelines#separating-compounded-english-segments)). With this method, the TM editors will never change or correct the English translation ([although, they may flag errors for review](https://github.com/84000/translation-memory-resources/wiki/TM-Editor-Guidelines#marking-errors)).

Therefore, with this methodology in mind, we hope to improve on the issues that were mentioned in version 1.0 above.

### Summary of Advantages for the Version 2.0 Methodology:
- Segments follow a more consistent standard that is based on the output created by the pybo preprocess script, which will mirror the pybo-catscript to be used by translators.
- Segmentation will be governed by Tibetan grammar and taking cues from the style of the English translation will be avoided. When the English compounds Tibetan segments it may be reduplicated and parsed apart with brackets. This will improve the segmentation’s overall consistency.
- When a .tmx file is exported from InterText, segments with either empty English or Tibetan segments will be excluded from the file. This is ideal for the TMs use in CAT platforms; however, the complete record of the bitext, which includes empty segments due to omissions are included in a separate set of .xml alignment files that will provide more complete data useful for machine learning projects. 
- Flags for TMs translated from alternate sources.
- Flags for errors found in English translation; these will include typos, unannotated omissions or ostensible translation errors to be reviewed by editors.  
- Additional metadata markup will be added to the TMs from the original English TEI including: milestones (along with ids that maybe linked to TEI) and endnotes (especially important for explaining alternate sources).

### Markup:

Some differing features found in version -2.0’s markup:

- &lt;milestone/>, &lt;ref/>, and &lt;note/> elements should be able to appear directly in the segments “&lt;seg/>” but remain hidden on CAT platforms and still be functional (Although I have only tested this with OmegaT and SmartCAT, which have no problems).
- @xml:id in &lt;milestone/> and &lt;note/> corresponds to unique identifier in published 84000 TEI file.
- &lt;flag type="alternateSource"> and &lt;flag type="dubiousTranslation"> added to segments that need to be flagged as such. Ostensibly the latter will be removed once the correction has been confirmed and corrected in the published translation and TM.

Here is a sample of the markup from version -2.0. Note that I have added wordwrap in this example, which should not be included within the segment text strings. I also added some arbitrary &lt;flag/>s to show how this would work when there was a problematic segment:

```
<tmx xmlns="http://www.lisa.org/tmx14" xmlns:eft="http://read.84000.co/ns/1.0" xmlns:tei="http://www.tei-c.org/ns/1.0" version="1.4b">
    <header creationtool="InterText" creationtoolversion="1.0" datatype="PlainText" segtype="block" adminlang="en-us" srclang="bo"
    o-tmf="XML aligned text" eft:text-id="UT22084-061-006"/>
    <body>
        <tu>
            <prop name="folio">F.143.b</prop>
            <tuv xml:lang="bo">
                <seg>ཐམས་ཅད་མཁྱེན་པ་ལ་ཕྱག་འཚལ་ལོ། །</seg>
            </tuv>
            <tuv xml:lang="en">
                <seg><tei:milestone xml:id="UT22084-061-006-16"/>Homage to the Omniscient One!</seg>
            </tuv>
        </tu>
        <tu>
            <prop name="folio">F.143.b</prop>
            <tuv xml:lang="en">
                <seg><tei:milestone xml:id="UT22084-061-006-215"/> Thus did I hear at one time.</seg>
            </tuv>
            <tuv xml:lang="bo">
                <seg>འདི་སྐད་བདག་གིས་ཐོས་པ་དུས་གཅིག་ན། </seg>
            </tuv>
        </tu>
        <tu>
            <prop name="folio">F.143.b</prop>
            <eft:flag type="alternateSource">Segment was translated from the Sanskrit, see note.</flag>
            <tuv xml:lang="en">
                <seg>The Blessed One was dwelling on the banks of the great Nairañjanā River,
                    together with seven thousand bodhisattvas. Among them were the Noble
                    Avalokiteśvara, Vajrapāṇi, Maitreya, and Mañjuśrī, and all the great śrāvakas
                    like Subhūti, Śāriputra, and Maudgalyāyana.<tei:note xml:id="UT22084-061-006-216"
                    /></seg>
            </tuv>
            <tuv xml:lang="bo">
                <seg>བཅོམ་ལྡན་འདས་ཆུ་བོ་ཆེན་པོ་ཀླུང་ནཻ་རཉྫ་ནཱའི་འགྲམ་ན། འཕགས་པ་སྤྱན་རས་
                    གཟིགས་དབང་ཕྱུག་དང་། ལག་ན་རྡོ་རྗེ་དང་། བྱམས་པ་དང་། འཇམ་དཔལ་ལ་སོགས་པ་
                    བྱང་ཆུབ་སེམས་དཔའ་བདུན་སྟོང་དང་། རབ་འབྱོར་དང་། ཤཱ་རིའི་བུ་དང་།
                    མཽད་གལ་གྱི་བུ་ལ་སོགས་པ་ཉན་ཐོས་ཆེན་པོ་ཐམས་ཅད་དང་ཐབས་ཅིག་ཏུ་བཞུགས་ཏེ།</seg>
            </tuv>
        </tu>
        <tu>
            <prop name="folio">F.143.b</prop>
            <eft:flag type="dubiousTranslation"/>
            <!--Segment and English translation need to be reviewed.-->
            <tuv xml:lang="en">
                <seg>He was circumambulated by Śakra, Brahmā, and all the protectors of the world,
                    as well as all the kings, ministers, brahmins, and householders, and was placed 
                    in front of the assembly.</seg>
            </tuv>
            <tuv xml:lang="bo">
                <seg>བརྒྱ་བྱིན་དང་། ཚངས་པ་དང་། འཇིག་རྟེན་སྐྱོང་བ་ཐམས་ཅད་དང་། རྒྱལ་པོ་དང་།
                    བློན་པོ་དང་། བྲམ་ཟེ་དང་། ཁྱིམ་བདག་ཐམས་ཅད་ཀྱིས་བསྐོར་ཅིང་། མདུན་<tei: ref folio="144a"/>དུ་བདར་ཏེ།</seg>
            </tuv>
        </tu>
    </body>
</tmx>
```

## XML Alignment Files Generated by InterText

As was mentioned, InterText also can export the alignment in the form of three .xml files. These files are collected stored in a separate repository because they are not useable on CAT platfroms so translators have no need for them. However, they may be valuable for machine learning projects since they contain segments that omit either English or Tibetan which are omitted in the .tmx, and they contain the original segment order of the English, which may have been rearranged in the .tmx alignment. 

Part II of the documentation containing instructions for TM editors and guidelines for following our recommended TM standard is continued [on the wiki page here:](https://github.com/84000/translation-memory-resources/wiki/TM-Editor-Guidelines#1-instructions-for-aligning-tms-from-pre-segmented-text-files-using-intertext)
