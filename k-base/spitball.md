MVP:

User posts question, they get kbase token
User answers question, they stake answer
User answer gets accepted, they get the token
User question gets rejected, they lose stake

Data is stored on IPFS. 



1. Store tokenURIs that point to something like IPFS
With Qs, As, Rep, Etc
Only change tokenURIs when governance passes or something. 
Your edits and changes are stored on your IPFS node, until "merged" into the IPFS "main" node? 

Use something like filecoin. Miners store the data, chainlink node is used to propogate and update on-chain stuff like rep from the files stored off-chain. 

Front-End: React
Blockchain: EVM Chain
Oracle: Chainlink (Connects Blockchain to Data Storage)
Database: IPFS
