# Chavrick Bot

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
├── frontend/
│   ├── pages/
│   │   └── index.js         # Main React/Next.js app
│   └── components/
│       └── ChatUI.js        # Chat interface
├── env/
│   └── .env                 # Environment variables (WSS, RPC, API keys)
├── tests/
│   ├── contract_tests.js    # Smart contract unit tests
│   └── integration_tests.py # Full system integration tests
├── docs/
│   └── ARCHITECTURE.md      # Detailed architecture and flow
└── LICENSE                  # MIT License file
```

## Key Features

- **Self-Learning:** Learns from user interactions stored on-chain (Solana PDA-based).
- **Web3 Integration:** Connects directly with Phantom, Solflare, or other Solana wallets.
- **On-Chain Memory:** Stores conversation history and message scores on Solana.
- **Real-time Updates:** Uses WebSockets for instant message syncing.
- **Modular Design:** Easily extendable with new features like DeFi trading, NFT management, and DAO voting.

## Getting Started

### Installation

```bash
git clone https://github.com/<your-username>/chavrick-bot.git
cd chavrick-bot
npm install
```

### Smart Contract Deployment

```bash
cd contracts
anchor build
anchor deploy --provider.cluster mainnet
```

### Environment Setup

Create a `.env` file in the `env/` directory with the following variables:

```
WSS_ENDPOINT=wss://api.mainnet-beta.solana.com
RPC_ENDPOINT=https://api.mainnet-beta.solana.com
API_KEY=your-api-key
```

### Running the Bot

```bash
cd bot-engine
python3 main.py
```

### Frontend

```bash
cd frontend
npm run dev
```
