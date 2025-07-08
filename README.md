# Deep Thought

Turn any text into a one-line summary using OpenAI.

---

## Quick start

```bash
docker run -i --rm \
  -e OPENAI_API_KEY=sk-... \
  ghcr.io/molnia1311/deep-thought "Long text to summarise"
```

Feed input via **args** or **stdin**; the summary prints to stdout.

### Config

| Env var                | Default          | Purpose                       |
| ---------------------- | ---------------- | ----------------------------- |
| `OPENAI_MODEL`         | `gpt-4o-mini`    | Model to call                 |
| `OPENAI_SYSTEM_PROMPT` | one-line summary | Customize the prompt          |

### Build locally

```bash
docker build -t deep-thought .
```
