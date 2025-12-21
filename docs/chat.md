---
id: chat
title: RAG Chat
---

import React, { useState } from 'react';

export default function Chat() {
  const [question, setQuestion] = useState('');
  const [answers, setAnswers] = useState([]);
  const [loading, setLoading] = useState(false);

  const askQuestion = async () => {
    setLoading(true);
    setAnswers([]);

    const res = await fetch('http://localhost:8000/ask', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ question })
    });

    const data = await res.json();
    setAnswers(data.answers);
    setLoading(false);
  };

  return (
    <div>
      <h1>Ask a Question</h1>
      <input
        type="text"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Type your question here..."
      />
      <button onClick={askQuestion} disabled={loading}>
        {loading ? "Loading..." : "Ask"}
      </button>
      <div>
        {answers.map((a, i) => (
          <p key={i}>{a}</p>
        ))}
      </div>
    </div>
  );
}
