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

## Journal du premier démarrage (2026-09-20)

| Étape | Commande (PowerShell, invite `PS C:\…>`) | Résultat |
|---|---|---|
| Assistant de config | `openviking-server.exe init` → mode `[2]` tout-Ollama | modèles téléchargés : `qwen3-embedding:0.6b` (embedding) + `qwen3.5:4b` (VLM), ~5 Go |
| Réseau | Bind `[1] Local 127.0.0.1`, port `1933` | serveur joignable uniquement depuis ce PC (pas d'auth) |
| Diagnostic | `openviking-server.exe doctor` | 1er passage : `Embedding FAIL (probe timed out)` → 2e passage : **All checks passed** |
| Serveur | `openviking-server.exe` | `OpenViking HTTP Server is running on 127.0.0.1:1933`, tracer désactivé |
| CLI | `ov.exe status` → langue `English` → `ov.exe config` → Add Config → Custom → nom `local` → URL défaut → No key → Account `default` | config `local` active, `ov status` : **Connected (Healthy)** |
| Test fonctionnel | `ov add-resource C:\Projets\OpenViking\docs\en` → `ov find "what is openviking"` | ressource `viking://resources/en` indexée, 9 résultats L0/L1/L2 — **installation validée** |

### Astuce : `Embedding FAIL (probe timed out)`

Ce n'est pas une panne : sur 8 Go de RAM, le premier chargement du modèle d'embedding dans
Ollama dépasse le délai du test. Il suffit de « préchauffer » le modèle puis de relancer `doctor` :

```powershell
Invoke-RestMethod -Method Post -Uri http://localhost:11434/api/embed -ContentType 'application/json' -Body '{"model":"qwen3-embedding:0.6b","input":"test"}' | Select-Object model, load_duration
& "C:\Users\Ludi\anaconda3\Scripts\openviking-server.exe" doctor
```

Les messages `WARNING … slow call … duration_ms=3000` sont normaux en local (≈ 3 s par embedding).

### Config du CLI `ov`

Le CLI a sa propre config (`C:\Users\Ludi\.openviking\ovcli.conf`, hors dépôt) :
`ov config` → **Add Config** → **Local** (pas « OpenViking Service », qui est l'offre cloud payante)
→ URL `http://127.0.0.1:1933` → API key vide → nom libre (ex. `local`).

### Test fonctionnel (Terminal 2, serveur lancé dans le Terminal 1)

```powershell
& "C:\Users\Ludi\anaconda3\Scripts\ov.exe" status
& "C:\Users\Ludi\anaconda3\Scripts\ov.exe" add-resource C:\Projets\OpenViking\docs\en
& "C:\Users\Ludi\anaconda3\Scripts\ov.exe" task status TASK_ID      # répéter jusqu'à completed
& "C:\Users\Ludi\anaconda3\Scripts\ov.exe" ls viking://resources/
& "C:\Users\Ludi\anaconda3\Scripts\ov.exe" find "what is openviking"
```

## Ce que l'outil apporte, en l'état

1. **Mémoire de projets entre sessions** : importer `C:\Projets\<projet>` une fois, puis `ov find`
   ramène les fichiers pertinents au lieu de relire tout le projet (moins de tokens).
2. **Apprentissage des préférences** via le plugin Claude Code (hooks + MCP) : chaque session est
   « commitée », les enseignements sont réinjectés dans les suivantes — remplace `claude-mem`.
3. **Base de connaissances / RAG local** : PDF, cours, docs, pages web interrogeables en langage naturel.
4. **Skills réutilisables** dans `viking://user/<id>/skills/`.
5. **Web Studio** pour parcourir le contexte.

Limite : avec 8 Go de RAM et les modèles Ollama, indexation lente ; pour un usage intensif,
brancher le VLM sur une API cloud (mode mixte de `init`).

## Licence et usage commercial (analyse du 2026-09-20 — pas un avis juridique)

Licence **AGPL-3.0 pure** (aucune clause additionnelle dans le dépôt).

| Autorisé | Obligatoire |
|---|---|
| Usage commercial, accès payant | Publier le code source complet de la version modifiée à tout utilisateur du service réseau (art. 13) |
| Renommer le produit, propre domaine/logo | Rester sous AGPL (pas de version propriétaire dérivée) |
| Modifier / étendre le code | Conserver les mentions de copyright ByteDance ; ne pas utiliser les marques OpenViking / VikingBot |
| Héberger sur Alibaba Cloud (Docker fourni) | Activer l'authentification (mode Remote + clés API), isolation par utilisateur, HTTPS, conformité RGPD |

Modèle économique viable : vendre l'**hébergement**, le **support**, les **intégrations** et les
services annexes — pas le secret du code. ByteDance vend déjà l'équivalent (« OpenViking Service »).
À faire valider par un avocat spécialisé avant tout lancement.

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
