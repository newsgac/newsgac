feature_descriptions = {
    'direct_quotes' : 'The number of direct quotes within the special opening and closing quote characters within the text',
    # 'remaining_quote_chars' : 'After the removal of direct quotes, the amount of opening and closing quote characters in the remaining text',
    # 'tokens' : 'The number of sequences of characters that are grouped together within the text. In addition to words, includes punctuation, abbreviations and Dutch names',
    'sentences' : 'The number of sentences within the text',
    'avg_sentence_length' : 'The proportion of the number of words with regards to the number of sentences after the removal of direct quotes',
    # 'digits' : 'The number of digits within the text',
    'digits_perc' : 'The percentage of the occurrence of digits with regards to the total number of tokens after the removal of direct quotes',
    # 'currency_symbols' : 'The number of currency symbols within the text',
    'currency_symbols_perc' : 'The percentage of the occurrence of currency symbols with regards to the total number of tokens after the removal of direct quotes',
    # 'exclamation_marks' : 'The number of exclamation marks (!) within the text after the removal of direct quotes',
    'exclamation_marks_perc' : 'The percentage of the occurrence of exclamation_marks with regards to the total number of tokens after the removal of direct quotes',
    # 'question_marks' : 'The number of question marks (?) within the text after the removal of direct quotes',
    'question_marks_perc' : 'The percentage of the occurrence of question marks with regards to the total number of tokens after the removal of direct quotes',
    # 'pronoun_1' : 'The number of first person pronouns (e.g. ik, mij, me) within the text',
    'pronoun_1_perc' : 'The percentage of the occurrence of first person pronouns with regards to the total number of tokens after the removal of direct quotes',
    # 'pronoun_1_perc_rel': 'The percentage of the occurrence of first person pronouns with regards to the total number of pronouns (i.e. sum of first person, second person and third person pronouns) after the removal of direct quotes',
    # 'pronoun_2' : 'The number of second person pronouns (e.g. jij, jouw, jullie) within the text',
    'pronoun_2_perc' : 'The percentage of the occurrence of second person pronouns with regards to the total number of tokens after the removal of direct quotes',
    # 'pronoun_2_perc_rel' : 'The percentage of the occurrence of second person pronouns with regards to the total number of pronouns (i.e. sum of first person, second person and third person pronouns) after the removal of direct quotes',
    # 'pronoun_3' : 'The number of third person pronouns (e.g. hij, zijn, hun) within the text',
    'pronoun_3_perc' : 'The percentage of the occurrence of third person pronouns with regards to the total number of tokens after the removal of direct quotes',
    # 'pronoun_3_perc_rel' : 'The percentage of the occurrence of third person pronouns with regards to the total number of pronouns (i.e. sum of first person, second person and third person pronouns) after the removal of direct quotes',
    # 'adjectives' : 'The number of adjectives in the Part-Of-Speech tagged sentences within the text after the removal of direct quotes',
    'adjectives_perc' : 'The percentage of the occurrence of adjectives with regards to the total number of tokens after the removal of direct quotes',
    # 'modal_verbs' : 'The number of modal verbs (e.g. behoeven, blijken, moeten, etc.) within the text after the removal of direct quotes',
    'modal_verbs_perc' : 'The percentage of the occurrence of modal verbs with regards to the total number of tokens after the removal of direct quotes',
    # 'modal_adverbs' : 'The number of modal adverbs (e.g. allicht, eigenlijk, gelukkig, etc.) within the text after the removal of direct quotes',
    'modal_adverbs_perc' : 'The percentage of the occurrence of modal adverbs with regards to the total number of tokens after the removal of direct quotes',
    # 'intensifiers' : 'The number of intensifiers (e.g. aanmerkelijk, bijna, echt, etc.) within the text after the removal of direct quotes',
    'intensifiers_perc' : 'The percentage of the occurrence of intensifiers with regards to the total number of tokens after the removal of direct quotes',
    # 'cogn_verbs' : 'The number of cognitive verbs (e.g. afleiden, bijna, echt, etc.) within the text after the removal of direct quotes',
    'cogn_verbs_perc' : 'The percentage of the occurrence of cognitive verbs with regards to the total number of tokens after the removal of direct quotes',
    # 'named_entities' : 'The number of named entitites (i.e. names in the text such as location, person, organization, product, etc.) within the text after the removal of direct quotes',
    'named_entities_perc' : 'The percentage of the occurrence of named entities with regards to the total number of tokens after the removal of direct quotes',
    # 'named_entities_pos' : 'The aggregated position of the named entities within the text calculated by taking the proportion of the normalized sum of indexes of the named entities to the total number of tokens after the removal of direct quotes',
    'unique_named_entities' : 'The normalized amount of unique named entities with regards to the number of named entities',
    # 'self_cl_1' : 'Self classification bucket 1 includes genres of nieuwsbericht and nieuwsartikel',
    # 'self_cl_2' : 'Self classification bucket 2 includes genres of interview, tweegesprek, vraaggesprek and interviewen',
    # 'self_cl_3' : 'Self classification bucket 3 includes genres of reportage, sfeerverslag, ooggetuigeverslag, reconstructie and reisverslag',
    # 'self_cl_4' : 'Self classification bucket 4 includes verslag',
    # 'self_cl_5' : 'Self classification bucket 5 includes opiniestuk, commentaar, opinie, betoog, hoofdartikel and betogen',
    # 'self_cl_6' : 'Self classification bucket 6 includes recensie, boekbespreking, filmkritiek, theaterkritiek, filmbespreking and theaterbespreking',
    # 'self_cl_7' : 'Self classification bucket 7 includes nieuwsanalyse, analyse, achtergrond, achtergrondartikel and beschouwing',
    # 'self_cl_8' : 'Self classification bucket 8 includes column, cursiefje and rubriek',
    # 'self_cl_3-4' : 'Self classification bucket 3-4 includes verslag',
    # 'self_cl_3-8' : 'Self classification bucket 3-8 includes kroniek',
    'polarity': 'A value between -1 and +1 calculated based on ws lexicon of adjectives (pattern.nl)',
    'subjectivity': 'A value between 0 and +1 calculated based on ws lexicon of adjectives (pattern.nl)',
    # 'prevailing_tense' : 'The prevailing tense used in the document (-1:past, 0:equal, 1:present)',
    # manually added features
    'article_raw_text' : 'Raw text of the article before pre-processing',
    'data_source_id' : 'The data source uploaded by the user that the article is ws part of',
    'date' : 'Date of the publication of the article',
    'genre' : 'Ground truth for the genre of the article in numeric format',
    'genre_friendly' : 'Ground truth for the genre of the article in ws user friendly text format'
}
features = [
    'direct_quotes',
    # 'remaining_quote_chars',
    # 'tokens',
    'sentences',
    'avg_sentence_length',
    # 'digits',
    'digits_perc',
    # 'currency_symbols',
    'currency_symbols_perc',
    # 'exclamation_marks',
    'exclamation_marks_perc',
    # 'question_marks',
    'question_marks_perc',
    # 'pronoun_1',
    'pronoun_1_perc',
    # 'pronoun_1_perc_rel',
    # 'pronoun_2',
    'pronoun_2_perc',
    # 'pronoun_2_perc_rel',
    # 'pronoun_3',
    'pronoun_3_perc',
    # 'pronoun_3_perc_rel',
    # 'adjectives',
    'adjectives_perc',
    # 'modal_verbs',
    'modal_verbs_perc',
    # 'modal_adverbs',
    'modal_adverbs_perc',
    # 'intensifiers',
    'intensifiers_perc',
    # 'cogn_verbs',
    'cogn_verbs_perc',
    # 'named_entities',
    'named_entities_perc',
    # 'named_entities_pos',
    'unique_named_entities',
    # 'self_cl_1',
    # 'self_cl_2',
    # 'self_cl_3',
    # 'self_cl_4',
    # 'self_cl_5',
    # 'self_cl_6',
    # 'self_cl_7',
    # 'self_cl_8',
    # 'self_cl_3-4',
    # 'self_cl_3-8',
    'polarity',
    'subjectivity',
    # 'prevailing_tense'
]