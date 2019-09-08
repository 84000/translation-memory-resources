[Using markdown syntax, but staging here for editing, suggestions, and comments.] 

# 84000 
# translation-memory-resources

**CONTENTS**
1. [Objectives](https://github.com/84000/translation-memory-resources/blob/master/README.md#1-objectives)
2. [Scripts](https://github.com/84000/translation-memory-resources/blob/master/README.md#2-scripts)
3. [Finished TMs](https://github.com/84000/translation-memory-resources/blob/master/README.md#3-finished-tms)
4. [Instructions for TM Editors](https://github.com/84000/translation-memory-resources/blob/master/README.md#4-instructions-for-tm-editors)
5. [TM Standards](https://github.com/84000/translation-memory-resources/blob/master/README.md#5-tm-standards)
6. [License](https://github.com/84000/translation-memory-resources/blob/master/README.md#6-license)

[1-3,6 will be in the README, 4-5 will be in the README as links to the wiki, then put all the 4) Instructions for TM editors and 5) TM standards as separate wiki pages. Mainly because I want to link TM editors directly to instructions and ignore all the technical aspects.]  

# 1. Objectives:

The purpose of this project is to create simple phrase-by-phrase, English-Tibetan translation memories by aligning 84000's published English translations with the Tibetan source texts found in the eKangyur (based on the Derge edition of the Kangyur). Our objective is to (1) create TMs as a resource to used on CAT platforms such as [OmegaT](link), and (2) create useful data for other digital Tibetan tools and projects such as word alingers, spell checkers, translation machine learning, and perhaps aligning our Tibetan-English segments with segments created by other groups who are creating canonical TMs from Chinese, Sanskrit, or other sources.

Because of this, it is important that we standardize our process for creating TMs for the best possible degree of consistency. Standards for the TMs in terms of segment length and structure need to be defined in a clear way so that they will be segmented constantly by all the TM editors working on the project. Also the TMs for each text need to be complete and contain all strings of the English and Tibetan texts including repetitions and strings that are omitted in either the source or target, although the latter can be removed from the TMs for use in CAT platforms.

For all of the TMs created previously, before 9/01/2019, this had not been the case because the TMs were mainly created primarily with their use with CAT tools in mind. Although these previous TMs may still be useful data for the other projects mentioned above, they are not ideal because they contain a significant amount of omissions and inconsistencies. These previous versions will all be labeled -v1.0… and all the TMs created according to these new guidelines will be labeled -v2.0...

To align the Tibetan-source and English-target two text (.txt) files will be generated with scripts and [InterText](link) application will be used to actually create the alignment and generate the .tmx files.

# 2. Scripts:

The “preprocess.py” script will create an “input” folder for placing the raw text files for both the English and Tibetan. The files generated in the “output” folder will be ready for aligning in InterText.  
## 2.A. Tibetan eKangyur Text Segmented with Pybo:

Using [pybo](link), the script, “preprocess.py” has been customized for pre-segmenting the Tibetan and will be used to generate a Tibetan .txt file from [eKangyur](link). Each segment will be formatted with line breaks. This will provide a foundational consistency since it follows some predetermined rules, although the Tibetan may then be further merged/split by the TM editors according to the guidelines below (4.A-C). 

The Tibetan includes:

- word segmentation created with spaces according to pybo’s bo tokenization. 
- underscores representing the actual spaces found in the Kangyur text.
- folio references in the eKangyur format, [3a], [3b] etc...
- line references in the eKangyur format, [3a.1], [3a.2] etc...

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
- <head> elements should not be included. 

Single line breaks should be placed at the end of each paragraph or stanza, i.e., for every instance of a </p> or </lg> found in the TEI.

For example:
> <milestone UT22084-061-006-16> <ref F.143.b> Homage to the Omniscient One! <milestone UT22084-061-006-17>
Thus did I hear at one time. The Blessed One was dwelling on the banks of the great Nairañjanā River, together with seven thousand bodhisattvas. Among them were the Noble Avalokiteśvara, Vajrapāṇi, Maitreya, and Mañjuśrī, and all the great śrāvakas like Subhūti, Śāriputra, and Maudgalyāyana. He was circumambulated by Śakra, Brahmā, and all the protectors of the world, as well as all the kings, ministers, brahmins, and householders, and was <ref F.144.a> placed in front of the assembly. After being presented with offerings of almsfood, he pleased his surrounding retinue with a teaching on Dharma, and encouraged, uplifted, and complimented them. By means of his great supernatural power, the Tathāgata and his surrounding retinue were then transported to the city of Vārāṇasī, where they stayed in the grove of the caretaker of mango trees.<note #2 UT22084-061-006-214> <milestone UT22084-061-006-18> At that time the earth trembled greatly,

This exported .txt should then be placed in the import folder created by the “preprocess.py” script. The ids will then be stripped and saved in the “tmp” folder while the texts are being aligned in InterText. They will then be reinserted in the final .tmx file.
## 2.C. Scripts to Run on .TMX Files Exported from InterText:

Still need to see how the .TMX will be exported from InterText and configure the final form of .TMX

In our previous TMs (“-v1.0”), the folio numbers were put into elements, e.g.:

> <prop name="folio">F.71.a</prop>

These were siblings to the actual <seg>s in the .tmx; however, this does not mark the folio ref’s position in the segment string.
# 3. Finished TMs:

[Document the previous versions “-1.0” vs. current “-2.0”, all the metadata, and how they are to be used with OmegaT and 84000’s TM search tool.]
# 4. Instructions for TM Editors:

[This section just instructions for how to use InterText. I will link to the relevant chapters of the online PDF of the InterText guied, or also make a short screencast, as the InterText guide is a bit wordy and the TM editors don’t need to read it all]

[The following section will contain the more critical instructions for how to determine the segments themselves.]

# 5. TM Standards

In order to make the TMs an optimal resource for using on CAT platforms and for machine learning, it is important to clearly define what makes a single segment of Tibetan so that they may be created in a consistent way when they are created by different TM editors.

This creates some unique challenges because **(A)** Tibetan doesn’t contain a consistent punctuation character that could be used to define segments, and **B)** differing styles in the English used by different translators will cause the matching English to be inconsistently compound verbs, phrases, and conjunctions in the Tibetan, making it very difficult to make clean breaks between segments according to a consistent set of rules. 

There has been some discussion about whether TM editors should **(1)** be given an abstract set of rules and match segments to those as best they can, or **(2)** re-edit the English to match the Tibetan according to a more rigorous set of standards. 

The advantages of the first option, (1) are that TMs can be produced much more quickly; they will match the original translation; and the TMs can be targeted toward a certain character length, for example, a 10-20 syllable ideal can be set, and larger segments can be broken down wherever cleanly possible until they reach that ideal length or get as close as possible. 

The second option, (2) would have the advantage of being able to follow a more rigorous standard based solely on the Tibetan grammar, but this would require more skill and time on part of the TM editors, and the result would have to be effectively re-translated for many passages in order to fit the English into the Tibetan segments.


## 5.A Editing Tibetan Segmentation:

Since the basic structure of a Tibetan phrase is subject-object-verb, the final verb is the best foundation for delimiting a Tibetan segment. The pybo-script basically does this by identifying final verbs. Its basic rules for segmentation are as follows:

-A segment break is created after a verb followed by a *shad* ། ending.
-A segment break is created after a completion particle (རྫོགས་ཚིག) followed by a *shad* ། ending.
-A segment break is *not* created after a nominalized verb. (+པ་/བ་/པར་ etc...)
-A segment break is created after a verb followed by a ན་  which will usually be a conditional conjunction (cases where it is not will need manual correction).
-A segment break is created after a verb followed by a ནས་ which will usually be a sequential conjunction (cases where it is not will need manual correction).
-A segment break is created after a verb followed by a continuative particle (ལྷག་བཅས་ = སྟེ་/ཏེ་/དེ་ )

### 5.A.i Defining the Tibetan Segment:

### 5.A.ii When the Tibetan Segments May Be Split:

### 5.A.iii When the Tibetan Segments Need to Be Merged:

## 5.B. Editing English Segmentation:

### 5.B.i Changing the Sentence Order in the English:

### 5.B.ii Words or Phrases Omitted or Added within the English Translation:

### 5.B.iii Alternative Sources:

### 5.B.iv Punctuation:

### 5.B.v Conjunctions “and” and “but” translated for “ནས་” “ལས་” and similar particles:

### 5.B.vi Prepositions

### 5.B.vii Verses

### 5.B.viii Judgment Calls









