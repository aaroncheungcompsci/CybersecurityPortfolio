# OWASP Top 10

## Objective
Document thorough and practical understanding of the OWASP Top 10 in terms of what it is and its purpose. This file will be kept in an archive when the OWASP top 10 gets updated to incentivse keeping up with cybersecurity trends, and to preserve the work that I have done to understand it.

### What is it?
OWASP top 10 is a list detailing the top 10 security risks in web applications.

### What is its purpose?
OWASP top 10's purpose is to educate developers, security teams, and organizations on the most common and impactful vulnerabilities. This encourages secure coding practices and risk-based prioritization. 

### How often is it updated?
OWASP top 10 is updated approximately every 4 years. At the time of writing, it is almost the end of 2025, so the list should be updated soon as the last update was September of 2021.

## The list (Updated as of 2021)

1) <b>A01:2021 - Broken Access Control</b>
    - Allows unauthorized users to manipulate data that they shouldn't have access to. This typically occurs when applications don't have the proper access controls (like inappropriate user permissions or becoming a priveleged user via. Insecure Direct Object Reference) configured and in place.
    - This is not to be confused with Broken Authentication Control, which deals with authentication methods like inappropriate passwords or misconfigured multifactor authentication (MFA).
2) <b>A02:2021 – Cryptographic Failures</b>
    - Occurs when information is not properly protected, whether the data is at rest or in transit. Examples would be if an application uses deprecated cryptographic functions like MD5 or SHA1, or if utilizing legacy protocols that do not provide any form of encryption like FTP or SMTP.
3) <b>A03:2021 – Injection</b>
    - Allows unauthorized users to introduce hostile code to an application, which essentially changes the expected execution. Various injection attacks can include SQL, NOSQL, OS Command, or Object Relational Mapping (ORM) (There are more than just these 4).
4) <b>A04:2021 – Insecure Design</b>
    - Not to be confused with "insecure implenetation", where a secure design can still have flaws in implementation which lead to exploitable vulnerabilities. The reverse is not true; you can't have an insecurely designed application be "fixed" by perfect implementation. 
    - An example of this lies with my SQL injection lab, where I had to design prepared statements to be added within the source code to fix the vulnerability. Without the prepared statements, the code was flawed and could continue to be exploited.
5) <b>A05:2021 – Security Misconfiguration</b>
    - This refers to a failure to implement all necessary security controls in a web application or server, or incorrectly implementing a few security controls. This security risk is primarily caused by human error.
6) <b>A06:2021 – Vulnerable and Outdated Components</b>
    - These components can include the following:
        - Operating systems
        - Web/Application Servers
        - Data Management Systems
        - APIs (Application Programming Interface)
        - Runtime Environments
        - Libraries
    - An unauthorized user only needs to find one security flaw in these components to compromise an entire system.
7) <b>A07:2021 – Identification and Authentication Failures</b>
    - Otherwise known as "Broken Authentication Control", this can include the  compromise of the following:
        - Passwords
        - Keys
        - Session Tokens
        - User Information
    - As clarified when talking about Broken Access Control, misconfiguration of MFA or inappropriate passwords can be considered authentication failures.
8) <b>A08:2021 – Software and Data Integrity Failures</b>
    - This refers to the assumptions related to software updates, critical data, and CI/CD pipelines without verifying/ensuring integrity. 
    - An example of this would be if a web application utilizes a plugin from untrusted sources. That plugin would give an attacker a vector to work with.
9) <b>A09:2021 – Security Logging and Monitoring Failures</b>
    - Detecting attacks is essential to responding to them. Insufficient logging and monitoring means not responding to the failures, thereby compromising an entire system without any authorized user knowing. 
    - This can have a serious impact on visibility for a breach as well as digital forensics.
10) <b>A10:2021 – Server-Side Request Forgery (SSRF)</b>
    - Occurs when an attacker is able to successfully forge a request of information to a server, primarily due to the server not validating the user-supplied URL.
    - This security risk is becoming more and more prominent as cloud services become more popular.

## Resources
- https://www.youtube.com/watch?v=hryt-rCLJUA (OWASP Top 10 2021 - The List and How You Should Use It)
- https://owasp.org/Top10 (OWASP Top 10)