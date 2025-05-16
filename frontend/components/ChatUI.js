
import { useState, useEffect } from 'react';

export default function ChatUI() {
    const [messages, setMessages] = useState([]);

    useEffect(() => {
        console.log("Connecting to WebSocket...");
        // TODO: Implement real-time WebSocket logic
    }, []);

    const sendMessage = (e) => {
        e.preventDefault();
        const input = e.target.elements.message.value;
        setMessages([...messages, input]);
        e.target.reset();
    };

    return (
        <div>
            <h2>Chat Interface</h2>
            <ul>
                {messages.map((msg, index) => (
                    <li key={index}>{msg}</li>
                ))}
            </ul>
            <form onSubmit={sendMessage}>
                <input type="text" name="message" placeholder="Say something..." />
                <button type="submit">Send</button>
            </form>
        </div>
    );
}
