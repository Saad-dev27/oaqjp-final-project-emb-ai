"""
Emotion Detection application using IBM Watson NLP API.
"""

import requests

API_URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)

HEADERS = {
    "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
}


def emotion_detector(text):
    """
    Analyze text and return five emotion scores
    and the dominant emotion.
    """

    empty_result = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
    }

    if not isinstance(text, str) or not text.strip():
        return empty_result

    payload = {
        "raw_document": {
            "text": text
        }
    }

    try:
        response = requests.post(
            API_URL,
            json=payload,
            headers=HEADERS,
            timeout=30
        )

        response.raise_for_status()
        result = response.json()

        emotions = result["emotionPredictions"][0]["emotion"]

        scores = {
            "anger": emotions["anger"],
            "disgust": emotions["disgust"],
            "fear": emotions["fear"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"]
        }

        scores["dominant_emotion"] = max(
            scores,
            key=scores.get
        )

        return scores

    except (
        requests.exceptions.RequestException,
        ValueError,
        KeyError,
        IndexError,
        TypeError
    ):
        return empty_result
