# [NOM DU PRODUIT] — La mémoire d'entreprise pour vos agents IA

> Offre commerciale — version de travail du 2026-09-20.
> Base technique : OpenViking (open source, AGPL-3.0). Le nom commercial, le domaine et le logo
> sont à définir ; « [NOM DU PRODUIT] » est un espace réservé.

---

## 1. Le pitch en une phrase

**Vos agents IA (Claude Code, Codex, Cursor, vos automatisations) oublient tout à chaque session.
[NOM DU PRODUIT] leur donne une mémoire d'entreprise partagée, privée et interrogeable — ils
retiennent vos projets, vos règles et leur propre expérience, et coûtent moins cher en tokens.**

---

## 2. Le problème que vivent les entreprises qui développent avec l'IA

| Symptôme quotidien | Coût réel |
|---|---|
| Chaque nouvelle session repart de zéro : on ré-explique le projet, les conventions, les décisions | 15 à 30 min perdues par session, par développeur |
| L'agent relit des dizaines de fichiers pour répondre à une question simple | Facture tokens qui explose, réponses lentes |
| Les erreurs corrigées la semaine dernière reviennent | Qualité instable, frustration des équipes |
| Chaque outil (Claude Code, Cursor, Codex, agents Make/n8n) a sa propre « mémoire » incompatible | Connaissance éparpillée, aucun capital commun |
| Un nouveau collaborateur (humain ou agent) met des semaines à connaître le contexte | Onboarding lent, dépendance aux « sachants » |
| Les données sensibles partent dans des services cloud tiers | Risque RGPD, secret des affaires |

**Le vrai problème n'est pas l'intelligence des modèles : c'est l'absence de mémoire organisée.**

---

## 3. La solution : un système de fichiers de contexte pour tous vos agents

[NOM DU PRODUIT] est un serveur de contexte installé **chez vous** (poste, serveur, VPC cloud).
Il organise tout ce que vos agents doivent savoir dans une arborescence unique :

```
viking://
├── resources/        ← vos projets, votre documentation, vos repos, vos pages web
├── user/<équipe>/
│   ├── memories/     ← préférences, décisions, règles apprises automatiquement
│   ├── skills/       ← procédures validées, réutilisables par tout agent
│   └── resources/    ← ressources privées de l'équipe
```

Trois mécanismes font la différence :

1. **Chargement à trois niveaux (L0 / L1 / L2).** Chaque dossier porte un résumé d'une phrase et une
   vue d'ensemble. L'agent décide s'il a besoin du contenu complet *avant* de le lire.
   → C'est ce qui divise la consommation de tokens.
2. **Recherche sémantique guidée par la structure.** L'agent trouve d'abord le bon dossier, puis le
   bon fichier — comme un collègue qui sait où chercher.
3. **Capture automatique de l'expérience.** À la fin de chaque session, ce qui mérite d'être retenu
   (décision, correction, préférence, procédure) est extrait, comparé à l'existant, puis fusionné
   ou créé. La mémoire s'améliore seule, sans saisie manuelle.

Compatible nativement avec **Claude Code, Codex, Cursor, TRAE, OpenCode, LangChain** et tout client
**MCP** — un seul serveur de mémoire pour toute la chaîne d'outils.

---

## 4. Les bénéfices, chiffrés

Résultats publiés par l'éditeur du moteur (benchmarks LoCoMo et tau2-bench, reproductibles) :

