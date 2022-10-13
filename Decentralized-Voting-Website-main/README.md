# Decentralized Voting


The project is based on developing a decentralized application (Dapp) for electoral polling
systems. It allows voters and administrators to organize voting in a decentralized manner
(without depending on a single administrative body). The electoral polling dapplication developed in this project is based on the ethereum blockchain
technology. 

## Tech Stack 
1. Frontend - CSS, JS
2. Backend - Node, Truffle 
3. Local Blockchain - Ganache, Metamask
4. Smart contracts - Solidity

## Configure code on your system

1. Clone the repo 

```
git clone https://github.com/pandeyanuradha/Decentralized-Voting-Website.git
cd Decentralized-Voting-Website
```

2. Run local Ethereum on Command Line Interface (CLI)

```
ganache-cli
```

3. Configure Metamask on your browser

New RPC URL: http://localhost:8545 <br />
Chain ID: 1337

4. Import accounts using Private keys from ganache-cli to Metamask
5. Deploy smart contract  
```
truffle migrate
````
6. Launch the development server
```
cd client
npm install
npm start
```

## Working of Decentralized Voting Website

1. Ganache workspace
 
<img src="https://github.com/pandeyanuradha/Decentralized-Voting-Website/blob/b5c495190ebf4219b5faafa9676e15ae6847fbc4/images/image3.png" height = "350" width="650" />

2. Admin will create a voting instance by launching/deploying the system in a blockchain network (EVM), then create an election instance and start the election with the details of the election filled in (including candidates for voters to vote). On startup, the homepage is displayed.

<img src="https://github.com/pandeyanuradha/Decentralized-Voting-Website/blob/b5c495190ebf4219b5faafa9676e15ae6847fbc4/images/image8.png" height = "350" width="650" />
<img src="https://github.com/pandeyanuradha/Decentralized-Voting-Website/blob/b5c495190ebf4219b5faafa9676e15ae6847fbc4/images/image3.png" height = "350" width="650" />

3. Metamask deduction for admin.

<img src="https://github.com/pandeyanuradha/Decentralized-Voting-Website/blob/b5c495190ebf4219b5faafa9676e15ae6847fbc4/images/image6.png" height = "450" width="650" />

4. Add candidates

<img src="https://github.com/pandeyanuradha/Decentralized-Voting-Website/blob/b5c495190ebf4219b5faafa9676e15ae6847fbc4/images/image2.png" height = "350" width="650" />

5. The voters can register through the registration portal

<img src="https://github.com/pandeyanuradha/Decentralized-Voting-Website/blob/b5c495190ebf4219b5faafa9676e15ae6847fbc4/images/image5.png" height = "350" width="650" />

6. Admin approves the voter

<img src="https://github.com/pandeyanuradha/Decentralized-Voting-Website/blob/b5c495190ebf4219b5faafa9676e15ae6847fbc4/images/image9.png" height = "350" width="650" />

7. Cast their votes

<img src="https://github.com/pandeyanuradha/Decentralized-Voting-Website/blob/b5c495190ebf4219b5faafa9676e15ae6847fbc4/images/image4.png" height = "350" width="650" />

8. After some time, depending on the scale of the election the admin ends the election. As that happens the voting is closed and the results are displayed announcing the winner at the top of the results page. Election Results are displayed.

<img src="https://github.com/pandeyanuradha/Decentralized-Voting-Website/blob/b5c495190ebf4219b5faafa9676e15ae6847fbc4/images/image1.png" height = "350" width="650" />





 
