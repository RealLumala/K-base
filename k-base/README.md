# Where am I?

- Start your Kovan Local Node & IPFS EA
- Strings can't be passed back from the CL node
- The IPFS EA has just been modified to take a `starting_char` for returning the string

Now we can make 2 calls, to get the feedback from IPFS

Use that, update it so the hash can be stored and be on your merry way!

# TODO

Write a makefile or something to do all this for you. 
# K-BASE

Open Sourced Decentralized Living Community Run Documentation and Software Engineering Support

Front end: React
Blockchain: Eth (ideally Optimism for gas on L2)
Oracle: Chainlink
Database: IPFS

# Design

User comes to site. Types in a question, hits "enter".
THe FE sends a request to create the IPFS [FileCoin](https://proto.school/verifying-storage-on-filecoin/02)

Any questions? Join the Alpha Chain [Discord](https://discord.gg/g6Wfc297Yy)

## License

This project is licensed under the [MIT license](LICENSE).

Local IPFS API Call:

Host your `test.json` object on your IPFS node via the CLI:

```
ipfs add test/test.json
```

```
curl -X POST "http://127.0.0.1:5001/api/v0/block/get?arg=QmW2mDfeUfx6FtQWBQqG67NZTWPpvbPiQB7rvWYq4ZHQ46"
```

To view from the UI, you can do

```
ipfs files ls /
```

# TODO
1. Have someone ask a question (data posted to IPFS)
2. Have someone answer a question (answer posted to IPFS)
3. Main question can accept or deny
4. Give rep




k-base
how does rep work?

User joins, they have to stake rep to post a question and an answer. 


