# LLM documentation entry point

This directory helps a documentation assistant locate a human-authored source.
It is not an agent prompt, an API credential, or an authorization layer.

Rules for LLM use:

1. Select a document matching language, Diátaxis type, audience, and goal.
2. Preserve `observed`, `estimated`, `decision`, and `unavailable` labels.
3. Cite the source path and its limitations.
4. Do not infer public availability from the presence of documentation.
5. Do not turn a tutorial into permission to mutate a device or server.
6. Ask the operator before an action requires credentials, network exposure,
   deployment, firmware writing, deletion, purchase, or publication.

The canonical machine-readable list is [context-index.json](context-index.json).
