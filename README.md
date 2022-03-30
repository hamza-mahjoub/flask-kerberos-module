# flask-kerberos-module
<div id="top"></div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#What-is-Kerberos">What is Kerberos</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#Kerberos-Configuration">Kerberos Configuration</a></li>
        <li><a href="#Flask-Configuration">Flask Configuration</a></li>
        <li>
           <a href="#installation">Installation</a>
        </li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
  </ol>
</details>

## About The project

This repository contains implemented solution for **kerberos authentification** in web context. A server expose files that are protected and shouldn't be accessible unless the user is authenticated. This project is implemented on **LINUX machines** using the **Ubuntu 20.04 LTS** distribution.
<p align="right">(<a href="#top">back to top</a>)</p>

### Built With
* [Python](https://www.python.org/), the widely used interpreted language.
* [Flask](https://flask.palletsprojects.com/en/2.1.x/), micro framework open-source de développement web en Python. the python micro-framework for wen developpement.

<p align="right">(<a href="#top">back to top</a>)</p>

### What is Kerberos
Kerberos is an AAA authentication protocol from the Massachusetts Institute of Technology (MIT) ”Athena” project. it is responsible for **authenticating, authorizing,
and monitoring users** who want to access _resources and services_ on your network thus the correspondance with the three-headed dog guardian of the gates of Hades in the greek mythology.
kerberos introduces the principle of **Single Sign-On (SSO)**. Thus with a single authentication, the user will have access to all the services of the network.
it relies on a trusted third party to manage authentication, the **KDC (Key Distribution Center)**. All users and services on the network trust this third party.
Kerberos uses a ticket system to perform authentication and introduces **the principle of SSO (Single Sign On)**. The user authenticates on the KDC and then uses a ticket to authenticate on each requested service. ( no password sending via network).

<p align="right">(<a href="#top">back to top</a>)</p>

## Getting Started

In order to run this project, we need to follow some few steps : 

### Prerequisites

* Make sure that you have a virtualization software.In this demo i used **Oracle VM VirtualBox** ( [Download Here](https://www.virtualbox.org/wiki/Downloads)).
* Make sure you have 2 linux machines with the **Ubuntu 20.04 LTS distribution**  ( [Download Here](https://ubuntu.com/download/desktop)).
* Make sure you have **python3** and **pip** on the server machine.
```bash
  sudo apt update
  sudo apt install python3
  sudo apt install python3-pip
``` 


### Kerberos Configuration

#### 1. Environnement

In order to proceed with the configurations we need to have a : 
- Domain name : "example.tn"
- Realm : "EXAMPLE.TN"
- Two machines : 

 | Machine Name     |   Machine IP   | Sub-domain name    |
 |    :---:         |     :---:      |    :---:           |
 | KDC              | 192.168.56.110 | kdc.example.tn     |
 | server           | 192.168.56.111 | server.example.tn  |
 > machines IP's are just an example, use `hostname -I` to get each machine ip. <br>
 > All the configurations must be done in **root** mode, use `su -` to connect as root.
 
<p align="right">(<a href="#top">back to top</a>)</p>

#### 2. DNS (Domain name system)
Used to match domain name to their IP's.
```bash
nano /etc/hosts
```
and add _(for each machine)_ : 
```bash
192.168.56.110    kdc.example.tn       kdc
192.168.56.111    server.example.tn    server
```
then set the **hostname**  _(for each machine)_ :
 | Machine Name     |            set new hostname                   | 
 |    :---:         |              :---:                            |
 | KDC              | `hostnamectl set-hostname kdc.example.tn `    |
 | server           | `hostnamectl set-hostname server.example.tn`  |

<p align="right">(<a href="#top">back to top</a>)</p>

#### 3. Time Synchronization
When the client obtains a ticket from Kerberos, it includes in its message the current time of day. One of the three parts of the response from Kerberos is a timestamp issued by the Kerberos server.

3.1. on the **_KDC_** install **ntp**:
```bash
apt install ntp
```
then edit the `/etc/ntp.conf` and add the lines below under the `# local users may interrogate the ntp server more closely` section: 
```bash
restrict 192.168.56.110 mask 255.255.255.0
nomodify notrap
server 127.127.1.0 stratum 10
listen on *
```
3.2. on the **_server_** install **ntp** and **ntpdate**:
```bash
apt install ntp
apt install ntpdate
```
then edit the `/etc/ntp.conf` and add the lines below under the `# Use Ubuntu's ntp server as a fallback` section: 
```bash
server 192.168.56.110
server obelix
```
<p align="right">(<a href="#top">back to top</a>)</p>

3.3. Synchronize time by running the below command on the server machine:
```bash
ntpdate -dv 192.168.56.110
```
<p align="right">(<a href="#top">back to top</a>)</p>

#### 4. Configure KDC
4.1. We need to install **the packages** _krb5-kdc_, _krb5-admin-server_ and _krb5-config_ by running : 
```bash
apt install krb5-kdc krb5-admin-server krb5-config
```
During installation you will be prompted to enter the _realm_, _kerberos server_ and _administartive server_ and it would be in order:
 | Prompt                  |    value         | 
 |    :---:                |     :---:        |
 | Realm                   | EXAMPLE.TN       |
 | Kerberos servers        | kdc.example.tn   |
 | Administrative Service  | kdc.example.tn   |
>Its capital sensitive.<br>
>View kdc settings with `cat /etc/krb5kdc/kdc.conf`.

4.2 Now we need to add **kerberos database** where principals will be stored
```bash
krb5_newrealm
```
> You will be prompted to choose a password.

4.3 we will create an _admin principal_ , a _host principal_ and generate its keytab:
- **principal:** a unique identity to which Kerberos can assign tickets.
- **keytb:** stores long-term keys for one or more principals and allow server applications to accept authentications from clients, but can also be used to obtain initial credentials for client applications.
```bash
kadmin.local                              # login as local admin
addprinc root/admin                       # add admin principal
addprinc -randkey host/kdc.example.tn     # add host principal
ktadd host/kdc.example.tn                 # generate host principal keytab
```
> type `q` to exit.

4.3 Grant the **admin principal** all privileges by editing `/etc/krb5kdc/kadm5.acl`:
```bash
root/admin *                              # just uncomment the line
```
4.4 restart the kerberos service by running: 
```bash
systemctl restart krb5-admin-server
systemctl status krb5-admin-server        # to check service status
```
<p align="right">(<a href="#top">back to top</a>)</p>

#### 5. Configure Server
5.1. We need to install **the packages** _krb5-user_, _libpam-krb5_ and _libpam-ccreds_ by running: 
```bash
apt install krb5-user libpam-krb5 libpam-ccreds
```
During installation you will be prompted to enter the _realm_, _kerberos server_ and _administartive server_ and it would be in order:
 | Prompt                  |    value         | 
 |    :---:                |     :---:        |
 | Realm                   | EXAMPLE.TN       |
 | Kerberos servers        | kdc.example.tn   |
 | Administrative Service  | kdc.example.tn   |
>Its capital sensitive.<br>
>View kdc settings with `cat /etc/krb5kdc/kdc.conf`.

5.2 we will create a _host principal_ and generate its keytab:
```bash
kadmin                                       # login as admin (type your password)
addprinc -randkey host/server.example.tn     # add host principal
ktadd host/server.example.tn                 # generate host principal keytab
```
> type `q` to exit.

5.3 Add a test user and create a correspending principal:
```bash
useradd -m -s /bin/bash testUser
kadmin
addprinc testUser
```
> type `q` to exit.

<p align="right">(<a href="#top">back to top</a>)</p>

### Flask Configuration

We install flask nn the **server** machine by running: 
```python
pip install Flask
```
Then we need to install the **Flask_kerberos** module by running:
```python
pip install Flask-Kerberos
```
> If an error occured run `apt install libkrb5-dev` then restart the Flask_kerberos module.<br>
> If it still persists, check your gcc installation.

<p align="right">(<a href="#top">back to top</a>)</p>

### Installation

1. Clone the repo
   ```console
   git clone https://github.com/hamza-mahjoub/flask-kerberos-module.git.
   ```
2. Login as root by running `su -`.

3. set the **KRB5_KTNAME** variable that references the **keytab**:
```bash
export KRB5_KTNAME=/etc/krb5.keytab
```
> To visualize your keytab, run the **ktutil** as root.
> ```bash
>ktutil                  
>?                         # list all commands
>read_kt /etc/krb5.keytab  # read keytab file
>list                      # show principals
>```

4. Turn all scripts executable by running `chmod 755 script_name.py`.
> There are 5 scripts: app.py, check_route.py, negotiate.py, addline.py, delete_line.py.



<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

before running the main 

app script: `./app.py` and everything should look normal.
```bash
```
<p align="right">(<a href="#top">back to top</a>)</p>

## Roadmap

- ✅ [Morgan middleware](https://www.npmjs.com/package/morgan)
- ✅ Setting up Configuration **.env** .
- ✅ Setting up **MongoDB** Database.
- 🔲 User Module
    - 🔲 User model.
    - 🔲 CRUD **(Create,Read,Update,Delete)**
- 🔲 [Swagger](https://swagger.io/).
- 🔲 Authentification Module.
- 🔲 Mailing Service.
- 🔲 RBAC **(Role Based Access Control)**
  
<p align="right">(<a href="#top">back to top</a>)</p>

