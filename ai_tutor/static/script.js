function handleKeyPress(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
}

function sendMessage() {
    let userInput = document.getElementById("user-input").value;
    if (userInput.trim() === "") return;

    let chatBox = document.getElementById("chat-box");
    let userMessage = `<div class="message-box user-message"><strong>You:</strong> ${userInput}</div>`;
    chatBox.innerHTML += userMessage;

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: userInput })
    })
    .then(response => response.json())
    .then(data => {
        let aiMessage = `<div class="message-box ai-message"><strong>AI:</strong> ${formatText(data.response)}</div>`;
        chatBox.innerHTML += aiMessage;
        document.getElementById("videoFrame").src = data.video_url;

        speakResponse(data.response);

        document.getElementById("user-input").value = "";
        chatBox.scrollTop = chatBox.scrollHeight;
    });
}

function startVoiceInput() {
    let recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = "en-US";

    recognition.onresult = function(event) {
        let userInput = event.results[0][0].transcript;
        document.getElementById("user-input").value = userInput;
        sendMessage();
    };

    recognition.start();
}

function speakResponse(text) {
    let speech = new SpeechSynthesisUtterance(text);
    speech.lang = "en-US";
    speech.pitch = 1;
    speech.rate = 1;
    speech.volume = 1;
    window.speechSynthesis.speak(speech);
}

function formatText(text) {
    return text.replace(/\*\*(.*?)\*\*/g, '<span class="bold">$1</span>').replace(/\n/g, '<br>');
}

window.onload = function() {
    speakResponse("Hello! What topic would you like to study today?");
};

