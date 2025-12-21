import React from 'react';
import Layout from '@theme/Layout';

export default function ChatbotPage() {
  return (
    <Layout title="Physical AI Chatbot" description="Ask questions about the textbook!">
      <div style={{ textAlign: 'center', marginTop: '20px' }}>
        <h1>Physical AI Textbook Chatbot</h1>
        <p>Ask anything about the textbook chapters (1-9).</p>

        {/* Iframe embedding Streamlit app */}
        <iframe
          src="https://physical-ai-book.streamlit.app/"
          style={{ width: '100%', height: '800px', border: 'none' }}
          title="Textbook Chatbot"
        />
      </div>
    </Layout>
  );
}
