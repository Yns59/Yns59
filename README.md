<!--
  A VERIFIER AVANT DE PUBLIER :
  1. Ce depot doit s'appeler exactement comme ton pseudo (Yns59/Yns59) pour s'afficher sur ton profil.
  2. Le lien LinkedIn (section contact) : verifie qu'il ouvre bien ton profil.
  3. Pour mettre a jour la roadmap : modifie roadmap.yml et push. La GitHub Action regenere assets/pipeline.svg.
  4. Ne touche pas aux balises waka (START_SECTION / END_SECTION) : WakaTime les met a jour tout seul.
-->

<div align="center">

<img src="./assets/banner.svg" width="100%" alt="Terminal animé. whoami : Younes, étudiant en Bachelor Informatique à Enigma, Lille. Mission : devenir la meilleure version de moi-même. Maintenant : TypeScript, ensuite React et Next.js. Recherche une alternance." />

<br/><br/>

*« Le meilleur moyen d'apprendre, c'est de faire. »*

</div>

<br/>

## `whoami`

Je m'appelle **Younes**, étudiant en **Bachelor Informatique à l'école Enigma** (2ème année, Lille), passionné par la création d'applications web .

J'aime apprendre, construire, casser des trucs, et recommencer jusqu'à ce que ce soit propre. Mon moteur : comprendre **tout le chemin d'une application**, du code jusqu'au serveur qui la fait tourner. C'est pour ça qu'à côté de PHP et Symfony, j'ai monté mon propre **homelab** (serveurs, virtualisation, automatisation) pour m'entraîner en autodidacte sur le DevOps.

Je ne vise pas « un bon niveau ». Je vise **la meilleure version de moi-même**, un jour de travail après l'autre.

> **1 % de mieux chaque jour = environ ×37 en un an.**
> Je ne cherche pas la perfection du premier coup, je cherche la progression, tous les jours.

<br/>

## `stack.yml`

```yaml
# mon environnement de travail
services:
  backend:   [PHP, Symfony, Python]
  frontend:  [HTML, CSS, JavaScript]
  data:      [SQL]
  devops:
    - Docker                    # utilisé en conditions réelles (stage)
    - Linux / Bash
    - Terraform
    - homelab perso             # serveurs, virtualisation, automatisation
    - GitLab CI/CD              # notions
    - Kubernetes                # notions, en autoformation

apprentissage:
  maintenant: TypeScript
  ensuite:    [React, Next.js]

domaines:    [sécurité appliquée à l'IoT, objets connectés, domotique et IA,
              administration systèmes Windows / Linux, gestion de projet]
langues:     [français (langue maternelle), anglais, arabe]
hors_code:   [sport de combat, cinéma, voyages]
```

<br/>

## `pipeline`

Ma roadmap de **Dev vers DevOps**, présentée comme un pipeline CI. Elle n'est pas une image figée : elle est **générée depuis [`roadmap.yml`](./roadmap.yml) par une GitHub Action**. Je change un pourcentage, je push, et le pipeline se met à jour tout seul. (De l'infra as code, appliquée à mon propre profil.)

<div align="center">

<img src="./assets/pipeline.svg" width="100%" alt="Pipeline de ma roadmap en 6 étapes : fondations, dev moderne (focus actuel : TypeScript, puis React et Next.js), conteneurs, infra et cloud, orchestration, excellence. L'avancement détaillé est dans roadmap.yml." />

</div>

<br/>

## `CHANGELOG.md`

```text
du plus récent au plus ancien

2026 · stage développeur web — Restaurant Le 44, Seclin (3 mois)
  ├─ Docker : conteneurisation de l'application, architecture multi-images
  ├─ Back-office : CRUD pour gérer menus à la carte et galerie de photos
  ├─ Comptes utilisateurs avec modification de profil sécurisée
  └─ Réservation de tables, données transmises au tableau de bord admin

2025 · Bachelor Informatique — École Supérieure des Sciences de l'Informatique (Enigma)
  └─ 2025 → 2028 : web, réseaux, sécurité IoT, objets connectés, domotique et IA,
                   administration systèmes Windows / Linux, gestion de projet

2024 · Baccalauréat, mention Assez Bien

2022 · stage technique — Centre Lazar Garreau (1 mois)
  └─ dépannage matériel et logiciel, installation et mise à jour de systèmes d'exploitation
```

