./user_mood_tag_all.txt
132 mood tags predefined by Livejournal


./user_mood_in_anew.txt
Intersection of 132 LJ mood tags and ANEW vocabulary


./music_emotion_tag_all.txt
190 music-emotion tags defined by AllMusic


./music_emotion_tag_in_anew.txt
Intersection of 190 music-emotion tags and ANEW vocabulary


ANEW:
http://csea.phhp.ufl.edu/media/anewmessage.html




./info/
Entries of LJ2M grouped by the user moods

Each entry is of the form:
<mood>_<article ID>,<user ID>,<original text in music tag>,<artist>,<song title>,<7digital song ID>,<EchoNest track ID>




./music/artist_list.txt
The list of artists in LJ2M


./music/song_list.csv
The list of songs in LJ2M

Each entry is of the form:
<artist>,<song title>


./music/song_list_7digital.csv
The list of songs in LJ2M

Each entry is of the form:
<artist>,<song title>,<7digital song ID>


./music/song_list_echonest.csv
The list of songs in LJ2M

Each entry is of the form:
<artist>,<song title>,<EchoNest track ID>


./music/song_music_emotion_prediction.csv
Music emotion predicted by our classifiers

Each entry is a 190-dim vector corresponding to the music emotion in ./music_emotion_tag_all.txt
Each value in the entry is in [0, 1]


./music/feature_echonest/
EchoNest pitches and timbre features

<EchoNest track ID>.pitch: the pitches feature of EchoNest retrieved from Million Song Dataset
<EchoNest track ID>.timbre: the timbre feature of EchoNest retrieved from Million Song Dataset




./text/word_count_nameremoved_stemming/
Word count with stemming

Remove Person name entity with Stanford Name Entity Recognizer
Index with Indri with krovetz stemming
Remove words appearing in less than 100 articles

Each entry is of the form:
<article ID>,<word ID 0>:<word count 0> <word ID 1>:<word count 1> ... <word ID k>:<word count k> 
See ./text./word_list_noname_stemming.txt for the word list
Word ID starts from 0


./text/word_count_nameremoved_nostemming
Word count without stemming

Remove Person name entity with Stanford Name Entity Recognizer
Index with Indri without stemming
Remove words appearing in less than 100 articles

Each entry is of the form:
<article ID>,<word ID 0>:<word count 0> <word ID 1>:<word count 1> ... <word ID k>:<word count k> 
See ./text/word_list_noname_nostemming.txt for the word list
Word ID starts from 0


./text/LIWC
LIWC2007 features

Output all categories
See LIWC_fields.txt for the field names


Indri:
http://www.lemurproject.org/indri.php

Stanford Name Entity Recognizer:
http://nlp.stanford.edu/software/CRF-NER.shtml

LIWC2007:
http://www.liwc.net/

You can use csv class in Python to read the .csv files


Reference
J.-Y. Liu, S.-Y. Liu and Y.-H. Yang, LJ2M Dataset: Toward better understanding of music-listening and user-mood, IEEE Int. Conf. Multimedia and Expo. (ICME), 2014.
Y.-H. Yang and J.-Y. Liu, Quantitative study of music listening behavior in a social and affective context, IEEE Trans. Multimedia, Special Issue on Social Media as Sensors, volume 15, number 6, pages 1304-1315, October 2013.