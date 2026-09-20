# OpenViking — Notes d'installation (Lüdi)

> Fork de [volcengine/OpenViking](https://github.com/volcengine/OpenViking) — licence AGPL-3.0.
> Installé le 2026-09-20 par Claude Code après audit de sécurité.

## C'est quoi ?

OpenViking est une **base de données de contexte pour agents IA** (ByteDance / Volcano Engine) :
un système de fichiers virtuel `viking://` dans lequel un agent (Claude Code, Codex, Cursor…)
range et retrouve :

- `resources/` → documents, dépôts de code, pages web importés
- `user/<id>/memories/` → préférences et expérience de l'utilisateur, conservées entre sessions
- `user/<id>/skills/` → façons de faire réutilisables

Chaque dossier porte un résumé court (L0) et une vue d'ensemble (L1) : l'agent ne charge le
contenu complet (L2) que si c'est pertinent → moins de tokens consommés.

## Résultat de l'audit de sécurité (2026-09-20)

| Point vérifié | Résultat |
|---|---|
| Licence | AGPL-3.0, aucune clé d'activation, gratuit en auto-hébergement |
| Réputation | 38 166 ⭐, 2 960 forks, release v0.4.21 le jour même, dépôt actif |
| Télémétrie | OpenTelemetry présent mais **désactivé par défaut** (`enabled: False`, cible `localhost:4317`) |
| Analytics web (Studio) | aucun (pas de Google Analytics, Baidu, Sentry, PostHog…) |
| Appels réseau au démarrage | aucun « check update » / « phone home » trouvé |
| URLs externes codées en dur | uniquement des endpoints de providers (Volcengine Ark, OpenRouter, Ollama, Kimi, Z.ai…) utilisés **seulement si tu les configures** |
| Cloud Volcengine | proposé comme **option 2** dans l'assistant, jamais par défaut (défaut = serveur local `127.0.0.1:1933`) |
| Téléchargement modèle local | modèle d'embedding `bge-small-zh-v1.5-gguf` depuis HuggingFace (attendu) |
| Bot Feishu/Lark | code présent, inactif sans configuration |

**Conclusion : aucun piège d'espionnage détecté.** Les données restent en local tant que tu
choisis un provider local (Ollama) ou ton propre compte API (OpenAI, OpenRouter…).

⚠️ Point d'attention : le serveur **ne demande pas d'authentification par défaut**. Ne l'expose
jamais au-delà de `localhost` sans configurer l'authentification (voir `docs/`).

## Installation faite

```powershell
# Package Python dans Anaconda (Windows)
& "C:\Users\Ludi\anaconda3\python.exe" -m pip install openviking --upgrade
```

Le dépôt est cloné dans `C:\Projets\OpenViking` (remote `origin` = fork L-k1, `upstream` = volcengine).

## Premier démarrage (à faire par Lüdi)

```powershell
# 1. Assistant de configuration : choisir le provider d'embedding + VLM
#    (recommandé pour rester 100 % local : Ollama ; sinon OpenAI / OpenRouter avec ta clé)
& "C:\Users\Ludi\anaconda3\Scripts\openviking-server.exe" init

# 2. Vérifier la config et la connectivité
& "C:\Users\Ludi\anaconda3\Scripts\openviking-server.exe" doctor

# 3. Démarrer le serveur (port 1933 par défaut)
& "C:\Users\Ludi\anaconda3\Scripts\openviking-server.exe"
```

Dans un second terminal :

```powershell
& "C:\Users\Ludi\anaconda3\Scripts\ov.exe" status
& "C:\Users\Ludi\anaconda3\Scripts\ov.exe" add-resource C:\Projets\OpenViking\docs\en
& "C:\Users\Ludi\anaconda3\Scripts\ov.exe" find "what is openviking"
```

La configuration est écrite dans `~/.openviking/ov.conf` (`C:\Users\Ludi\.openviking\`).

## Intégration Claude Code (plus tard)

Le dossier `examples/claude-code-memory-plugin/` contient un plugin (hooks + MCP) qui donne à
Claude Code une mémoire inter-sessions via le serveur local. Marketplace :
`/plugin marketplace add volcengine/OpenViking`. À tester une fois le serveur opérationnel.

## Mettre à jour depuis l'original

```powershell
git fetch upstream
git merge upstream/main
git push origin main
```