<br/>

## `TODO.md`

**Déjà accompli**
- [x] Réaliser un **stage de développeur web** (3 mois) : site complet, back-office, réservation
- [x] **Conteneuriser** une vraie application sous Docker (architecture multi-images)
- [x] Monter mon propre **homelab** pour m'entraîner en autodidacte

**Court terme**
- [ ] Décrocher une **alternance** pour progresser sur du concret
- [ ] Avoir des bases solides en **TypeScript**
- [ ] Construire un premier projet **React**
- [ ] Mettre en place un pipeline **CI/CD** complet

**Moyen terme**
- [ ] Livrer une application **full-stack Next.js** déployée en ligne
- [ ] Provisionner toute une infra avec **Terraform**
- [ ] Faire tourner une vraie application sur **Kubernetes**

**Long terme**
- [ ] Maîtriser l'**observabilité** (monitoring, logs, alertes)
- [ ] Obtenir une **certification** cloud / DevOps
- [ ] Devenir un développeur **full-stack complet, avec une vraie culture DevOps**

<br/>

## `principes`

1. **Apprendre chaque jour**, même 30 minutes.
2. **Construire plutôt que regarder** : un projet vaut mille tutos.
3. **Casser, comprendre, recommencer** : l'erreur fait partie du chemin.
4. **Viser propre** : un code lisible, une infra reproductible.
5. **Ne jamais s'arrêter** : la curiosité n'a pas de ligne d'arrivée.

