from setuptools import setup, find_packages

setup(
    name="EmotionDetection",
    version="0.0.1",
    description="Emotion Detection Application using IBM Watson NLP",
    packages=find_packages(),
    install_requires=["requests"],
    python_requires=">=3.8"
)
