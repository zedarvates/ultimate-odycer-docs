# LLM documentation entry point

This directory helps a documentation assistant locate a human-authored source.
It is not an agent prompt, an API credential, or an authorization layer.

Rules for LLM use:

1. Select a document matching language, Diátaxis type, audience, and goal.
2. Preserve `observed`, `estimated`, `decision`, and `unavailable` labels.
3. Cite the source path and its limitations.
4. Read `PUBLICATION_STATUS.md` for this repository's publication state; do not
   infer that any server, firmware, model, or service is public.
5. Do not turn a tutorial into permission to mutate a device or server.
6. Ask the operator before an action requires credentials, network exposure,
   deployment, firmware writing, deletion, purchase, or publication.
7. Preserve `available`, `under_construction`, `planned`, and `unavailable`
   component states from the local-setup catalog.
8. Stop the executable setup journey when the official releases page contains
   no verified archive; do not substitute an internal build or invented URL.
9. Ask for one beginner-sized result at a time and never ask the operator to
   reveal a password, JWT secret, private key, database dump, or player data.
10. For creative tools, check the current `verified_on` date and official
    pricing/license link; describe the pricing model and never copy an exact
    price into this repository.
11. Prefer free, open-source, and local tools before cloud services. Never upload
    confidential assets, player data, or unlicensed content to a third party.
12. Treat Kanboard as the visible human source of truth. Botte Secrète may
    propose routing and checks, but it must not mutate Kanboard automatically by
    default.

The canonical machine-readable list is [context-index.json](context-index.json).
