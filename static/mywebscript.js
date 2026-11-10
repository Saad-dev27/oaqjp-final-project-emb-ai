async function RunSentimentAnalysis() {

    const textToAnalyze =
        document.getElementById("textToAnalyze").value.trim();

    const responseElement =
        document.getElementById("system_response");

    if (!textToAnalyze) {
        responseElement.innerText =
            "Please enter some text for emotion detection.";
        return;
    }

    responseElement.innerText = "Analyzing customer feedback...";

    try {
        const response = await fetch(
            `/emotionDetector?textToAnalyze=${encodeURIComponent(textToAnalyze)}`
        );

        const result = await response.text();

        responseElement.innerText = result;

    } catch (error) {
        responseElement.innerText =
            "An error occurred while connecting to the server.";
    }
}