<!--
  PROJETS EN VEDETTE (decommente et complete quand tu as quelque chose a montrer) :

  ## `projets`

  | Projet | Description | Stack |
  |:---|:---|:---|
  | [Nom du projet](https://github.com/Yns59/nom-du-repo) | Ce qu'il fait, en une phrase | PHP · Symfony · Docker |
-->

<br/>

## `wakatime`

<!--START_SECTION:waka-->

```txt
From: 18 June 2026 - To: 10 October 2026

Total Time: 68 hrs 36 mins

YAML                21 hrs 58 mins        ████████░░░░░░░░░░░░░░░░░   31.57 %
PHP                 14 hrs 8 mins         █████░░░░░░░░░░░░░░░░░░░░   20.32 %
JavaScript          8 hrs 14 mins         ███░░░░░░░░░░░░░░░░░░░░░░   11.83 %
Terraform           4 hrs 54 mins         █▓░░░░░░░░░░░░░░░░░░░░░░░   07.05 %
Docker              3 hrs 56 mins         █▒░░░░░░░░░░░░░░░░░░░░░░░   05.66 %
Bash                2 hrs 51 mins         █░░░░░░░░░░░░░░░░░░░░░░░░   04.11 %
HCL                 56 mins               ▒░░░░░░░░░░░░░░░░░░░░░░░░   01.34 %
```

<!--END_SECTION:waka-->

<br/>

## `contact`

Je suis **à la recherche d'une alternance** en développement web / DevOps, sur Lille et ses environs. Passionné et proactif, je veux mettre mes compétences techniques (web, réseaux) au service de vos projets tout en renforçant mon expertise sur le terrain.

Si tu as une opportunité, ou juste envie d'échanger :

- **LinkedIn** : [Younes-Gallouch](https://www.linkedin.com/in/Younes-Gallouch)
- **Email** : [gallouchy@gmail.com](mailto:gallouchy@gmail.com)

<br/>

<div align="center">

```text
$ younes --status
build en cours · la suite au prochain commit ▌
```

</div>| **2022** (1 mois) | 🔧 **Stage technique**, Centre Lazar Garreau | Dépannage matériel et logiciel, installation, configuration et mise à jour de systèmes d'exploitation et de logiciels |
| **2023 – 2024** | 📜 **Baccalauréat**, mention Assez Bien | |

### 💼 Ce que j'ai livré en stage

- 🐳 **Déploiement et DevOps :** conteneurisation de l'application sous **Docker** (architecture multi-images) pour un environnement isolé et propre
- 🗂️ **Back-office et CRUD :** interface administrateur pour gérer dynamiquement le contenu du site (menus à la carte, galerie de photos)
- 🔐 **Gestion des utilisateurs :** système de comptes avec modification de profil sécurisée
- 📅 **Système de réservation :** module de réservation de tables, avec transmission automatique des données (nom, prénom, couverts) vers le tableau de bord de l'administrateur

---

## ⌨️ Ma stack

**Ce que j'utilise**

![PHP](https://img.shields.io/badge/PHP-777BB4?style=for-the-badge&logo=php&logoColor=white)
![Symfony](https://img.shields.io/badge/Symfony-000000?style=for-the-badge&logo=symfony&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge)

**Ce que j'explore côté DevOps et systèmes**

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)
![GitLab CI/CD](https://img.shields.io/badge/GitLab_CI%2FCD-notions-FC6D26?style=for-the-badge&logo=gitlab&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-notions-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![YAML](https://img.shields.io/badge/YAML-CB171E?style=for-the-badge&logo=yaml&logoColor=white)

**Ce que j'apprends maintenant** 🌱

![TypeScript](https://img.shields.io/badge/TypeScript-en%20cours-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![React](https://img.shields.io/badge/React-prochainement-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![Next.js](https://img.shields.io/badge/Next.js-prochainement-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)

**Domaines qui me passionnent :** 🔒 sécurité appliquée à l'IoT · 📡 objets connectés · 🏡 domotique et IA · 🖥️ administration systèmes Windows / Linux · 📋 gestion de projet

---

## 🗺️ Ma roadmap : de Dev à DevOps

> Je documente ma progression pour rester honnête avec moi-même, et pour que tu voies où j'en suis.

**Légende :** ✅ Acquis · 🔄 En cours · 🎯 Prochain objectif · ⏳ Plus tard

<!--
  COMMENT METTRE A JOUR LA ROADMAP :
  - Change l'emoji de statut (🎯 -> 🔄 -> ✅).
  - Ajuste la barre : 10 blocs, ▰ = rempli, ▱ = vide (ex. 40 % = ▰▰▰▰▱▱▱▱▱▱).
  - Mets aussi a jour le schema Mermaid plus bas (classes done / wip / todo).
-->

```mermaid
flowchart LR
    A["🧱 Fondations Dev<br/>PHP · Symfony · JS · Python"] --> B["⚛️ Dev moderne<br/>TypeScript · React · Next.js"]
    B --> C["🐳 Conteneurs et CI/CD<br/>Docker · Homelab · Pipelines"]
    C --> D["☁️ IaC et Cloud<br/>Terraform · Cloud"]
    D --> E["☸️ Orchestration<br/>Kubernetes · Observabilité"]
    E --> F["🏆 Dev + DevOps complet"]

    classDef done fill:#2ea043,color:#ffffff,stroke:#2ea043
    classDef wip fill:#f0883e,color:#ffffff,stroke:#f0883e
    classDef todo fill:#30363d,color:#ffffff,stroke:#6e7681

    class A done
    class B,C,D,E wip
    class F todo
```

### 🧱 Phase 1 : Fondations du développeur

| Statut | Compétence | Progression |
|:---:|:---|:---|
| ✅ | HTML / CSS | `▰▰▰▰▰▰▰▰▱▱` 80 % |
| 🔄 | JavaScript | `▰▰▰▰▰▰▱▱▱▱` 60 % |
| 🔄 | PHP | `▰▰▰▰▰▰▰▱▱▱` 70 % |
| 🔄 | Symfony et architecture MVC | `▰▰▰▰▰▱▱▱▱▱` 50 % |
| 🔄 | Python | `▰▰▰▰▱▱▱▱▱▱` 40 % |
| 🔄 | Bases de données (SQL) | `▰▰▰▰▰▱▱▱▱▱` 50 % |
| 🔄 | Git et workflow collaboratif | `▰▰▰▰▰▰▱▱▱▱` 60 % |

### ⚛️ Phase 2 : Développement moderne *(mon focus actuel)*

| Statut | Compétence | Progression |
|:---:|:---|:---|
| 🔄 | **TypeScript** | `▰▱▱▱▱▱▱▱▱▱` 10 % |
| 🎯 | **React** | `▱▱▱▱▱▱▱▱▱▱` 0 % |
| 🎯 | **Next.js** | `▱▱▱▱▱▱▱▱▱▱` 0 % |

### 🐳 Phase 3 : Conteneurs, CI/CD et automatisation

| Statut | Compétence | Progression |
|:---:|:---|:---|
| 🔄 | Docker et Docker Compose (déjà utilisé en stage) | `▰▰▰▰▰▱▱▱▱▱` 50 % |
| 🔄 | Linux et scripting Bash | `▰▰▰▰▱▱▱▱▱▱` 40 % |
| 🔄 | Homelab perso (serveurs, virtualisation, automatisation) | `▰▰▰▰▱▱▱▱▱▱` 40 % |
| 🔄 | Pipelines CI/CD (GitLab CI, GitHub Actions) | `▰▰▱▱▱▱▱▱▱▱` 25 % |

### ☁️ Phase 4 : Infrastructure as Code et Cloud

| Statut | Compétence | Progression |
|:---:|:---|:---|
| 🔄 | Terraform (HCL) | `▰▰▱▱▱▱▱▱▱▱` 20 % |
| 🎯 | Ansible | `▱▱▱▱▱▱▱▱▱▱` 0 % |
| 🎯 | Un cloud provider (AWS / Azure / GCP) | `▱▱▱▱▱▱▱▱▱▱` 0 % |

### ☸️ Phase 5 : Orchestration et observabilité

| Statut | Compétence | Progression |
|:---:|:---|:---|
| 🔄 | Kubernetes (en autoformation) | `▰▱▱▱▱▱▱▱▱▱` 10 % |
| ⏳ | Monitoring (Prometheus / Grafana) | `▱▱▱▱▱▱▱▱▱▱` 0 % |
| ⏳ | GitOps (ArgoCD / Flux) | `▱▱▱▱▱▱▱▱▱▱` 0 % |

### 🏆 Phase 6 : Excellence

| Statut | Compétence | Progression |
|:---:|:---|:---|
| 🔄 | Sécurité : DevSecOps, en m'appuyant sur ma base sécurité IoT | `▰▱▱▱▱▱▱▱▱▱` 10 % |
| ⏳ | Tests automatisés et qualité de code | `▱▱▱▱▱▱▱▱▱▱` 0 % |
| ⏳ | Certification cloud / DevOps | `▱▱▱▱▱▱▱▱▱▱` 0 % |
| ⏳ | Contribuer à un projet open source | `▱▱▱▱▱▱▱▱▱▱` 0 % |

**📊 Progression globale :** `▰▰▰▱▱▱▱▱▱▱` ~30 %

---

## 🎯 Mes objectifs

**✅ Déjà accompli**
- [x] Réaliser un **stage de développeur web** (3 mois) : site complet, back-office, réservation
- [x] **Conteneuriser** une vraie application sous Docker (architecture multi-images)
- [x] Monter mon propre **homelab** pour m'entraîner en autodidacte

**🔥 Court terme**
- [ ] Décrocher une **alternance** pour progresser sur du concret
- [ ] Avoir des bases solides en **TypeScript**
- [ ] Construire un premier projet **React**
- [ ] Mettre en place un pipeline **CI/CD** complet

**🚀 Moyen terme**
- [ ] Livrer une application **full-stack Next.js** déployée en ligne
- [ ] Provisionner toute une infra avec **Terraform**
- [ ] Faire tourner une vraie application sur **Kubernetes**

**🏆 Long terme**
- [ ] Maîtriser l'**observabilité** (monitoring, logs, alertes)
- [ ] Obtenir une **certification** cloud / DevOps
- [ ] Devenir un développeur **full-stack complet, avec une vraie culture DevOps**

---

## 💪 Mes principes

1. **Apprendre chaque jour**, même 30 minutes.
2. **Construire plutôt que regarder** : un projet vaut mille tutos.
3. **Casser, comprendre, recommencer** : l'erreur fait partie du chemin.
4. **Viser propre** : un code lisible, une infra reproductible.
5. **Ne jamais s'arrêter** : la curiosité n'a pas de ligne d'arrivée.

---

## 🛠️ En ce moment

- 🌱 J'approfondis mes connaissances en **Symfony** et architecture MVC
- 🔷 Je me forme à **TypeScript**, avant de passer à **React** puis **Next.js**
- 🐳 J'avance sur **Docker, CI/CD (GitLab, GitHub Actions), Terraform et Kubernetes** pour la partie DevOps
- 🏠 Je fais évoluer mon **homelab** pour tester de nouveaux outils
- 🧪 J'explore le développement d'applications web complètes, de la base de données à l'interface
- 💻 Je travaille sur des projets perso pour mettre en pratique ce que j'apprends
- 📚 Toujours un onglet de doc ouvert quelque part

<!--
  PROJETS EN VEDETTE (decommente et complete quand tu as quelque chose a montrer) :

  ## 📂 Projets en vedette

  | Projet | Description | Stack |
  |:---|:---|:---|
  | [Nom du projet](https://github.com/Yns59/nom-du-repo) | Ce qu'il fait, en une phrase | PHP · Symfony · Docker |
-->

---

## ⏱️ Mon temps de code (WakaTime)

<!--START_SECTION:waka-->

```txt
From: 18 June 2026 - To: 10 October 2026

Total Time: 68 hrs 36 mins

YAML                21 hrs 58 mins        ████████░░░░░░░░░░░░░░░░░   31.57 %
PHP                 14 hrs 8 mins         █████░░░░░░░░░░░░░░░░░░░░   20.32 %
JavaScript          8 hrs 14 mins         ███░░░░░░░░░░░░░░░░░░░░░░   11.83 %
Terraform           4 hrs 54 mins         █▓░░░░░░░░░░░░░░░░░░░░░░░   07.05 %
Docker              3 hrs 56 mins         █▒░░░░░░░░░░░░░░░░░░░░░░░   05.66 %
Bash                2 hrs 51 mins         █░░░░░░░░░░░░░░░░░░░░░░░░   04.11 %
HCL                 56 mins               ▒░░░░░░░░░░░░░░░░░░░░░░░░   01.34 %
```

<!--END_SECTION:waka-->

---

## 📊 Mes stats GitHub

<div align="center">

<img height="180" src="https://github-readme-stats.vercel.app/api?username=Yns59&show_icons=true&theme=tokyonight&hide_border=true&count_private=true" alt="Stats GitHub" />
<img height="180" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Yns59&layout=compact&theme=tokyonight&hide_border=true" alt="Langages principaux" />

<br/>

<img src="https://streak-stats.demolab.com?user=Yns59&theme=tokyonight&hide_border=true" alt="Streak GitHub" />

<br/>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=Yns59&theme=tokyo-night&hide_border=true" width="100%" alt="Activité GitHub" />

</div>

---

## 🌍 Au-delà du code

- 🗣️ **Langues :** 🇫🇷 Français (langue maternelle) · 🇬🇧 Anglais · 🌍 Arabe
- 🥊 Sport de combat : discipline, persévérance et humilité, des valeurs que je retrouve dans le code
- 🎬 Cinéma
- ✈️ Voyages

---

## 🤝 Travaillons ensemble

Je suis **à la recherche d'une alternance** en développement web / DevOps, sur Lille et ses environs. Passionné et proactif, je veux mettre mes compétences techniques (web, réseaux) au service de vos projets tout en renforçant mon expertise sur le terrain. Si tu as une opportunité ou juste envie d'échanger, écris-moi !

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Younes_Gallouch-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/Younes-Gallouch)
[![Email](https://img.shields.io/badge/Email-gallouchy%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:gallouchy@gmail.com)

</div>

---

<div align="center">

### *« Je ne suis pas encore là où je veux être, mais je suis plus loin qu'hier. »* 🚀

*Profil en construction, comme moi.* 🚧

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:6C63FF,100:00C9A7&height=120&section=footer" width="100%" alt="" />

</div>
