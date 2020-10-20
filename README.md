# i-Voting

Secure, trustful and anonymity backend internet voting protocol and implantation POC

## How it works?

Main server - This server controlled by the country. It sign up the Citizen who wants to vote and authenticate them

Ballot - The server where the Citizen is voting. Listen for votes and send back the votes to the server in the end of the election. This server can be one or more of the following: party server/citizen computer/private companies.   

Citizen - The user who vote

### Before the election day

Ballots are listed in the main server

The citizen generates public and private keys. He authenticate to the main server. The public key used for identification by Ballot. The citizen gets x numbers of IPs of Ballots.

### When the election day starts

The main server sends to the Ballots list of public keys that need to vote in this Ballot.

### In the election day

The Ballot is waiting for votes.

Citizens vote in all the Ballots that they get from the server. Citizens send to Ballots: public key, made up id, the vote, and signature of the vote, for the Ballot to verify. 

### When the election day ends

The Ballot is sent back to the main server only the votes and the made up id (not send the public key to make the main don't know who is voting for who).

The main server counts the votes and take the majority of the vote for each made up id. For example: 880 vote for party A 6 times and party B 2 times, take vote for the pary A. 


## Weakness

* Client side can be infected with a virus
* DDOS attacks the Ballots and/or the main server
* Only The main server can get the true votes, but he can lie 
* With enough present of Ballots the election can be compromise
* If we mix data from the Ballot server and the main server we can know who vote for who 

## Ways to improve security

* Real ID authentication
* Prevent everybody to be a Ballot - only in country IP or only party computers or private componise
* Same packets size of untracking of types of server
* Random timing for ballots for untracking that is a ballot server
* Force using SSL