| Indicateur | Sans mémoire | Avec le moteur | Gain |
|---|---|---|---|
| Précision de rappel des informations utilisateur (Claude Code) | 57 % | 80 % | **+23 pts** |
| Précision de rappel (autres agents) | 24 – 33 % | 82 – 83 % | **jusqu'à ×3,4** |
| Tokens d'entrée consommés | référence | | **−34 % à −91 %** |
| Latence des requêtes | référence | | **−58 % à −66 %** |
| Taux de réussite de tâches multi-étapes (mémoire d'expérience) | référence | | **+7 à +12 pts** |

Traduit pour une équipe qui développe à plein temps avec l'IA :

- **Moins de tokens** = facture API réduite dès le premier mois.
- **Moins de ré-explications** = des heures récupérées chaque semaine par développeur.
- **Moins d'erreurs répétées** = qualité qui monte au lieu d'osciller.
- **Un capital de connaissance** qui reste dans l'entreprise, même quand les personnes ou les outils
  changent.

---

## 5. Cas d'usage concrets pour une entreprise « IA à plein temps »

### 5.1 Mémoire de projet partagée
Tous vos dépôts et votre documentation sont importés une fois. N'importe quel agent, dans n'importe
quel outil, retrouve la bonne partie du bon projet en une requête. Fini le « relis tout le repo ».

### 5.2 Règles d'entreprise appliquées automatiquement
Conventions de code, langue des commentaires, procédures de déploiement, interdits de sécurité :
apprises une fois, réinjectées dans chaque session de chaque agent.

### 5.3 Agents d'automatisation qui capitalisent
Vos automatisations (Make, n8n, scripts, pipelines) enregistrent ce qui a marché comme **skills**.
La prochaine exécution part de l'expérience acquise au lieu de repartir de zéro.

### 5.4 Base de connaissances interne interrogeable
Contrats, procédures, comptes rendus, documentation fournisseurs, pages web : importés, résumés,
retrouvables en langage naturel avec la source exacte.

### 5.5 Onboarding accéléré
Un nouveau développeur ou un nouvel agent hérite immédiatement de tout le contexte de l'équipe.

### 5.6 Multi-agents coordonnés
Plusieurs agents spécialisés (analyse, code, tests, déploiement) partagent la même mémoire au lieu de
se transmettre des résumés incomplets.

---

## 6. Ce qui nous distingue

| | Mémoire native des outils | Services cloud de mémoire | **[NOM DU PRODUIT]** |
|---|---|---|---|
| Fonctionne avec plusieurs agents/outils | ✗ | partiel | **✓ tous (MCP, hooks natifs)** |
| Données hébergées chez vous | ✗ | ✗ | **✓ (poste, serveur, VPC)** |
| Réduction mesurée des tokens | ✗ | variable | **✓ −34 à −91 %** |
| Capture automatique de l'expérience | ✗ | partiel | **✓** |
| Code auditable, pas de boîte noire | ✗ | ✗ | **✓ open source** |
| Aucun enfermement propriétaire | ✗ | ✗ | **✓ données exportables** |

---

## 7. Nos offres

> Tarifs indicatifs à ajuster selon le positionnement et le marché. Toutes les offres sont sans
> engagement au-delà de la période indiquée.

### 🟢 DÉCOUVERTE — « Un poste, une semaine pour convaincre »
Pour un développeur ou un dirigeant qui veut mesurer le gain avant d'engager l'équipe.

- Installation sur **un poste** (Windows / macOS / Linux), modèles 100 % locaux ou API au choix
- Intégration à **un outil** (Claude Code, Cursor ou Codex)
- Import de **2 projets** + 1 session de prise en main (1 h, visio)
- Rapport de gain tokens/temps après 7 jours

**Prix indicatif : 490 € HT (forfait unique)**

### 🔵 ÉQUIPE — « Le serveur de mémoire de l'entreprise »
Pour une équipe de 3 à 15 personnes qui développe quotidiennement avec l'IA.

- Serveur dédié installé **chez le client** (serveur interne ou VPC cloud du client)
- Authentification, comptes utilisateurs, isolation des données, HTTPS
- Intégration de **tous les outils** de l'équipe (Claude Code, Cursor, Codex, MCP, LangChain…)
- Import initial de l'ensemble des projets et de la documentation
- Formation équipe (2 × 2 h) + guide d'usage interne
- Support prioritaire, mises à jour, sauvegardes configurées

**Prix indicatif : 2 900 € HT d'installation + 390 € HT / mois** (support, mises à jour, supervision)

### 🟣 ENTREPRISE — « Hébergé, supervisé, garanti »
Pour les organisations qui veulent le résultat sans gérer l'infrastructure.

- Hébergement géré sur **Alibaba Cloud** (ou le cloud du client), région au choix
- Supervision 24/7, sauvegardes quotidiennes, plan de reprise
- Modèles au choix : locaux (confidentialité maximale) ou API premium (performance maximale)
- Intégrations sur mesure (agents métier, automatisations, connecteurs internes)
- Accompagnement continu : revue mensuelle des mémoires et des skills, optimisation des coûts tokens
- Engagement de disponibilité contractuel

**Prix indicatif : sur devis — à partir de 1 200 € HT / mois**

### Options
- Migration depuis une mémoire existante (claude-mem, mem0, notes internes) : sur devis
- Journée d'atelier « agents + mémoire » sur site : 1 200 € HT
- Développement d'agents ou d'automatisations exploitant la mémoire : régie ou forfait

---

## 8. Comment se passe une installation

1. **Cadrage (30 min)** — outils utilisés, projets prioritaires, contraintes de confidentialité.
2. **Installation (½ à 1 journée)** — serveur, modèles, sécurité, intégrations.
3. **Import initial** — projets, documentation, règles d'entreprise.
4. **Formation** — comment interroger, comment capitaliser, bonnes pratiques.
5. **Semaine 2 : mesure** — tokens économisés, temps gagné, ajustements.
6. **Suivi** — mises à jour, revue des mémoires, nouvelles intégrations.

---

## 9. Sécurité et confidentialité

- **Vos données restent chez vous** : aucune télémétrie, aucun envoi vers un service tiers sans votre
  configuration explicite (vérifié par audit du code source).
- **Choix des modèles** : 100 % local (rien ne sort de votre réseau) ou fournisseur d'API de votre
  choix, avec vos propres clés.
- **Contrôle d'accès** : comptes, clés API, isolation par utilisateur, listes de contrôle par
  ressource.
- **Conformité RGPD** : hébergement en Europe possible, données exportables et supprimables.
- **Transparence totale** : le moteur est open source (AGPL-3.0) — auditable par votre DSI, aucun
  enfermement propriétaire. Vous payez notre expertise, notre installation et notre support, pas une
  boîte noire.

---

## 10. Réponses aux objections fréquentes

**« Le moteur est open source, pourquoi payer ? »**
Parce que l'installation, la sécurisation, le choix des modèles, les intégrations, l'import et la
formation prennent des jours à une équipe qui ne l'a jamais fait — et que la valeur vient de la
mémoire *bien organisée*, pas du logiciel brut. Vous gardez la liberté de reprendre la main à tout
moment : c'est justement notre garantie anti-enfermement.

**« Nos données sont sensibles. »**
Tout tourne chez vous. En mode local, aucune donnée ne quitte votre réseau. Nous vous remettons le
rapport d'audit du code.

**« Ça va coûter cher en modèles ? »**
Non : les modèles locaux sont gratuits, et si vous utilisez des API, la réduction de tokens
(−34 à −91 %) finance l'outil.

**« Nos développeurs utilisent des outils différents. »**
C'est le cas d'usage central : un seul serveur de mémoire pour Claude Code, Cursor, Codex, et tout
client MCP.

**« Et si vous disparaissez ? »**
Le moteur est open source, vos données sont dans un format ouvert sur vos serveurs, et la
documentation d'exploitation vous est remise. Vous n'êtes jamais bloqués.

---

## 11. Discours pour les vidéos

### 11.1 Teaser 60 secondes
> Vous développez avec l'IA tous les jours ? Alors vous connaissez ça : chaque matin, votre agent a
> tout oublié. Le projet, vos règles, l'erreur corrigée hier. Vous ré-expliquez. Il relit tout. La
> facture de tokens grimpe.
>
> [NOM DU PRODUIT] change ça. C'est une mémoire d'entreprise pour vos agents IA, installée chez vous.
> Vos projets, vos règles, l'expérience de vos agents — organisés, retrouvables, partagés entre
> Claude Code, Cursor, Codex et vos automatisations.
>
> Résultat mesuré : jusqu'à 3 fois plus de précision, jusqu'à 90 % de tokens en moins.
> Vos données ne quittent jamais votre réseau.
>
> Installation en une journée. Lien en description.

### 11.2 Démo 5 minutes (plan)
1. **(0:00)** Le problème en direct : une session d'agent qui repart de zéro, relit 40 fichiers.
2. **(0:45)** Même question, avec [NOM DU PRODUIT] : `find` ramène 3 fichiers, réponse immédiate.
3. **(1:30)** L'arborescence `viking://` : ressources, mémoires, skills — « comme un disque dur pour
   l'IA ». Montrer les résumés L0/L1.
4. **(2:30)** Fin de session : la mémoire capture une décision automatiquement. Nouvelle session :
   elle est là.
5. **(3:30)** Multi-outils : la même mémoire depuis Cursor puis depuis Claude Code.
6. **(4:15)** Sécurité : tout est local, modèles au choix, code auditable.
7. **(4:45)** Les trois offres et l'appel à l'action.

### 11.3 Phrases clés à réutiliser
- « Vos agents IA sont brillants, mais amnésiques. Nous leur donnons une mémoire. »
- « Un seul disque dur de contexte pour tous vos outils IA. »
- « Moins de tokens, moins de répétitions, plus de résultats. »
- « Installé chez vous. Vos données ne partent nulle part. »
- « Open source, auditable, sans enfermement — vous payez l'expertise, pas la boîte noire. »

---

## 12. Appel à l'action

**Réservez un diagnostic de 30 minutes** : nous regardons vos outils, vos projets et estimons votre
gain en tokens et en temps. Sans engagement.

→ [lien de réservation] · [e-mail] · [site]

---

## Annexe — Mentions à respecter (usage commercial du moteur AGPL-3.0)

- Le moteur est distribué sous licence AGPL-3.0 : le code source de la version déployée doit être
  accessible aux utilisateurs du service (lien « code source » dans l'interface).
- Les mentions de copyright de l'éditeur d'origine sont conservées dans les sources.
- Les marques de l'éditeur d'origine ne sont pas utilisées dans la communication ; seul le nom
  commercial [NOM DU PRODUIT] apparaît.
- Faire valider l'ensemble par un conseil juridique avant la première vente.
