
# Chavrick Bot - Self-Learning Web3 AI (Solana Mainnet Edition)
 
An on-chain, self-learning chatbot powered by AI and Web3. Chavrick Bot continuously evolves by learning from user interactions and storing conversations on Solana mainnet. No token reward mechanism is included; interactions are purely on-chain.

## Project Structure

```
chavrick-bot/
├── README.md                # Project overview
├── bot-engine/
│   ├── main.py              # Main AI engine code
│   ├── memory.py            # In-memory message processing
│   └── onchain_storage.py   # Solana storage logic (Anchor / PDA-based)
├── contracts/
│   └── ChavrickBot.rs       # Solana smart contract for on-chain learning
├── web3/
│   ├── client.js            # Solana.js integration with WebSocket support
│   └── utils.js             # Common Web3 utilities (RPC, WebSocket, API)
├── env/
│   └── .env                 # Environment variables (WSS, RPC, API keys)
├── tests/
│   ├── contract_tests.js    # Smart contract unit tests
│   └── integration_tests.py # Full system integration tests
├── frontend/
│   ├── pages/
│   │   └── index.js         # Main React/Next.js app
│   └── components/
│       └── ChatUI.js        # Chat interface
├── docs/
│   └── ARCHITECTURE.md      # Detailed architecture and flow
└── LICENSE                  # MIT License file
```

## License
MIT License
