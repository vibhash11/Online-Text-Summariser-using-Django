# -*- coding: utf8 -*-

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from collections import defaultdict
from ..nlp.stemmers import null_stemmer
from ._summarizer import AbstractSummarizer
from .edmundson_cue import EdmundsonCueMethod
from .edmundson_key import EdmundsonKeyMethod
from .edmundson_title import EdmundsonTitleMethod
from .edmundson_location import EdmundsonLocationMethod


class EdmundsonSummarizer(AbstractSummarizer):


    def __init__(self, stemmer=null_stemmer, cue_weight=1.0, key_weight=0.0,
            title_weight=1.0, location_weight=1.0):
        super(EdmundsonSummarizer, self).__init__(stemmer)

        self._ensure_correct_weights(cue_weight, key_weight, title_weight,
            location_weight)

        self._cue_weight = float(cue_weight)
        self._key_weight = float(key_weight)
        self._title_weight = float(title_weight)
        self._location_weight = float(location_weight)

    def _ensure_correct_weights(self, *weights):
        for w in weights:
            if w < 0.0:
                raise ValueError("Negative wights are not allowed.")

    def __call__(self, document, sentences_count):
        ratings = defaultdict(int)

        if self._cue_weight > 0.0:
            method = self._build_cue_method_instance()
            ratings = self._update_ratings(ratings, method.rate_sentences(document))
        if self._key_weight > 0.0:
            method = self._build_key_method_instance()
            ratings = self._update_ratings(ratings, method.rate_sentences(document))
        if self._title_weight > 0.0:
            method = self._build_title_method_instance()
            ratings = self._update_ratings(ratings, method.rate_sentences(document))
        if self._location_weight > 0.0:
            method = self._build_location_method_instance()
            ratings = self._update_ratings(ratings, method.rate_sentences(document))

        return self._get_best_sentences(document.sentences, sentences_count, ratings)

    def _update_ratings(self, ratings, new_ratings):
        assert len(ratings) == 0 or len(ratings) == len(new_ratings)

        for sentence, rating in new_ratings.items():
            ratings[sentence] += rating

        return ratings

