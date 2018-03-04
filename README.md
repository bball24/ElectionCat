# ElectionCat

ElectionCat is designed to help student organizations conduct their elections as pain-free and convenient as possible.

By default, ElectionCat is set up for a mock ACM@UCR election; modifying for your own org is easy!


# Requirements:

- Python 3.4+
- Flask


# Installation:

Locally-Hosted:
1. Change whatever you would like in the settings/JSON files
2. run main.py
3. By default, the server will be running at localhost:5000/

Remotely-Hosted:
1. Change whatever you would like in the settings/JSON files
2. Deploy the package to the host, it *should* automatically run


# How to Use:

Before running the server, make sure the following are set:
  /assets: change the logo, unless you want to showcase ACM@UCR
  /databases: - modify the idlist.json to your student population (student IDs, network IDs, anything else), users need to
                provide a valid ID to vote. This file is a simple list.
              - modify the candidates.json to fit your needs; the hierarchy is Position->Candidate->Biography
              - the votes.json does not need to exist: a blank one will be created automatically

Initially, voting is closed. To open voting, browse to "yourhostedsite.com/start" and enter your admin key. By default,
the key is "password".

To close the voting, browse to "yourhostedsite.com/stop" and enter your admin key. You will be redirected to a special
results page with the tallied votes of each candidate. Other users are redirected to the root page "yourhostedsite.com",
and see only the winners of each position.


# How it works:

ElectionCat works to guide users through the GUI: normal users visit "yourhostedsite.com", log in with their valid ID,
and proceed to vote, change their votes, and read the bios throughout the voting period. Once an admin ends the election,
normal users will soon be redirected to the results page, displaying the winners of each position.

The only difference between an admin and a normal user is the knowledge of the "admin key", which is used to open and
close voting through the "/start" and "/stop"


# Temporary Example Hosting:

https://electioncat.azurewebsites.net/


# Authors:

Jack Kolb <br />
Jerry Tan <br />

Created for HackTech 2018