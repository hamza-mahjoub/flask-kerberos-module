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
        <li><a href="#Configuration">Configuration</a></li>
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

This repository contains implemented solution for **kerberos authentification** in web context. This project is implemented on **LINUX machines** using the **Ubuntu 20.04 LTS** distribution.
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
* Make sure you have **python3** and **pip** on the service machine.
```ssh
  sudo apt update
  sudo apt install python3
  sudo apt install python3-pip
``` 
 | Machine Name | Machine Ip  | Sub-domain name |
 | :---:         |     :---:      |          :---: |
 | git status   | git status     | git status    |
 | git diff     | git diff       | git diff      |

### Configuration

#### Configure-kerberos

<p align="right">(<a href="#top">back to top</a>)</p>

### Installation


1. Clone the repo
   ```sh
   git clone https://github.com/hamza-mahjoub/nestjs-backend-template.git
   ```
2. Install NPM packages
   ```sh
   npm install
   ```
3. Add a **.env** file
   ```sh
   CONNECTION_STRING="MongoDb connection string"
   APPLICATION_PORT = 3000  // port is 3000 by default.
   MORGAN_ENV = "dev"
   ```
<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage
- Run the project using 
```sh
   npm run start:dev
   ```
Examples will be provided to showcase some features of this project.

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

