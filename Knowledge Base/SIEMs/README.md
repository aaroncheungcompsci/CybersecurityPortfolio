# SIEMs

### What is it?
SIEM stands for <b>Security Information and Event Management</b>, and it is a tool that collects data via. logs within an IT environment in real time. This allows security teams to detect, analyze, and respond to threats effectively in a centralized platform.

### What is its purpose?
The primary purpose of a SIEM is to provide security visibility by correlating events across systems, detecting suspicious activity, and supporting incident investigation/response.

### Why do SIEMs matter?
Modern environments generate large volumes of logs that are difficult to analyze manually. SIEMs help security teams reduce this complexity by aggregating events, applying detection rules, and highlighting activity that may require investigation.

## Mini-project
Upon doing my own research and investigations on learning how SIEMs work through a free application named Wazuh, I recognized that logs are a extremely important. That being said, for a beginner like me, logs can be overwhelming to analyze at first due to the sheer volume of different pieces of data. This left me with many questions, but a single one stood out:

- Which pieces of a log are relevant?

I decided to create a Python script to sort through and filter necessary 